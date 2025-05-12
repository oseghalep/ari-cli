import json
from ari_cli.config import list_aliases

def export_aliases(file_path):
    with open(file_path, 'w') as f:
        json.dump(list_aliases(), f, indent=2)