# Collecte depuis Granola

Utiliser cette procédure pour constituer un corpus fidèle depuis Granola ou depuis des exports Granola.

## Recherche et couverture

1. Définir les bornes : projet, période, entreprises, type d'entretien et mots-clés.
2. Chercher à la fois le nom du projet, les noms d'entreprises, les noms de participants et les termes métier probables.
3. Établir une liste de réunions candidates avec titre, date, participants et raison d'inclusion.
4. Dédupliquer les réunions retrouvées par plusieurs recherches.
5. Lire les notes et la transcription complète de chaque réunion incluse. Une note résumée seule ne suffit pas pour citer.
6. Tenir un journal des réunions incluses, exclues et introuvables.

Ne pas conclure à l'exhaustivité si le connecteur ne permet pas de l'établir. Écrire explicitement la couverture obtenue.

## Unité source

Attribuer un `source_id` stable à chaque réunion, par exemple `GRA-2026-07-18-ACME-01`. Conserver lorsque disponible :

- titre de réunion ;
- date et heure ;
- participants et organisation ;
- type d'entretien ;
- URL ou identifiant Granola ;
- plage temporelle ou section de la transcription ;
- statut de la transcription : complet, partiel ou incertain.

## Attribution des voix

- `customer` : participant client explicitement identifié.
- `interviewer` : personne qui mène l'entretien.
- `internal` : collaborateur interne apportant une opinion produit.
- `unknown` : attribution non suffisamment fiable.

Les propos `interviewer`, `internal` et `unknown` peuvent éclairer le contexte mais ne comptent pas comme demande client indépendante.

## Effet de questionnement

Qualifier chaque élément :

- `spontaneous` : thème introduit par le client sans suggestion de solution ;
- `prompted` : réponse à une question ouverte ;
- `leading` : réponse à une proposition orientée ou à une fonctionnalité nommée ;
- `unknown` : contexte insuffisant.

Une réponse `leading` reste une preuve, mais sa qualité est plus faible pour démontrer une demande spontanée.

## Qualité de la transcription

- Préserver les hésitations ou nuances qui changent le sens.
- Utiliser un localisateur plutôt qu'un horodatage inventé.
- Si un mot semble mal transcrit, conserver l'original et ajouter une note ; ne pas corriger la citation.
- Si une citation essentielle est ambiguë, la paraphraser hors guillemets et marquer le verbatim `uncertain`.

## Confidentialité

Traiter les transcriptions comme privées par défaut. Pseudonymiser dans le document final. Ne pas transférer le corpus vers un autre service sans instruction explicite de l'utilisateur.
