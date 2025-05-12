import json
from ari_cli.config import add_alias

def import_aliases(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        for name, command in data.items():
            add_alias(name, command)