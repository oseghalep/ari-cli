import subprocess
import getpass
from ari_cli.config import get_alias

def run_alias(name):
    alias = get_alias(name)
    if not alias:
        print(f"Alias '{name}' not found.")
        return

    cmd = alias["command"]

    if alias.get("requires_password"):
        password = getpass.getpass("Enter password: ")
        print("Password entered.")

    if alias.get("requires_passphrase"):
        passphrase = getpass.getpass("Enter SSH key passphrase: ")
        print("Passphrase entered.")

    subprocess.run(cmd, shell=True)