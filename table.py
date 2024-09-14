from rich.table import Table

from rich.console import Console


console = Console()

table = Table(title="User Data")

table.add_column("ID", justify="right", style="cyan", no_wrap=True)
table.add_column("Name", style="magenta")
table.add_column("Age", justify="right", style="green")

table.add_row("1", "Alice", "28")
table.add_row("2", "Bob", "32")
table.add_row("3", "Charlie", "22")

console.print(table)