"""Build the v0.1.0 release ZIP from an explicit allowlist using only the standard library."""
from pathlib import Path
import hashlib
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('cpo-product-strategist', 'data-visualization-bi', 'microgroup-context-intelligence')
FILES = ('README.md', 'README.en.md', 'SKILL-CARDS.md', 'PUBLICATION-NOTICE.md', 'ATTRIBUTION.md', 'LICENSE', 'THIRD-PARTY-NOTICES.txt', 'scripts/build_package.py')
DIRS = tuple('skills/' + name for name in SKILLS) + ('demos', 'examples')
# Reject recognizable credentials and machine-specific locations, not ordinary methodological terminology.
UNSAFE = re.compile(r'/(?:Users|home)/[^\s]+|/private/(?:tmp|var)/[^\s]+|[A-Z]:\\Users\\|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\b(?:sk-(?:proj-)?[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16})\b|(?:api_key|password|access_token)\s*[:=]\s*[\"\'][^\"\'\s]{8,}', re.I)


def collect():
    paths = [ROOT / name for name in FILES]
    for name in DIRS:
        directory = ROOT / name
        if directory.is_symlink() or not directory.is_dir():
            raise ValueError('Missing or symlinked directory: ' + name)
        paths.extend(directory.rglob('*'))
    result = {}
    for path in sorted(set(paths)):
        relative = path.relative_to(ROOT)
        if path.is_symlink() or any(part in ('..', '') for part in relative.parts):
            raise ValueError('Unsafe path: ' + str(relative))
        if path.is_dir():
            continue
        # Interpreter caches are generated locally and never part of a skill distribution.
        if '__pycache__' in relative.parts or path.suffix == '.pyc':
            continue
        if not path.is_file():
            raise ValueError('Missing or nonregular file: ' + str(relative))
        content = path.read_bytes()
        if UNSAFE.search(content.decode('utf-8')):
            raise ValueError('Credential or machine reference: ' + str(relative))
        result[relative.as_posix()] = content
    for name in SKILLS:
        assert 'skills/' + name + '/SKILL.md' in result
    # Delivered Markdown must resolve without private repository documentation.
    for name, content in result.items():
        if not name.endswith('.md'):
            continue
        for link in re.findall(r'\]\(([^)]+)\)', content.decode()):
            if '://' in link or link.startswith('#'):
                continue
            target = (ROOT / name).parent / link.split('#')[0]
            resolved = target.resolve().relative_to(ROOT).as_posix()
            if resolved not in result and not any(item.startswith(resolved.rstrip('/') + '/') for item in result):
                raise ValueError('Broken package link: ' + name + ': ' + link)
    return result


def main():
    files = collect()
    manifest = ''.join(hashlib.sha256(data).hexdigest() + '  ' + name + '\n' for name, data in files.items()).encode()
    output = ROOT / 'dist/product-decision-skills-v0.1.0.zip'
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, data in {**files, 'SHA256SUMS': manifest}.items():
            info = zipfile.ZipInfo(name, (2026, 10, 13, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    print(str(output.relative_to(ROOT)))
    print(hashlib.sha256(output.read_bytes()).hexdigest())


if __name__ == '__main__':
    main()
