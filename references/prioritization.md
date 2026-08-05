# Priorisation

Séparer la force de la demande client de la décision de mise en œuvre. Le score ordonne le jugement ; il ne remplace pas les preuves.

## Score d'opportunité

Noter chaque critère disponible de 1 à 5 :

| Critère | Poids | Interprétation |
| --- | ---: | --- |
| Couverture des clients | 20 % | Nombre et diversité de clients indépendants concernés |
| Intensité du problème | 15 % | Sévérité, coût, délai, risque ou fréquence du problème |
| Caractère critique du processus | 15 % | Place du besoin dans un processus essentiel |
| Alignement stratégique | 15 % | Alignement explicite avec la cible et la direction produit |
| Pertinence commerciale | 10 % | Lien étayé avec l'adoption, la rétention, l'expansion, la marge ou le coût |
| Qualité des preuves | 10 % | Spécificité, spontanéité, traçabilité et indépendance |
| Fréquence | 10 % | Récurrence parmi les sources indépendantes couvertes |
| Récence | 5 % | Pertinence pour la version et le contexte actuels |

Calculer uniquement sur les critères disponibles :

```text
score = somme(note × poids disponible) / somme(poids disponible) × 20
```

Reporter la complétude. Ne jamais convertir une donnée manquante en note 1.

## Confiance

- `high` — plusieurs clients indépendants, exemples spécifiques, bon contexte de segment, peu de contradictions majeures.
- `medium` — signal répété mais couverture incomplète, questions orientées ou contre-preuves significatives.
- `low` — signal isolé, vague, ancien, hypothétique, dupliqué ou fortement inféré.

Abaisser la confiance si le thème vient surtout de questions orientées, d'un seul compte dominant, d'une attribution de voix incertaine ou d'une transcription partielle.

## Décision

- `commit` — problème important, stratégie et solution suffisamment établies, dépendances acceptables.
- `validate` — opportunité plausible mais incertitude sur le problème, la solution, le segment ou la faisabilité.
- `defer` — valeur possible mais dépendance, calendrier ou cible non prioritaire.
- `park` — preuves faibles, contradiction forte ou faible alignement.

Une forte demande client n'impose pas la décision `commit`. Une fonctionnalité peut rester en `validate` si la solution demandée est incertaine. Ces valeurs sont des identifiants techniques du format JSON.

## Couche de mise en œuvre séparée

Ne pas mélanger dans le score client :

- effort et complexité d'ingénierie ;
- dépendances liées aux données, à la sécurité, aux droits, aux connecteurs ou à la couche sémantique ;
- risque de maintenance ;
- compatibilité avec le lot en cours ;
- séquençage technique.

Obtenir ces éléments depuis la feuille de route existante, les spécifications, l'équipe technique ou une estimation explicitement fournie. S'ils sont indisponibles, indiquer qu'ils sont inconnus et recommander un chiffrage.

## Maintenant / Ensuite / Plus tard

- Maintenant : décision ou validation à lancer immédiatement, prérequis inclus.
- Ensuite : élément conditionné par un résultat mesurable ou un prérequis identifié.
- Plus tard : signal crédible hors séquence actuelle, ou option à reconsidérer avec une condition claire.

Chaque élément doit contenir : pourquoi maintenant, preuves, contre-preuves, dépendances, critère de décision et mesure de succès.

## Règles d'arbitrage

- Compter les organisations et rôles concernés, pas les mentions brutes.
- Expliquer lorsqu'un segment stratégique minoritaire l'emporte sur la majorité.
- Prioriser le problème avant la solution littérale proposée.
- Ne pas produire de prévision précise de revenus à partir d'entretiens qualitatifs.
- Lorsque l'effort est inconnu, recommander une exploration technique ou un chiffrage, pas un quadrant impact/effort fictif.
