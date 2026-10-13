"""Create a local metadata copy for a target Salesforce username."""
from pathlib import Path
import argparse
import shutil

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--username', required=True, help='Existing target Salesforce username, not a password')
args = parser.parse_args()
if not args.username.strip() or any(c in args.username for c in '<>&\"\'\r\n'):
    parser.error('Provide a valid Salesforce username without XML control characters.')
root = Path(__file__).resolve().parents[1]
destination = root / '.deploy' / 'force-app'
shutil.copytree(root / 'force-app', destination, dirs_exist_ok=True)
changed = 0
for path in destination.rglob('*.xml'):
    content = path.read_text(encoding='utf-8')
    if 'REPLACE_WITH_SALESFORCE_USERNAME' in content:
        path.write_text(content.replace('REPLACE_WITH_SALESFORCE_USERNAME', args.username), encoding='utf-8')
        changed += 1
print(f'Prepared {destination}; configured {changed} metadata files. Source files remain unchanged.')
