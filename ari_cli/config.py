import os
import json

CONFIG_PATH = os.path.expanduser("~/.ari_aliases.json")

def _load_aliases():
    if not os.path.exists(CONFIG_PATH):
        return {}
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def _save_aliases(aliases):
    with open(CONFIG_PATH, "w") as f:
        json.dump(aliases, f, indent=4)

def add_alias(name, command):
    aliases = _load_aliases()
    aliases[name] = command
    _save_aliases(aliases)

def get_alias(name):
    aliases = _load_aliases()
    return aliases.get(name)

def remove_alias(name):
    aliases = _load_aliases()
    if name in aliases:
        del aliases[name]
        _save_aliases(aliases)

def list_aliases():
    return _load_aliases()