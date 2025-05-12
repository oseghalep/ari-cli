import subprocess
from ari_cli.config import get_alias

def check_status(name):
    command = get_alias(name)
    if not command:
        print(f"Alias '{name}' not found.")
        return
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        if result.returncode == 0:
            print(f"[✔] Connection successful for '{name}'.")
        else:
            print(f"[✖] Connection failed for '{name}': {result.stderr.decode().strip()}")
    except Exception as e:
        print(f"[!] Error checking alias '{name}': {str(e)}")