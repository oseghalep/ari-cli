import sys
import click

@click.group()
def main():
    pass

@main.command()
@click.argument('name')
@click.argument('command')
def add(name, command):
    """Add a new alias."""
    from ari_cli.commands.add import add_alias
    add_alias(name, command)
    click.echo(f"Alias '{name}' added.")

@main.command()
def list():
    """List all aliases."""
    from ari_cli.commands.list import list_items
    for name, command in list_items().items():
        click.echo(f"{name} => {command}")

@main.command()
@click.argument('name')
def delete(name):
    """Delete an alias."""
    from ari_cli.commands.delete import delete_item
    delete_item(name)
    click.echo(f"Alias '{name}' deleted.")

@main.command()
@click.argument('name')
def get(name):
    """Show the command behind a specific alias."""
    from ari_cli.commands.get import get_command
    command = get_command(name)
    click.echo(command if command else "Alias not found.")

@main.command()
@click.argument('name')
def run(name):
    """Run the command linked to a specific alias."""
    from ari_cli.commands.run import run_alias
    run_alias(name)

@main.command()
def clear():
    """Clear all saved aliases."""
    from ari_cli.commands.clear import clear_aliases
    clear_aliases()
    click.echo("All aliases cleared.")

@main.command()
@click.argument('file_path')
def export(file_path):
    """Export all aliases to a JSON file."""
    from ari_cli.commands.export_aliases import export_aliases
    export_aliases(file_path)
    click.echo(f"Aliases exported to {file_path}")

@main.command(name='import')
@click.argument('file_path')
def import_aliases(file_path):
    """Import aliases from a JSON file."""
    from ari_cli.commands.import_aliases import import_aliases
    import_aliases(file_path)
    click.echo(f"Aliases imported from {file_path}")

@main.command()
@click.argument('name')
def status(name):
    """Check if an alias can connect (basic SSH check)."""
    from ari_cli.commands.status import check_status
    check_status(name)

@main.command()
@click.argument('name')
def remove(name):
    """Remove a saved alias."""
    from ari_cli.commands.remove import remove_alias
    remove_alias(name)
    click.echo(f"Alias '{name}' removed.")

@main.command()
@click.argument('name')
def show(name):
    """Display the command linked to an alias."""
    from ari_cli.commands.show import show_alias
    command = show_alias(name)
    click.echo(command if command else "Alias not found.")

@main.command()
@click.argument('name')
@click.argument('new_command')
def update(name, new_command):
    """Update an alias with a new command."""
    from ari_cli.commands.update import update_alias
    update_alias(name, new_command)
    click.echo(f"Alias '{name}' updated.")

@main.command()
@click.argument('old_name')
@click.argument('new_name')
def rename(old_name, new_name):
    """Rename an alias."""
    from ari_cli.commands.rename import rename_alias
    rename_alias(old_name, new_name)
    click.echo(f"Alias renamed from '{old_name}' to '{new_name}'.")

@main.command()
@click.argument('file_path')
def backup(file_path):
    """Backup all aliases to a file."""
    from ari_cli.commands.backup import backup_aliases
    backup_aliases(file_path)
    click.echo(f"Aliases backed up to '{file_path}'")

if __name__ == "__main__":
    main()