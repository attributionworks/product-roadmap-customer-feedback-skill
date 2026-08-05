#!/usr/bin/env python3
"""Générer un rapport Markdown décisionnel depuis un JSON d'analyse validé."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def items(value):
    return value if isinstance(value, list) else []


def text(value, fallback="Non renseigné"):
    if value is None or value == "":
        return fallback
    if isinstance(value, list):
        return ", ".join(str(item) for item in value) or fallback
    return str(value)


def evidence_links(ids):
    return ", ".join(f"`{eid}`" for eid in items(ids)) or "Aucune preuve reliée"


def render(data):
    meta = data["meta"]
    dataset = data["dataset"]
    verdict = data["verdict"]
    evidence = {item["id"]: item for item in items(data.get("evidence")) if item.get("id")}
    lines = [
        f"# {text(meta.get('project'))} — Synthèse des retours clients et feuille de route",
        "",
        f"**Décision couverte :** {text(meta.get('decision_scope'))}  ",
        f"**Niveau de confiance :** {text(dataset.get('confidence'))}  ",
        f"**Périmètre :** {text(dataset.get('coverage'))}",
        "",
        "## 1. Synthèse exécutive",
        "",
        f"### {text(verdict.get('headline'))}",
        "",
        text(verdict.get("summary")),
        "",
        f"- **Signal le plus fort :** {text(verdict.get('strongest_signal'))}",
        f"- **Incertitude principale :** {text(verdict.get('biggest_uncertainty'))}",
        f"- **Décision recommandée :** {text(verdict.get('recommended_decision'))}",
        "",
        "## 2. Corpus et méthode",
        "",
        f"- Entretiens : {text(dataset.get('interviews'))}",
        f"- Organisations clientes : {text(dataset.get('client_organizations'))}",
        f"- Participants : {text(dataset.get('participants'))}",
        f"- Période : {text(dataset.get('date_range'))}",
        f"- Confiance : {text(dataset.get('confidence_reason'))}",
        f"- Biais et limites : {text(dataset.get('biases'))}",
        "",
        "## 3. Besoins et thèmes transverses",
        "",
    ]

    for theme in items(data.get("themes")):
        lines += [
            f"### {text(theme.get('id'))} — {text(theme.get('name'))}",
            "",
            text(theme.get("statement")),
            "",
            f"- Clients distincts : {text(theme.get('distinct_clients'))}",
            f"- Rôles : {text(theme.get('roles'))}",
            f"- Confiance : {text(theme.get('confidence'))}",
            f"- Interprétation : {text(theme.get('interpretation'))}",
            f"- Preuves : {evidence_links(theme.get('evidence_ids'))}",
            f"- Contre-preuves : {evidence_links(theme.get('counter_evidence_ids'))}",
            "",
        ]

    lines += ["## 4. Opportunités de fonctionnalités", ""]
    features = sorted(items(data.get("features")), key=lambda item: item.get("priority_score") or -1, reverse=True)
    for feature in features:
        score = feature.get("priority_score")
        score_label = f"{score:.1f}/100" if isinstance(score, (int, float)) else "non calculé"
        lines += [
            f"### {text(feature.get('id'))} — {text(feature.get('name'))}",
            "",
            f"**Décision : {text(feature.get('decision')).upper()} · Score : {score_label} · Confiance : {text(feature.get('confidence'))}**",
            "",
            f"- Problème : {text(feature.get('problem'))}",
            f"- Hypothèse de solution : {text(feature.get('solution_hypothesis'))}",
            f"- Utilisateurs cibles : {text(feature.get('target_users'))}",
            f"- Recommandation : {text(feature.get('recommendation'))}",
            f"- Validation requise : {text(feature.get('validation_needed'))}",
            f"- Mesure de succès : {text(feature.get('success_metric'))}",
            f"- Dépendances : {text(feature.get('dependencies'))}",
            f"- Effort : {text(feature.get('effort'), 'Inconnu')}",
            f"- Preuves : {evidence_links(feature.get('evidence_ids'))}",
            f"- Contre-preuves : {evidence_links(feature.get('counter_evidence_ids'))}",
            "",
        ]

    lines += ["## 5. Feuille de route", ""]
    for lane, title in (("now", "Maintenant"), ("next", "Ensuite"), ("later", "Plus tard")):
        lines += [f"### {title}", ""]
        for item in items(data.get("roadmap", {}).get(lane)):
            lines += [
                f"- **{text(item.get('feature_id'))} — {text(item.get('action'))}**",
                f"  - Pourquoi : {text(item.get('rationale'))}",
                f"  - Critère de décision : {text(item.get('gate'))}",
                f"  - Signal de succès : {text(item.get('success_signal'))}",
                f"  - Dépendances : {text(item.get('dependencies'))}",
                f"  - Preuves : {evidence_links(item.get('evidence_ids'))}",
            ]
        if not items(data.get("roadmap", {}).get(lane)):
            lines.append("Aucun élément suffisamment étayé.")
        lines.append("")

    lines += ["## 6. Risques et arbitrages", ""]
    for risk in items(data.get("risks")):
        lines += [
            f"- **{text(risk.get('risk'))}** — {text(risk.get('mitigation'))}",
            f"  - Fonctionnalités concernées : {text(risk.get('affected_feature_ids'))}",
            f"  - Preuves : {evidence_links(risk.get('evidence_ids'))}",
        ]
    if not items(data.get("risks")):
        lines.append("Aucun risque documenté.")

    lines += ["", "## 7. Questions ouvertes et plan de validation", ""]
    for question in items(data.get("open_questions")):
        lines += [
            f"- **{text(question.get('question'))}**",
            f"  - Pourquoi : {text(question.get('why'))}",
            f"  - Méthode : {text(question.get('method'))}",
            f"  - Segment cible : {text(question.get('target_segment'))}",
        ]

    lines += ["", "## Annexe A — Synthèse par entretien", ""]
    for summary in items(data.get("interview_summaries")):
        lines += [
            f"### {text(summary.get('source_id'))} — {text(summary.get('client_org'))}",
            "",
            f"- Contexte : {text(summary.get('context'))}",
            f"- Tâches à accomplir : {text(summary.get('jobs'))}",
            f"- Irritants : {text(summary.get('pains'))}",
            f"- Fonctionnalités demandées : {text(summary.get('requested_features'))}",
            f"- Résultats : {text(summary.get('outcomes'))}",
            f"- Objections : {text(summary.get('objections'))}",
            f"- Preuves : {evidence_links(summary.get('evidence_ids'))}",
            "",
        ]

    lines += ["## Annexe B — Registre des preuves", ""]
    for eid in sorted(evidence):
        item = evidence[eid]
        if meta.get("shareability") == "public" and item.get("consent") != "publishable":
            quote = "[Citation masquée — autorisation de publication absente]"
        elif meta.get("shareability") in {"redacted", "public"}:
            quote = item.get("shareable_text")
        else:
            quote = item.get("verbatim")
        lines += [
            f"### {eid}",
            "",
            f"> {text(quote)}",
            "",
            f"Source : {text(item.get('source_id'))} · Client : {text(item.get('client_org'))} · Rôle : {text(item.get('role'))} · Type : {text(item.get('statement_type'))} · Localisateur : {text(item.get('transcript_locator'))}",
            "",
        ]
    return "\n".join(lines).rstrip() + "\n"


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Utilisation : render_feedback_report.py <analyse.json> <rapport.md>")
    input_path, output_path = Path(sys.argv[1]), Path(sys.argv[2])
    data = json.loads(input_path.read_text(encoding="utf-8"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render(data), encoding="utf-8")
    print(f"CRÉÉ : {output_path.resolve()}")


if __name__ == "__main__":
    main()
