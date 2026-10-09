#!/usr/bin/env python3
"""Validate, package or install this content-only skill. Python standard library only."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = 'human-copywriter'
SKILL = ROOT / 'skills' / NAME


def inventory(source=SKILL):
    """Reject symlinks; inventory only the explicitly selected skill folder."""
    if source.is_symlink() or not source.is_dir():
        raise ValueError('Skill source must be a real directory')
    entries = {}
    for path in sorted(source.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symlink is not packageable: {path}')
        if path.is_file():
            entries[path.relative_to(source).as_posix()] = path.read_bytes()
    return entries


def check(source=SKILL):
    entries = inventory(source)
    for required in ('SKILL.md', 'LICENSE'):
        if required not in entries:
            raise ValueError(f'Missing {required}')
    text = entries['SKILL.md'].decode('utf-8')
    match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not match or f'name: {NAME}\n' not in match.group(1) + '\n':
        raise ValueError('Invalid name/frontmatter')
    description = re.search(r'^description: (.+)$', match.group(1), re.M)
    if not description or len(description.group(1)) > 200:
        raise ValueError('Expected a single-line discovery description <=200 characters')
    for relative, data in entries.items():
        if not relative.endswith('.md'):
            continue
        for target in re.findall(r'\]\(([^\s)]+)\)', data.decode('utf-8')):
            if '://' in target or target.startswith('#'):
                continue
            destination = (source / relative).parent / target.split('#', 1)[0]
            if not destination.resolve().is_relative_to(source.resolve()):
                raise ValueError(f'Link leaves skill: {relative}: {target}')
            if not destination.is_file():
                raise ValueError(f'Missing resource: {relative}: {target}')
    return entries


def manifest(entries):
    return {path: {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
            for path, data in entries.items()}


def package(destination, source=SKILL):
    entries = check(source)
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    archive = destination / f'{NAME}.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as bundle:
        for relative, data in entries.items():
            info = zipfile.ZipInfo(f'{NAME}/{relative}', date_time=(2026, 10, 9, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, data)
    record = {'name': NAME, 'files': manifest(entries),
              'zip_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}
    (destination / f'{NAME}-manifest.json').write_text(json.dumps(record, indent=2) + '\n')
    return archive


def install(parent, source=SKILL):
    entries = check(source)
    parent = Path(parent).expanduser()
    target = parent / NAME
    if target.is_symlink():
        raise ValueError(f'Refusing to overwrite a symlink: {target}')
    if target.exists():
        if inventory(target) == entries:
            return target, 'already identical'
        raise ValueError(f'Existing skill differs; inspect it before updating: {target}')
    parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=f'.{NAME}-', dir=parent))
    try:
        for relative, data in entries.items():
            path = stage / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        stage.rename(target)
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    if inventory(target) != entries:
        raise ValueError('Installed files did not match source')
    return target, 'installed and verified'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('check')
    pack = commands.add_parser('package')
    pack.add_argument('--dest', type=Path, default=ROOT / 'dist')
    local = commands.add_parser('install')
    local.add_argument('--client', choices=('codex', 'claude'), required=True)
    local.add_argument('--dest', type=Path, help='Skills parent directory')
    args = parser.parse_args()
    try:
        if args.command == 'check':
            print(f'Valid package: {len(check())} files')
        elif args.command == 'package':
            print(package(args.dest))
        else:
            parent = args.dest
            if parent is None:
                parent = (Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills'
                          if args.client == 'codex' else Path.home() / '.claude' / 'skills')
            path, status = install(parent)
            print(f'{status}: {path}')
    except (ValueError, OSError) as error:
        parser.exit(1, f'Error: {error}\n')


if __name__ == '__main__':
    main()
