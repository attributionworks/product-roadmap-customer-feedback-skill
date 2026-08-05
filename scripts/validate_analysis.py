#!/usr/bin/env python3
"""Valider un fichier JSON d'analyse des retours clients et ses liens de preuve."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

WEIGHTS = {
    "client_breadth": 0.20,
    "pain_intensity": 0.15,
    "workflow_criticality": 0.15,
    "strategic_fit": 0.15,
    "commercial_relevance": 0.10,
    "evidence_quality": 0.10,
    "frequency": 0.10,
    "recency": 0.05,
}
SPEAKERS = {"customer", "interviewer", "internal", "unknown"}
CONSENT = {"publishable", "permission-unknown", "internal-only", "unknown"}
DECISIONS = {"commit", "validate", "defer", "park"}


def as_list(value):
    return value if isinstance(value, list) else []


def normalized_score(scores):
    available = [(WEIGHTS[key], value) for key, value in scores.items() if key in WEIGHTS and isinstance(value, (int, float))]
    if not available:
        return None
    return sum(weight * value for weight, value in available) / sum(weight for weight, _ in available) * 20


def validate(data):
    errors, warnings = [], []
    for key in ("meta", "dataset", "verdict", "roadmap"):
        if not isinstance(data.get(key), dict):
            errors.append(f"{key} doit être un objet")
    for key in ("interview_summaries", "themes", "features", "risks", "open_questions", "evidence", "sources"):
        if not isinstance(data.get(key), list):
            errors.append(f"{key} doit être un tableau")

    meta = data.get("meta", {})
    for key in ("project", "decision_scope", "language", "shareability"):
        if not meta.get(key):
            errors.append(f"meta.{key} est obligatoire")

    source_ids = {item.get("source_id") for item in as_list(data.get("sources")) if item.get("source_id")}
    evidence_ids, evidence_by_id = set(), {}
    for index, item in enumerate(as_list(data.get("evidence"))):
        prefix = f"evidence[{index}]"
        evidence_id = item.get("id")
        if not evidence_id:
            errors.append(f"{prefix}.id est obligatoire")
        elif evidence_id in evidence_ids:
            errors.append(f"identifiant de preuve en double : {evidence_id}")
        else:
            evidence_ids.add(evidence_id)
            evidence_by_id[evidence_id] = item
        if not item.get("source_id"):
            errors.append(f"{prefix}.source_id est obligatoire")
        elif item.get("source_id") not in source_ids:
            errors.append(f"{prefix}.source_id référence une source inconnue : {item.get('source_id')}")
        if not item.get("verbatim") and not item.get("shareable_text"):
            errors.append(f"{prefix} doit contenir verbatim ou shareable_text")
        if item.get("speaker_kind") not in SPEAKERS:
            errors.append(f"{prefix}.speaker_kind doit appartenir à {sorted(SPEAKERS)}")
        if item.get("consent", "unknown") not in CONSENT:
            errors.append(f"{prefix}.consent doit appartenir à {sorted(CONSENT)}")
        if meta.get("shareability") in {"redacted", "public"} and not item.get("shareable_text"):
            errors.append(f"{prefix}.shareable_text est obligatoire pour un rapport partageable")
        if meta.get("shareability") == "public" and item.get("consent") != "publishable":
            warnings.append(f"{prefix} n'est pas publiable ; sa citation sera masquée")

    feature_ids = set()
    theme_ids = set()
    references = []
    for index, theme in enumerate(as_list(data.get("themes"))):
        theme_id = theme.get("id")
        if not theme_id:
            errors.append(f"themes[{index}].id est obligatoire")
        elif theme_id in theme_ids:
            errors.append(f"identifiant de thème en double : {theme_id}")
        else:
            theme_ids.add(theme_id)
        references.extend(as_list(theme.get("evidence_ids")))
        references.extend(as_list(theme.get("counter_evidence_ids")))
    for index, feature in enumerate(as_list(data.get("features"))):
        feature_id = feature.get("id")
        if not feature_id:
            errors.append(f"features[{index}].id est obligatoire")
        elif feature_id in feature_ids:
            errors.append(f"identifiant de fonctionnalité en double : {feature_id}")
        else:
            feature_ids.add(feature_id)
        references.extend(as_list(feature.get("evidence_ids")))
        references.extend(as_list(feature.get("counter_evidence_ids")))
        for theme_id in as_list(feature.get("theme_ids")):
            if theme_id not in theme_ids:
                errors.append(f"features[{index}] référence un thème inconnu : {theme_id}")
        if feature.get("decision") not in DECISIONS:
            errors.append(f"features[{index}].decision doit appartenir à {sorted(DECISIONS)}")
        scores = feature.get("scores", {})
        if not isinstance(scores, dict):
            errors.append(f"features[{index}].scores doit être un objet")
            scores = {}
        for key, value in scores.items():
            if key not in WEIGHTS:
                warnings.append(f"features[{index}].scores.{key} n'est pas un critère standard")
            elif not isinstance(value, (int, float)) or not 1 <= value <= 5:
                errors.append(f"features[{index}].scores.{key} doit être compris entre 1 et 5")
        expected = normalized_score(scores)
        actual = feature.get("priority_score")
        if expected is not None and isinstance(actual, (int, float)) and not math.isclose(expected, actual, abs_tol=0.6):
            errors.append(f"features[{index}].priority_score devrait valoir {expected:.1f}, valeur reçue : {actual}")
        if not as_list(feature.get("evidence_ids")):
            warnings.append(f"features[{index}] ne possède aucune preuve favorable")

    roadmap = data.get("roadmap", {})
    for lane in ("now", "next", "later"):
        if not isinstance(roadmap.get(lane), list):
            errors.append(f"roadmap.{lane} doit être un tableau")
            continue
        for index, item in enumerate(roadmap[lane]):
            if item.get("feature_id") not in feature_ids:
                errors.append(f"roadmap.{lane}[{index}] référence une fonctionnalité inconnue : {item.get('feature_id')}")
            references.extend(as_list(item.get("evidence_ids")))

    for risk in as_list(data.get("risks")):
        references.extend(as_list(risk.get("evidence_ids")))
        for feature_id in as_list(risk.get("affected_feature_ids")):
            if feature_id not in feature_ids:
                errors.append(f"un risque référence une fonctionnalité inconnue : {feature_id}")

    for index, summary in enumerate(as_list(data.get("interview_summaries"))):
        if summary.get("source_id") not in source_ids:
            errors.append(f"interview_summaries[{index}] référence une source inconnue : {summary.get('source_id')}")
        references.extend(as_list(summary.get("evidence_ids")))

    for index, question in enumerate(as_list(data.get("open_questions"))):
        for feature_id in as_list(question.get("related_feature_ids")):
            if feature_id not in feature_ids:
                errors.append(f"open_questions[{index}] référence une fonctionnalité inconnue : {feature_id}")

    for reference in references:
        if reference not in evidence_ids:
            errors.append(f"référence de preuve inconnue : {reference}")

    for feature in as_list(data.get("features")):
        supporting = [evidence_by_id[eid] for eid in as_list(feature.get("evidence_ids")) if eid in evidence_by_id]
        if supporting and not any(item.get("speaker_kind") == "customer" for item in supporting):
            warnings.append(f"la fonctionnalité {feature.get('id')} ne possède aucune preuve issue de la voix du client")

    return errors, warnings


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Utilisation : validate_analysis.py <analyse.json>")
    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    errors, warnings = validate(data)
    for warning in warnings:
        print(f"AVERTISSEMENT : {warning}")
    if errors:
        print("ANALYSE INVALIDE", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"VALIDE : {path} ({len(data.get('evidence', []))} preuves, {len(data.get('features', []))} fonctionnalités)")


if __name__ == "__main__":
    main()
