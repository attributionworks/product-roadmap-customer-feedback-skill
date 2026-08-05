# Spécification du rapport

Créer un JSON canonique, puis générer le document et les éventuels exports à partir de cette source unique.

## Objet racine

```json
{
  "meta": {},
  "dataset": {},
  "verdict": {},
  "interview_summaries": [],
  "themes": [],
  "features": [],
  "roadmap": {"now": [], "next": [], "later": []},
  "risks": [],
  "open_questions": [],
  "evidence": [],
  "sources": []
}
```

## Champs essentiels

### `meta`

`project`, `product`, `decision_scope`, `mode`, `language`, `generated_at`, `shareability` (`private`, `redacted` ou `public`).

### `dataset`

`interviews`, `client_organizations`, `participants`, `date_range`, `coverage`, `missing_metadata`, `duplicate_rate`, `confidence`, `confidence_reason`, `biases`, `excluded_sources`.

### `verdict`

`headline`, `summary`, `strongest_signal`, `biggest_uncertainty`, `recommended_decision`.

### `interview_summaries`

Pour chaque entretien : `source_id`, `client_org`, `participants`, `context`, `jobs`, `pains`, `requested_features`, `outcomes`, `objections`, `evidence_ids`.

### `themes`

`id`, `name`, `type`, `statement`, `evidence_ids`, `counter_evidence_ids`, `distinct_clients`, `roles`, `segments`, `confidence`, `interpretation`, `alternative_explanations`.

### `features`

`id`, `name`, `problem`, `solution_hypothesis`, `target_users`, `theme_ids`, `evidence_ids`, `counter_evidence_ids`, `scores`, `score_completeness`, `priority_score`, `confidence`, `decision`, `dependencies`, `effort`, `recommendation`, `validation_needed`, `success_metric`.

### `roadmap`

Utiliser `now`, `next`, `later`. Chaque item contient `feature_id`, `action`, `rationale`, `evidence_ids`, `dependencies`, `gate`, `success_signal`.

### `risks`

`risk`, `type`, `affected_feature_ids`, `evidence_ids`, `mitigation`.

### `open_questions`

`question`, `why`, `method`, `target_segment`, `related_feature_ids`.

### `evidence`

Utiliser le registre défini dans `evidence-model.md`. Ajouter `shareable_text` pour les livrables expurgés ou publics.

### `sources`

`source_id`, `title`, `type`, `date`, `participants`, `client_org`, `locator`, `transcript_status`, `privacy`, `inclusion_status`.

## Ordre du document

1. Synthèse exécutive et décision recommandée
2. Périmètre, méthode et niveau de confiance
3. Ce que les clients cherchent réellement à accomplir
4. Thèmes transverses et contre-signaux
5. Opportunités de fonctionnalités classées
6. Feuille de route « Maintenant / Ensuite / Plus tard » ou séquence de validation
7. Dépendances, risques et arbitrages
8. Questions ouvertes et plan de recherche
9. Annexe : synthèse par entretien
10. Annexe : registre des preuves

## Contraintes

- Toute citation visible provient directement de `evidence.verbatim` ou `shareable_text`.
- Toute recommandation cite au moins un ID de preuve.
- Tous les IDs référencés existent.
- Les scores numériques ne sont présents que lorsqu'ils sont justifiés.
- Les données privées ne figurent pas dans un rapport expurgé ou public.
- Le titre et la synthèse restent orientés décision, pas volume de contenu.
