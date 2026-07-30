from rich.table import Table
from rich.console import Console
import requests

def show_tasks(tasks: list):

    table = Table()
    console = Console()

    table.add_column("Task")
    table.add_column("Hours")
    table.add_column("Completed")

    for task, hours, complete in tasks:
        if complete:
            table.add_row(task, str(hours), "[green]:heavy_check_mark:")
        else:
            table.add_row(task, str(hours), "[red]:cross_mark:")

    console.print(table)

def add_tasks(tasks: list):
    while True:
        task = input("task: ")
        if task == "quit":
            break
        hours = int(input("hours: "))
        completed = input("completed? (y/n)")
        if completed == "y":
            completed = True
        else:
            completed = False

        tasks.append((task, hours, completed))

def quote():
    text = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = text.json()
    print(f"{data['setup']}\n{data['punchline']}")

tasks = [
    ("Study Python", 3, True),
    ("Gym", 1, False),
    ("Read a book", 2, True),
    ("Watch course", 4, True),
]

add_tasks(tasks)
show_tasks(tasks)
quote()




