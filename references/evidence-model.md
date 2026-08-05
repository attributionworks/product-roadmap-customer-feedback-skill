# Modèle de preuves

Classer ce que la personne a réellement exprimé avant d'interpréter ce que l'équipe produit doit faire.

## Types d'affirmations

- `pain` — coût, délai, risque, difficulté ou frustration actuelle.
- `job` — progrès recherché dans une situation donnée.
- `desired_outcome` — résultat souhaité, non encore démontré.
- `observed_behavior` — action ou processus actuel décrit concrètement.
- `workaround` — contournement manuel ou outil alternatif.
- `feature_request` — solution ou capacité explicitement demandée.
- `verified_outcome` — résultat concret que le client dit avoir obtenu.
- `objection` — frein à l'adoption, l'usage, la confiance ou l'expansion.
- `purchase_trigger` — événement ayant provoqué l'évaluation ou l'achat.
- `churn_risk` — motif explicite de réduction, départ ou non-renouvellement.
- `commercial_signal` — lien explicite avec vente, renouvellement, marge ou coût.
- `praise` — appréciation positive sans résultat spécifique.
- `question` — demande d'information.
- `counter_evidence` — signal qui contredit ou limite un thème.
- `noise` — contenu sans sens produit défendable.

Autoriser plusieurs types si chacun est justifié.

## Temporalité et force

Qualifier :

- `current_behavior` — pratique réellement en cours ;
- `past_behavior` — pratique ou problème historique ;
- `hypothetical_intent` — intention déclarée ou scénario imaginé ;
- `future_requirement` — condition nécessaire annoncée ;
- `unknown`.

Ne pas traiter « je l'utiliserais » comme un comportement ou un achat.

## Registre minimal

Chaque élément contient au minimum :

```json
{
  "id": "E-001",
  "source_id": "GRA-2026-07-18-ACME-01",
  "interview_title": "Entretien Acme",
  "date": "2026-07-18",
  "client_org": "Acme",
  "participant_id": "P-01",
  "role": "Responsable SEA",
  "speaker_kind": "customer",
  "transcript_locator": "section 12 / 00:18:30",
  "verbatim": "Je passe encore deux heures à recouper les chiffres.",
  "language": "fr",
  "translation": null,
  "statement_type": ["pain", "workaround"],
  "prompt_status": "spontaneous",
  "temporality": "current_behavior",
  "feature_area": "cross-channel-reporting",
  "intensity": 4,
  "specificity": 5,
  "consent": "internal-only",
  "duplicate_of": null,
  "notes": ""
}
```

Utiliser `unknown` ou `null` pour les métadonnées absentes. Ne pas inférer un segment ou un rôle depuis un nom ou un domaine email.

## Indépendance et doublons

- Une même personne répétant un problème dix fois compte comme une seule source indépendante pour la fréquence.
- Plusieurs participants d'une même entreprise peuvent représenter des rôles distincts, mais ne valent pas automatiquement plusieurs clients.
- Un copier-coller, une citation répétée dans des notes ou une même transcription importée deux fois est un doublon.
- Deux clients distincts formulant le même problème ne sont pas des doublons.

## Anatomie d'un thème

Chaque thème contient : identifiant stable, nom orienté problème ou tâche à accomplir, affirmation, identifiants de preuve, clients distincts, rôles, segments, plage de dates, contre-preuves, alternative explicative, interprétation et confiance.

Garder séparés :

- le problème ou la tâche à accomplir ;
- le résultat attendu ;
- la solution demandée ;
- le bénéfice observé ;
- l'objection.

Les relier explicitement plutôt que de les fusionner.

## Saturation

Parler de saturation seulement au sein d'un segment comparable et après plusieurs entretiens indépendants. Mesurer l'apparition de nouveaux thèmes par vague d'entretien. Un consensus apparent entre trois interlocuteurs du même client n'est pas une saturation marché.
