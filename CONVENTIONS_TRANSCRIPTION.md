# Conventions de transcription

Adaptation des [conventions de FelixBerloty](https://github.com/grostim/FelixBerloty/blob/master/CONVENTIONS_TRANSCRIPTION.md), consultées le 20 octobre 2026, pour le tapuscrit **Adrien Berloty (1851 - 1905)** de **Léon Peillon**. Le texte n'est pas attribué à Adrien ni à Félix Berloty.

## Sources et séquençage

- 32 photographies : IMGP0125.JPG pour la couverture, puis IMGP0126.JPG à IMGP0156.JPG pour les pages 1 à 31. La page 1 ne porte pas de numéro visible ; la dernière est également sans numéro. La numérotation 1 à 31 est la correspondance documentaire retenue, cohérente avec les numéros imprimés 2 à 30.
- Copies inchangées dans `Originaux/`, noms normalisés et empreintes SHA-256 dans `manifest.csv`.
- Lecture des photographies avec OCR local auxiliaire. Cette méthode diffère de la lecture sans OCR indiquée pour FelixBerloty ; aucun nom de modèle ou de transcripteur de l'autre projet n'est recopié comme attribution du présent travail.
- Le Markdown est la source éditoriale unique ; le LaTeX à la racine en dérive par Pandoc. Les exports locaux PDF et EPUB et les artefacts de CI dérivent du même texte.
- Les commentaires relient les pages sources au texte. La phrase interrompue entre les pages 17 et 18 est réunie dans un seul paragraphe ; son repère de provenance est inline.

## Présentation

- Classe LaTeX `report`, A4, 11 pt, Latin Modern, Babel français, marges de 2,5 cm, en-têtes discrets et pagination propre à l'édition.
- La couverture est représentée par une page de titre : Adrien Berloty, 1851 - 1905, Léon Peillon, 1er mai 1993 (date complète donnée à la fin du texte). La mention « Transcription des 31 pages du tapuscrit familial » est retirée à la demande de l’utilisateur du 21 octobre 2026.
- Le tapuscrit n'a pas de chapitres nommés. Les sept titres ajoutés sont documentés ici comme éditoriaux. Ils reprennent les principales transitions du texte ; les séparateurs originaux sont conservés ou représentés par ces transitions.
- Aucun portrait, QR code ou identifiant Gramps n'est inventé ou repris d'un autre document.

## Texte et normalisations

- Conserver les paragraphes, le vocabulaire, les tournures, les abréviations, les unités (Ha, Km, H, F) et la forme des dates et montants.
- Corriger les erreurs mécaniques I/O pour 1/0, espaces, césures, coquilles et accords manifestes. Réunir les mots séparés par la machine ou l'OCR ; ligatures françaises et ponctuation lisible.
- Passer les noms propres en casse usuelle, sans inventer leur identification. Corriger Dumoustier en Demoustier (p. 9), conformément à la réponse de l’utilisateur du 21 octobre 2026. Les lectures douteuses sont consignées dans le relevé éditorial, puis soumises à l’utilisateur une par une.
- Corriger le décès de Joséphine Coste en 1855 conformément à la réponse de l’utilisateur du 21 octobre 2026. Conserver, conformément aux réponses de l’utilisateur : « à peine 12 ans » pour Adrien, « classe 91 », « neuf ans plus tôt », les âges de 23 et 35 ans pour Bonaventure et de 12 ans pour Marie. Ne pas appliquer les corrections ou divergences d'une autre transcription à celle-ci.
- Les hypothèses d'appartenance à la Congrégation, les motifs de retraite et les appréciations politiques restent les propos de l'auteur.

- Corriger « Rérum Noverrum » en « Rerum novarum » aux deux occurrences (p. 20 et 21), conformément à la réponse de l’utilisateur du 21 octobre 2026.

- Corriger « Prudhommat » en « Prudhomat » (p. 12), conformément à la réponse de l’utilisateur du 21 octobre 2026.

- Corriger « Lubresac » en « Loubressac » (p. 12), conformément à la réponse de l’utilisateur du 21 octobre 2026.

- Corriger « Lantigne » en « Lantignié » aux deux occurrences (p. 7 et 11), conformément à la réponse de l’utilisateur du 21 octobre 2026.

- Corriger « Einselden » en « Einsiedeln » (p. 28), conformément à la réponse de l’utilisateur du 21 octobre 2026.

- Corriger « Koningsee » en « Königssee » (p. 25), conformément à la réponse de l’utilisateur du 21 octobre 2026.

- Corriger « Clémenceau » en « Clemenceau » (p. 28), conformément à la réponse de l’utilisateur du 21 octobre 2026.

- Corriger « Trillon » en « Trion » (p. 28), conformément à la réponse de l’utilisateur du 21 octobre 2026.

## Manuscrit et notes

- Intégrer les corrections lisibles : « et à » (p. 10), « Saint-Just » (p. 22), « peu lumineuses » (p. 23), « politiques ou religieuses » (p. 24), « ne » (p. 25), « nue propriété » (p. 31).
- La note manuscrite sur Isaac Coste (p. 9) est conservée comme note de l'auteur.
- Le soulignement « maire de Saint-Antoine d'Ouroux » (p. 21) est rendu en gras.
- À la demande de l’utilisateur, aucune note de bas de page ajoutée par le transcripteur ne figure dans l’édition. Seule la note manuscrite de l’original sur Isaac Coste est conservée. Les points douteux sont traités dans le relevé éditorial et discutés un par un dans la conversation avant correction du texte.

## Construction et versionnement

`python3 scripts/build.py` génère les trois formats ; `--source-only` régénère le LaTeX. La CI reprend la compilation double passe, les exports, l'injection de version et les releases automatiques du dépôt modèle. Les Conventional Commits éventuels sont en français. Les fichiers temporaires et sorties générées sont ignorés par Git.

31/31 pages et couverture transcrites ; la relecture humaine reste souhaitable pour les noms rares et la validation historique.
