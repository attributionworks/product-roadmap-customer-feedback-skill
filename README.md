# Prioriser les retours clients

Une skill réutilisable pour transformer des entretiens clients, des transcriptions Granola, des notes de recherche, des enquêtes ou des demandes adressées au support en décisions produit traçables.

Elle produit notamment :

- un registre de preuves relié aux sources ;
- une synthèse par entretien et des thèmes transverses ;
- des hypothèses de fonctionnalités avec contre-preuves et dépendances ;
- une notation explicable ;
- une feuille de route ou une séquence de validation ;
- un rapport Markdown généré depuis un JSON canonique.

La skill a été initialement conçue pour un projet B2B de plateforme marketing agentique, puis structurée pour rester utilisable sur d’autres produits et corpus multilingues.

## Principes

- Ne jamais inventer, fusionner ou « améliorer » un verbatim.
- Compter les sources indépendantes, pas le nombre de répétitions.
- Séparer le problème, le résultat attendu et la solution demandée.
- Rendre visibles les contre-preuves, les données manquantes et les biais.
- Ne pas déduire un effort technique précis depuis des entretiens qualitatifs.
- Conserver le registre complet privé et ne publier que des extraits autorisés.

## Installation

Copiez ce dépôt dans le répertoire de skills de votre environnement en conservant `SKILL.md` à la racine du dossier :

```text
skills/
└── prioriser-retours-clients/
    ├── SKILL.md
    ├── agents/
    ├── assets/
    ├── references/
    └── scripts/
```

Redémarrez ou rechargez ensuite l’environnement qui découvre les skills.

## Utilisation

Exemple de demande :

```text
Utilise $prioriser-retours-clients pour analyser ces entretiens comme un seul lot.
Construis un registre de preuves, identifie les besoins, propose des hypothèses de fonctionnalités
et une feuille de route argumentée. Ne modifie aucun verbatim.
```

La skill propose cinq modes :

- `complet` : analyse complète et livrables ;
- `feuille-de-route` : besoins, opportunités, dépendances et séquençage ;
- `entretiens` : analyse entretien par entretien ;
- `comparer` : comparaison entre segments ;
- `valider` : questions ouvertes et preuves à collecter.

## Processus technique

Le format de sortie canonique est décrit dans [`references/report-spec.md`](references/report-spec.md).

Valider une analyse :

```bash
python3 scripts/validate_analysis.py outputs/projet-analyse-retours.json
```

Générer un rapport Markdown :

```bash
python3 scripts/render_feedback_report.py \
  outputs/projet-analyse-retours.json \
  outputs/projet-feuille-de-route.md
```

## Structure

- [`SKILL.md`](SKILL.md) : déclenchement et processus principal ;
- [`references/granola-intake.md`](references/granola-intake.md) : constitution fidèle d’un corpus Granola ;
- [`references/evidence-model.md`](references/evidence-model.md) : modèle de preuve et règles d’agrégation ;
- [`references/prioritization.md`](references/prioritization.md) : notation, confiance et arbitrage ;
- [`references/report-spec.md`](references/report-spec.md) : schéma du JSON canonique et structure du rapport ;
- [`references/cockpit-overlay.md`](references/cockpit-overlay.md) : exemple de cadrage spécialisé pour une plateforme marketing agentique ;
- [`scripts/validate_analysis.py`](scripts/validate_analysis.py) : contrôle des IDs, liens de preuve et scores ;
- [`scripts/render_feedback_report.py`](scripts/render_feedback_report.py) : génération du Markdown.

## Confidentialité

Ce dépôt ne contient aucune transcription client ni aucun registre de preuves réel. Les noms et citations utilisés dans les exemples de schéma sont fictifs.

Avant toute publication d’un rapport généré, vérifiez les consentements, la pseudonymisation et le niveau de partage autorisé.

## Licence

MIT — Attribution Works.
