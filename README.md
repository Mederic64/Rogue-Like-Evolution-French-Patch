# Rogue Like Evolution : French patch

Welcome, this is my attempt at translating Rogue Like: Evolution by [Oni](https://www.patreon.com/OniArtist/) in french.

## Summary

Basically the intended idea is to generate translations with the Ren'Py SDK for the french language, use tools to extract the text and convert it to a PO file, do the translation, and put the text back in using the tools / SDK again.

## Tools / Prerequisites

This translation works for the latest version of Rogue Like: Evolution at the time it started, that is to say version **0.990m**. Also the Ren'Py SDK version used is the same than Oni uses for the game. **6.99.13**.

- [Ren'Py SDK 6.99.13](https://www.renpy.org/release/6.99.13)
- [Ren'Py Translator ToolKit 1.3](https://github.com/Beuc/renpy-ttk)
- A PO editor [POEdit](https://poedit.net/download)

## Changes in the game code

- Unfortunately, due to Oni's coding habits, variables of translatable text are used in the Ren'Py files. So we need to add "__()" around the text we want to translate, so Ren'Py SDK can export them properly. It's done using a python script. 

- Since Rogue's name in french is different, and her name variable is used to call her pictures, we need to change her picture names as well.

- screens.rpy: Added a language selection part, and modified the area around the clock to fit the french text.

Since the changes are already done, just download the repo's archive.rpa and replace it in your game copy folder.

## Working on a PO file

**Translation status : 30%**

Just open this repo's PO file and edit it using a text editor / PO editor.

For information, I already pre-translated the entries using [Deepl](https://www.deepl.com). So machine translation is already available, but I want an accurate, localized one. So rather than translating, checking is the major part of the work left!

## Some Python scripts

Some handy home-made Python 2.7 scripts were made to help beautify the translation, since some defects like blank useless lines or duplicates are possible.

- addTranslatableStrings.py: Will add "__()" around text defined in $line variable.
- removeBlankLines.py: Remove blank entries in PO file
- removeUselessStrings.py: Remove metadata entry added by POEdit
- unfuzzyDuplicates.py: If an entry is duplicated but has already been translated, it's useful to be able to unfuzzy all duplicates of same original text, and replace their translation with the first unfuzzy translation of original text it finds.

These scripts can be upgraded eventually, and are not perfect, so checking with a diff tool is required. (Like WinMerge)

## Import and test translation

- Have the original game in version 0.990m
- Replace archive.rpa by the repo's if not done already
- Generate translations for "french" OR add this repo's "french" folder in /game/tl
- Open renpy-ttk in Ren'Py SDK and import your MO file. (Compiled PO file) with mo2tl
- Launch game normally

---

Bienvenue dans mon patch de traduction pour Rogue Like: Evolution par [Oni](https://www.patreon.com/OniArtist/) en français !

## En bref

L'idée originale est de générer les traductions avec le SDK de Ren'Py pour la langue "french", en utilisant des outils pour extraire le texte traduisible et le convertir en fichier PO (gettext), faire la traduction, et remettre le texte traduit avec les outils / le SDK.

## Outils utilisés / Prérequis

Cette traduction marche pour la dernière version de Rogue Like: Evolution au moment du début de la traduction, à savoir *0.990m*. La version du SDK Ren'Py est aussi la même que celle qu'utilise Oni. (*6.99.13*)

- [Ren'Py SDK 6.99.13](https://www.renpy.org/release/6.99.13)
- [Ren'Py Translator ToolKit 1.3](https://github.com/Beuc/renpy-ttk)
- Un éditeur PO [POEdit](https://poedit.net/download)

## Modifications dans le code du jeu

- Malheureusement, les habitudes de codage d'Oni nous forcent à l'adapter pour la traduction. Le point le plus important est l'utilisation de variables avec du texte traduisible à l'intérieur. (Notamment $line) Il faut donc rajouter autour de ces textes "__()" pour que le SDK veuille l'extraire comme traduisible. Un script Python est déjà disponible pour faire le travail automatiquement.

- Vu que le nom de Malicia en anglais n'est pas le même, il faut aussi remplacer le nom de certaines images la concernant.

- screens.rpy: Il a été rajouté un cadre de sélection de langue, ainsi qu'une modification au niveau de la zone de l'horloge pour y faire tenir le texte français.

Les modifications ont déjà été faites, donc il n'y a qu'à remplacer le fichier archive.rpa du jeu par celui du dépôt.

## Travail dans le fichier PO

*Statut de la traduction : 30%*

Le fichier PO est mis à disposition dans le dépôt, il n'y qu'à le modifier avec un éditeur de texte / éditeur PO.

Pour information, une pré-traduction utilisant [Deepl](https://www.deepl.com) a déjà été faite, donc même si une traduction machine est disponible, nous souhaitons une traduction précise et bien localisée. Il y a donc plus de vérification de traduction à faire que de traduction à proprement parler !

## Quelques scripts Python

Des scripts Python 2.7 maison ont été faits pour optimiser / embellir la traduction, car quelques défauts comme des lignes inutiles / vides ou des doublons sont possibles.

- addTranslatableStrings.py: Ajoute "__()" autour des chaînes de texte de la variable $line pour les rendre traduisibles.
- removeBlankLines.py: Enlève les entrées vides d'un fichier PO
- removeUselessStrings.py: Enlève l'entrée de métadonnées rajoutée par POEdit
- unfuzzyDuplicates.py: Si une entrée est dupliquée et "fuzzy" (à vérifier) a déjà été traduite auparavant dans une entrée avec texte original identique, il est pratique de rendre toutes les autres entrées de texte original identique "unfuzzy" (traduction vérifiée) avec sa traduction remplacée par la première traduction vérifiée qu'il trouve pour cette même entrée de texte original identique.

Ces scripts peuvent être améliorés, et ne sont jamais parfaits, donc il est prudent de toujours vérifier la différence avec les fichiers sortants des scripts. (On peut utiliser WinMerge)

## Importer et tester la traduction

- Avoir une version du jeu Rogue Like: Evolution 0.990m
- Remplacer archive.rpa par celui du dépôt si ce n'est pas déjà fait
- Générer les traductions pour "french" ou bien coller le dossier "french" du dépôt dans /game/tl
- Ouvrir renpy-ttk avec le SDK Ren'Py et importer le fichier MO (Fichier PO compilé) avec mo2tl
- Lancer le jeu normalement

## Liens utiles - Useful links

- [Oni's Patreon](https://www.patreon.com/OniArtist/)
- [Ren'Py SDK 6.99.13](https://www.renpy.org/release/6.99.13)
- [Ren'Py Translator ToolKit 1.3](https://github.com/Beuc/renpy-ttk)
- [POEdit](https://poedit.net/download)
- [Unofficial Rogue Like Discord](https://discord.gg/b2jS82)
