---
name: prioriser-retours-clients
description: Analyser des entretiens clients, des transcriptions Granola, des notes de recherche, des enquêtes, des retours du support ou des corpus qualitatifs mixtes afin de produire un registre de preuves traçable, des besoins, des hypothèses de fonctionnalités, des contradictions et une feuille de route produit étayée. Utiliser cette skill pour synthétiser la voix du client, comparer des segments, prioriser un portefeuille de fonctionnalités, préparer un document de retours produit, transformer des entretiens en recommandations ordonnées ou déterminer ce qu'il faut construire et ce qu'il faut d'abord valider. Optimisée pour les entretiens B2B en français ou multilingues et pour le projet Cockpit de CyberCité, tout en restant réutilisable pour d'autres produits. Ne jamais inventer, fusionner ni lisser les citations.
---

# Prioriser les retours clients

Transformer des retours clients qualitatifs en décisions produit défendables. Garder chaque conclusion reliée aux entretiens qui la soutiennent et rendre visibles les désaccords, les lacunes et les dépendances.

## Charger les références utiles

- Lire [references/granola-intake.md](references/granola-intake.md) avant toute recherche ou extraction depuis Granola.
- Lire [references/evidence-model.md](references/evidence-model.md) avant de découper, classer ou agréger les verbatims.
- Lire [references/prioritization.md](references/prioritization.md) avant de noter des opportunités ou d'ordonner une feuille de route.
- Lire [references/report-spec.md](references/report-spec.md) avant de créer le JSON canonique ou le document final.

## Choisir le mode

- `complet` — registre de preuves, synthèse, fonctionnalités, feuille de route et document final. Mode par défaut.
- `feuille-de-route` — besoins, opportunités, dépendances et ordre de traitement.
- `entretiens` — analyse entretien par entretien, thèmes transverses et saturation.
- `comparer` — comparaison par segment, métier, client, période ou niveau de maturité.
- `valider` — questions ouvertes, tests et preuves à collecter avant décision.

## Exécuter le processus

### 1. Définir la décision

- Reformuler la décision attendue : choix de fonctionnalités, cadrage d'un lot, validation d'une proposition de valeur ou comparaison de segments.
- Identifier la période, le périmètre produit, les clients inclus et l'audience du document.
- Inspecter d'abord les sources disponibles. Ne demander que les informations dont l'absence changerait réellement la recommandation.
- Si aucun contexte d'effort, d'architecture ou de stratégie n'est fourni, produire une priorité client et une séquence de validation, pas un plan de mise en œuvre prétendument certain.

### 2. Récupérer le corpus

- Pour Granola, suivre `references/granola-intake.md` et récupérer toutes les réunions correspondant au périmètre avant de conclure.
- Conserver le titre, la date, les participants, l'organisation cliente et un localisateur vérifiable pour chaque verbatim lorsque disponibles.
- Distinguer les propos du client, de l'intervieweur, d'un collaborateur interne et les locuteurs incertains.
- Ne jamais considérer la formulation d'une question de l'intervieweur comme une demande client.
- Signaler les transcriptions incomplètes, les attributions de locuteur incertaines et les entretiens absents.

### 3. Construire le registre de preuves

- Créer un item stable par affirmation autonome, sans découper au point de perdre la négation, la condition ou le contexte.
- Préserver le verbatim exact. Placer traductions, paraphrases et interprétations dans des champs distincts.
- Classer chaque item selon `references/evidence-model.md`.
- Compter les sources indépendantes au niveau client ou participant, pas le nombre de répétitions dans une même conversation.
- Marquer les doublons, les propos provoqués, l'intention hypothétique, les comportements observés et la contre-preuve.
- Utiliser la valeur technique `unknown` plutôt que d'inférer une donnée manquante.

### 4. Synthétiser sans écraser les nuances

- Produire d'abord une mini-synthèse par entretien : contexte, tâches à accomplir, irritants, attentes, fonctionnalités citées, signaux commerciaux, objections et citations clés.
- Regrouper ensuite les items sémantiquement équivalents en thèmes transverses.
- Séparer le problème, la tâche à accomplir, le résultat attendu et la solution demandée.
- Montrer pour chaque thème les clients distincts, segments, métiers, sources, verbatims et contre-signaux.
- Signaler la saturation uniquement lorsque les nouveaux entretiens n'apportent plus de thèmes majeurs dans un segment comparable.

### 5. Transformer les besoins en hypothèses de fonctionnalités

- Formuler chaque fonctionnalité comme une hypothèse de solution reliée à un problème ou à une tâche explicite.
- Conserver la demande littérale du client sans la confondre avec la solution recommandée.
- Identifier utilisateurs cibles, scénario, valeur attendue, dépendances, risques, mesure de succès et test de validation.
- Rattacher chaque fonctionnalité à ses identifiants de preuves et de contre-preuves.

### 6. Prioriser

- Appliquer le score de valeur et de qualité défini dans `references/prioritization.md` uniquement sur les critères disponibles.
- Garder effort, complexité, dépendances et risques séparés du score de demande client.
- Ne jamais inventer une estimation technique depuis les verbatims.
- Attribuer une décision explicite à chaque fonctionnalité, conformément au référentiel de priorisation.
- Produire un ordre « Maintenant / Ensuite / Plus tard » seulement si la stratégie et les contraintes permettent un séquençage crédible. Sinon produire une séquence « Décider / Tester / Mesurer ».
- Expliquer tout arbitrage où une fonctionnalité moins fréquente est priorisée pour des raisons stratégiques, commerciales ou de dépendance.

### 7. Produire les livrables

- Créer un JSON canonique conforme à `references/report-spec.md`.
- Le valider :

```bash
python3 scripts/validate_analysis.py outputs/<projet>-analyse-retours.json
```

- Générer la note Markdown :

```bash
python3 scripts/render_feedback_report.py outputs/<projet>-analyse-retours.json outputs/<projet>-feuille-de-route.md
```

- Si l'utilisateur demande un document Word ou PDF, utiliser les outils documentaires adaptés à partir du Markdown validé et vérifier visuellement la mise en page.
- Garder le registre complet privé. Dans un livrable partageable, pseudonymiser les personnes et clients sauf autorisation explicite.
- Retourner des liens cliquables vers les livrables demandés.

### 8. Vérifier avant livraison

- Vérifier que chaque citation du document existe exactement dans le registre.
- Vérifier que chaque recommandation et chaque fonctionnalité cite au moins un identifiant de preuve.
- Vérifier que les voix client ne sont pas gonflées par les relances de l'intervieweur ou les répétitions d'un même compte.
- Vérifier que les signaux contradictoires et les segments minoritaires pertinents restent visibles.
- Vérifier que la priorité immédiate ne contient pas une fonctionnalité dont une dépendance bloquante reste non traitée.
- Terminer par : décision recommandée, plus forte incertitude, données manquantes et prochain test.

## Garde-fous non négociables

- Ne jamais inventer, fusionner, lisser, compléter ou traduire silencieusement un verbatim.
- Ne jamais transformer une demande de fonctionnalité en preuve que cette solution est la bonne.
- Ne jamais présenter un volume qualitatif comme statistiquement représentatif.
- Ne jamais confondre intention déclarée, comportement actuel, résultat observé et impact commercial.
- Ne jamais masquer une contre-preuve pour rendre la conclusion plus nette.
- Ne jamais publier un nom ou une citation client sans consentement adapté à cet usage.
- Préférer la mention « preuves insuffisantes » à une recommandation artificiellement précise.
