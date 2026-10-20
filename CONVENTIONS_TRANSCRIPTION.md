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
- La couverture est représentée par une page de titre : Adrien Berloty, 1851 - 1905, Léon Peillon, 1er mai 1993 (date complète donnée à la fin du texte).
- Le tapuscrit n'a pas de chapitres nommés. Les sept titres ajoutés sont documentés ici comme éditoriaux. Ils reprennent les principales transitions du texte ; les séparateurs originaux sont conservés ou représentés par ces transitions.
- Aucun portrait, QR code ou identifiant Gramps n'est inventé ou repris d'un autre document.

## Texte et normalisations

- Conserver les paragraphes, le vocabulaire, les tournures, les abréviations, les unités (Ha, Km, H, F) et la forme des dates et montants.
- Corriger les erreurs mécaniques I/O pour 1/0, espaces, césures, coquilles et accords manifestes. Réunir les mots séparés par la machine ou l'OCR ; ligatures françaises et ponctuation lisible.
- Passer les noms propres en casse usuelle, sans inventer leur identification. Conserver notamment Dumoustier (p. 9), Lantigne, Prudhommat, Lubresac, Koningsee, Einselden, Trillon et Clémenceau. La variante Dumoustier et les lectures des communes des Escouannes sont signalées en note.
- Conserver les dates et âges contradictoires : Joséphine Coste 1855/1862, « classe 91 », Bonaventure 23 ans et Marie 12 ans. Ne pas appliquer les corrections ou divergences d'une autre transcription à celle-ci.
- Les hypothèses d'appartenance à la Congrégation, les motifs de retraite et les appréciations politiques restent les propos de l'auteur.

## Manuscrit et notes

- Intégrer les corrections lisibles : « et à » (p. 10), « Saint-Just » (p. 22), « peu lumineuses » (p. 23), « politiques ou religieuses » (p. 24), « ne » (p. 25), « nue propriété » (p. 31).
- La note manuscrite sur Isaac Coste (p. 9) est conservée comme note de l'auteur.
- Le soulignement « maire de Saint-Antoine d'Ouroux » (p. 21) est rendu en gras.
- Toutes les notes ajoutées commencent par « (Note du transcripteur) ». Les incohérences sont signalées sans arbitrage historique ; le relevé éditorial distingue ces constatations des vérifications non effectuées.

## Construction et versionnement

`python3 scripts/build.py` génère les trois formats ; `--source-only` régénère le LaTeX. La CI reprend la compilation double passe, les exports, l'injection de version et les releases automatiques du dépôt modèle. Les Conventional Commits éventuels sont en français. Les fichiers temporaires et sorties générées sont ignorés par Git.

31/31 pages et couverture transcrites ; la relecture humaine reste souhaitable pour les noms rares et la validation historique.
