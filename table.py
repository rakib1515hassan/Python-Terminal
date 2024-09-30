from rich.table import Table
from rich.console import Console

console = Console()

table = Table(title="User Data")

data = {
    0: {"id": 1, "name": "Rakib", "age": 28},
    1: {"id": 2, "name": "Hassan", "age": 24},
    2: {"id": 3, "name": "Tuhin", "age": 25},
    3: {"id": 4, "name": "Rubel", "age": 22},
    4: {"id": 5, "name": "Joshim", "age": 29},
}

table.add_column("ID", justify="right", style="cyan", no_wrap=True)
table.add_column("Name", style="magenta")
table.add_column("Age", justify="right", style="green")

for v in data.values():
    table.add_row(str(v["id"]), v["name"], str(v["age"]))

console.print(table)
