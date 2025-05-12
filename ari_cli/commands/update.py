from ari_cli.config import add_alias, get_alias

def update_alias(name, new_command):
    if not get_alias(name):
        print(f"Alias '{name}' does not exist.")
        return
    add_alias(name, new_command)