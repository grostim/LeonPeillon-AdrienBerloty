#!/usr/bin/env python3
"""Construit LaTeX, PDF et EPUB à partir du texte relu en Markdown."""
from pathlib import Path
import argparse
import csv
import hashlib
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
STEM = 'Leon_Peillon_Adrien_Berloty'

def run(*args):
    subprocess.run(args, cwd=ROOT, check=True)

def verify_sources():
    with (ROOT / 'Originaux' / 'manifest.csv').open(newline='') as source:
        rows = list(csv.DictReader(source))
    if len(rows) != 32 or [int(row['page']) for row in rows] != list(range(32)):
        raise SystemExit('Le manifest doit contenir la couverture et les 31 pages, dans cet ordre.')
    for row in rows:
        original = ROOT / 'Originaux' / row['original_conserve']
        if hashlib.sha256(original.read_bytes()).hexdigest() != row['sha256']:
            raise SystemExit(f'Original modifié : {original}')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-only', action='store_true')
    args = parser.parse_args()
    verify_sources()
    run('pandoc', 'transcription.md', '--from=markdown', '--to=latex', '--standalone',
        '--top-level-division=chapter', '--template=scripts/template.tex',
        '--lua-filter=scripts/pages.lua', '--wrap=none', '--output=Adrien Berloty.tex')
    if args.source_only:
        return
    out = ROOT / 'output'
    (out / 'pdf').mkdir(parents=True, exist_ok=True)
    scratch = ROOT / 'tmp' / 'latex'
    scratch.mkdir(parents=True, exist_ok=True)
    for _ in range(2):
        run('pdflatex', '-interaction=nonstopmode', '-halt-on-error',
            f'-output-directory={scratch}', 'Adrien Berloty.tex')
    shutil.copyfile(scratch / 'Adrien Berloty.pdf', out / 'pdf' / f'{STEM}.pdf')
    run('pandoc', 'transcription.md', '--to=epub3', '--toc', '--split-level=1',
        f'--output=output/{STEM}.epub')
    shutil.copyfile(ROOT / 'transcription.md', out / f'{STEM}.md')

if __name__ == '__main__':
    main()
