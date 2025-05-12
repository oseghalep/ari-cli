# ARI CLI - SSH Alias Manager

ARI CLI is a powerful and easy-to-use command-line tool for managing SSH aliases, named after my daugther Ariella. You can save, list, delete, and manage your SSH aliases with ease. With ARI CLI, you can quickly connect to remote systems without typing long SSH commands repeatedly.

---

## Features

* **Add an Alias**: Save SSH commands with aliases for quick access.
* **Delete an Alias**: Remove an alias when it's no longer needed.
* **List Aliases**: View all saved aliases and their corresponding commands.
* **Run Alias**: Execute a saved alias command directly.
* **Show Alias**: View the command behind a specific alias.
* **Export Aliases**: Export your saved aliases to a JSON file for backup or sharing.
* **Import Aliases**: Import aliases from a JSON file.
* **Clear Aliases**: Remove all saved aliases from the configuration.
* **Status**: Check if an alias can successfully connect via SSH (basic connectivity check).
* **Backup**: Create a backup of all aliases to a file.
* **get**: Show the command behind a specific alias.
* **remove**: Remove a saved alias.
* **rename**: Rename an alias.
* **update**: Update an alias with a new command.

---

## Installation

To install ARI CLI, you can use `pip`, Python's package manager. If you haven't already installed `pip`, please follow the instructions at [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/).

### Step 1: Install ARI CLI using pip

You can install the latest version of ARI CLI with the following command:

```bash
pip install ari-cli
```

Alternatively, you can install the project directly from GitHub:

```bash
pip install git+https://github.com/oseghalep/ari-cli.git
```

---

## Usage

After installing ARI CLI, you can run the tool with the following command:

```bash
ari --help
```

This will display the help message, showing all available commands and options.

### Global Options:

* `--help`: Show help information and usage.

---

## Commands

### 1. **add** - Add a new alias

Add a new SSH alias to your configuration.

```bash
ari add <alias_name> <ssh_command>
```

#### Example:

```bash
ari add myserver 'ssh -i ~/.ssh/id_rsa user@192.168.1.10'
```

---

### 2. **delete** - Delete an alias

Remove a specific alias from the configuration.

```bash
ari delete <alias_name>
```

#### Example:

```bash
ari delete myserver
```

---

### 3. **list** - List all aliases

Show a list of all saved aliases and their corresponding commands.

```bash
ari list
```

#### Example:

```bash
ari list
```

---

### 4. **get** - Show the command behind a specific alias

Display the SSH command linked to a specific alias.

```bash
ari get <alias_name>
```

#### Example:

```bash
ari get myserver
```

---

### 5. **run** - Execute the command linked to a specific alias

Run the SSH command linked to an alias directly.

```bash
ari run <alias_name>
```

#### Example:

```bash
ari run myserver
```

---

### 6. **clear** - Remove all saved aliases

Clear all saved aliases from the configuration.

```bash
ari clear
```

#### Example:

```bash
ari clear
```

---

### 7. **export** - Export all aliases to a JSON file

Export all saved aliases to a JSON file for backup or sharing.

```bash
ari export <file_path>
```

#### Example:

```bash
ari export ~/aliases_backup.json
```

---

### 8. **import** - Import aliases from a JSON file

Import saved aliases from a JSON file.

```bash
ari import <file_path>
```

#### Example:

```bash
ari import ~/aliases_backup.json
```

---

### 9. **status** - Check if an alias can SSH successfully

Check if an alias can connect successfully via SSH (basic connectivity check).

```bash
ari status <alias_name>
```

#### Example:

```bash
ari status myserver
```

---

### 10. **remove** - Remove a saved alias

Remove a specific alias from the configuration.

```bash
ari remove <alias_name>
```

#### Example:

```bash
ari remove myserver
```

---

### 11. **show** - Display the command linked to an alias

Show the SSH command behind an alias.

```bash
ari show <alias_name>
```

#### Example:

```bash
ari show myserver
```

---

### 12. **update** - Update an alias

Update an existing alias with a new SSH command.

```bash
ari update <alias_name> <new_command>
```

#### Example:

```bash
ari update myserver 'ssh newuser@192.168.1.20'
```

---

### 13. **rename** - Rename an alias

Rename a saved alias.

```bash
ari rename <old_name> <new_name>
```

#### Example:

```bash
ari rename myserver newserver
```

---

### 14. **backup** - Backup all aliases

Create a backup of all saved aliases to a file.

```bash
ari backup <file_path>
```

#### Example:

```bash
ari backup ~/aliases_backup.json
```

---

## Configuration

ARI CLI uses a JSON file to store aliases. By default, this file is located at `~/.ari_aliases.json`. You can manually edit the file if needed, but it's recommended to use the CLI commands for managing aliases.

---

## Contribution

We welcome contributions to ARI CLI! If you have an idea for a new feature or found a bug, please feel free to fork the repository, make changes, and create a pull request.

### How to contribute:

1. Fork the project.
2. Create a new branch.
3. Make your changes.
4. Test your changes.
5. Submit a pull request with a clear description of the changes.

---

## License

This project is licensed under the MIT License - see the [https://github.com/oseghalep/ari-cli/blob/main/LICENSE](https://github.com/oseghalep/ari-cli/blob/main/LICENSE) file for details.

---

## Contact

* **Author**: Oseghale Paul Okosun
* **GitHub**: [https://github.com/oseghalep](https://github.com/oseghalep)
* **Email**: [oseghalep@gmail.com](mailto:oseghalep@gmail.com)

---

Feel free to reach out if you have any questions, feature requests, or issues.

---