from ari_cli.config import get_alias, add_alias, delete_alias

def rename_alias(old_name, new_name):
    command = get_alias(old_name)
    if command:
        add_alias(new_name, command)
        delete_alias(old_name)
    else:
        print(f"Alias '{old_name}' not found.")