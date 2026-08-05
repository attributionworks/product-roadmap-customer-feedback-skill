# Contexte spécialisé pour Cockpit

Charger cette référence uniquement pour le projet Cockpit. Ce cadrage facilite la classification ; il ne remplace ni les verbatims, ni la feuille de route et les spécifications actuelles.

## Contexte de travail à confirmer

Cockpit est une plateforme agentique construite au-dessus des expertises de CyberCité et TimeOne. Le premier socle vise la centralisation des données de performance dans un lac de données et leur interrogation en langage naturel, avec une restitution sous forme de tableaux de bord. La feuille de route suivante doit être arbitrée à partir des besoins clients, des dépendances liées aux données et de la stratégie du groupe.

Avant analyse, confirmer si ce cadrage et le périmètre du lot courant sont toujours valides.

## Segments utiles

N'utiliser un segment que s'il est explicitement connu :

- annonceur vs équipe agence ;
- direction marketing vs expert canal vs données et mesure vs direction générale ;
- PME/ETI/grand compte ;
- maturité des données et de l'IA ;
- mono-canal vs multi-canal ;
- utilisateur opérationnel vs décideur/acheteur ;
- expertise : SEO, SEA, social ads, programmatique, affiliation, analytics/CRM.

## Taxonomie des fonctionnalités

- `data-foundation` — connecteurs, fraîcheur, historique, qualité, droits, cloisonnement entre clients.
- `identity-and-reconciliation` — taxonomie, mapping, identité, entités, métriques, déduplication.
- `semantic-layer` — définitions métier, dimensions, règles de calcul, contexte client.
- `global-search-and-nlq` — recherche transverse, questions en langage naturel, navigation.
- `dashboarding-and-reporting` — visualisations, exports, commentaires, alertes, partage.
- `cross-channel-insights` — arbitrage de canaux, attribution, anomalies, recommandations.
- `seo-geo-and-content` — audit SEO/GEO, clusters, knowledge graph, contenu.
- `automation-and-agents` — workflows autonomes ou supervisés, activation, génération.
- `collaboration-and-memory` — briefs, décisions, livrables, historique, gouvernance.
- `admin-security-and-governance` — rôles, confidentialité, validation, auditabilité.
- `agent-quality-and-ops` — évaluations, observabilité, coûts, feedback et amélioration.

Créer une nouvelle catégorie si un verbatim ne correspond pas proprement à cette taxonomie.

## Dépendances à rendre visibles

- Une fonctionnalité de recommandation dépend souvent de la qualité et de la fraîcheur des données.
- Une interrogation en langage naturel dépend d'une couche sémantique et d'une gouvernance des métriques.
- Un enseignement multicanal peut dépendre de la réconciliation des entités et des identités.
- Une automatisation d'activation nécessite permissions, validation humaine, journalisation et mécanisme de retour arrière.
- Une mémoire client nécessite un cloisonnement entre clients, un cycle de vie des données et des règles d'accès.

Ne pas placer une fonctionnalité aval dans la priorité immédiate sans traiter son prérequis ou expliciter que cette priorité correspond à une validation et non à une mise en production.

## Angles d'analyse spécifiques

Pour chaque signal, préciser si le client demande surtout :

- accès plus rapide à l'information ;
- compréhension ou explication ;
- décision ou recommandation ;
- production d'un livrable ;
- exécution/activation ;
- mémoire et continuité ;
- confiance, contrôle ou gouvernance.

Cette distinction évite de regrouper sous « IA » des besoins et niveaux de risque très différents.
