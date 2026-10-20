# Adrien Berloty (1851 - 1905) - Léon Peillon

Transcription intégrale du tapuscrit familial signé **Léon Peillon, le 1er mai 1993**, d'après les 32 photographies fournies : une couverture et 31 pages de texte, dont la dernière sans numéro imprimé.

Projet préparé sur le modèle de [grostim/FelixBerloty](https://github.com/grostim/FelixBerloty) : originaux conservés, conventions éditoriales, source LaTeX principal à la racine, signalements d'erreurs et pipeline GitHub Actions produisant PDF, EPUB et Markdown avec versionnement automatique des releases. Aucun portrait n'est ajouté : les pièces fournies n'en contiennent pas.

## Lire et corriger

- [Transcription modifiable](transcription.md).
- [Source LaTeX généré](<Adrien Berloty.tex>).
- [Conventions de transcription](CONVENTIONS_TRANSCRIPTION.md).
- [Relevé éditorial et points à revoir](RELEVE_EDITORIAL.md).
- [Correspondance et empreintes des originaux](Originaux/manifest.csv).

Après construction locale : [PDF](output/pdf/Leon_Peillon_Adrien_Berloty.pdf), [EPUB](output/Leon_Peillon_Adrien_Berloty.epub), [Markdown](output/Leon_Peillon_Adrien_Berloty.md). Les sorties sont exclues du versionnement. Elles sont également prévues comme artefacts de CI et pièces jointes des releases, après publication effective sur GitHub. Aucun dépôt distant n'est créé par la construction.

## Structure

```text
.github/ISSUE_TEMPLATE/       Signalement des erreurs de transcription
.github/workflows/ci-release.yml
Originaux/                   Couverture.jpg, Page 01.jpg à Page 31.jpg, manifest.csv
Adrien Berloty.tex            Source LaTeX généré
transcription.md              Source éditoriale unique
scripts/build.py              Construction locale reproductible
scripts/template.tex          Mise en page LaTeX
scripts/pages.lua             Repères de provenance photographique
CONVENTIONS_TRANSCRIPTION.md
RELEVE_EDITORIAL.md
output/                      PDF, EPUB et Markdown générés
```

## Construire

Installer Python 3, Pandoc et TeX Live (pdflatex, babel-french, lmodern, geometry, parskip, fancyhdr et hyperref). Les paquets Debian nécessaires sont listés dans le workflow.

```sh
python3 scripts/build.py
```

Pour régénérer uniquement le LaTeX :

```sh
python3 scripts/build.py --source-only
```

Corriger `transcription.md`, puis reconstruire ; ne pas modifier directement le LaTeX généré. Deux passes PDF mettent à jour la table des matières. Les repères des photographies restent dans les commentaires Markdown et LaTeX ; ils n'imposent pas les sauts de page de l'édition.

## Pipeline et releases

Le workflow reprend celui de FelixBerloty, consulté le 20 octobre 2026 : construction sur les propositions, lancements manuels et mises à jour de `master` ou `main`, conservation des trois artefacts, puis release automatique sur un push vers `master` ou `main`. Le dernier titre de commit pilote la version : `feat` augmente la majeure, `fix`, `style`, `refactor`, `docs` ou `correction` augmentent la mineure, les autres augmentent le correctif. La version est injectée dans une copie temporaire du LaTeX. Les propositions et lancements manuels ne publient pas de release.

Les commits éventuels doivent suivre les Conventional Commits en français. Le workflow distant n'a pas été exécuté pendant la préparation locale.

## État et provenance

31/31 pages de texte transcrites et relues sur les photographies, ainsi que les mentions de couverture. Les corrections manuscrites lisibles sont intégrées ; les incohérences internes sont signalées sans correction historique conjecturale. Sept chapitres éditoriaux facilitent la lecture. La dernière page porte la signature et la date du 1er mai 1993.

Fichiers fournis : `IMGP0125.JPG` à `IMGP0156.JPG`, conservés octet pour octet. Les photographies arrivent dans un ordre mélangé dans le message ; l'ordre des noms correspond à l'ordre de lecture. Un OCR français local a servi de brouillon auxiliaire, repris par lecture des images. Les jugements et hypothèses du récit restent ceux de Léon Peillon. Une relecture humaine des noms propres rares et des actes cités reste utile. Aucune licence de redistribution des archives familiales n'est présumée.
