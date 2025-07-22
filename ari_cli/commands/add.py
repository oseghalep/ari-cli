from ari_cli.config import add_alias as add_to_config

def add_alias(name, command, requires_password=False, requires_passphrase=False):
    add_to_config(name, command, requires_password, requires_passphrase)