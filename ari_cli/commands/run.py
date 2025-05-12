import subprocess
from ari_cli.config import get_alias

def run_alias(name):
    command = get_alias(name)
    if command:
        subprocess.run(command, shell=True)
    else:
        print(f"Alias '{name}' not found.")