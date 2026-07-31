from dataclasses import dataclass
from rich.table import Table
from rich.console import Console

@dataclass
class Task:
    title: str
    hours: int
    completed: bool   
    priority: int

def add_task(tasks: list, title: str, hours: int, priority: int):
    task = Task(title, hours, False, priority)
    tasks.append(task)

def complete_task(tasks: list, title: str):
    found = False
    for t in tasks:
        if t.title == title:
            found = True
            t.completed = True
    if not found:
        print("task not found.")

def total_hours(tasks: list):
    total = 0
    for t in tasks:
        total += t.hours

    return total


def completed_tasks(tasks: list):
    completed = []
    for t in tasks:
        if t.completed == True:
            completed.append(t)

    return completed

def remove_completed(tasks: list):
    #transforming the list
    tasks[:] = [t for t in tasks if not t.completed]

def highest_priority(tasks: list):
    high_p = 4
    high_h = -1
    for t in tasks:
        if t.priority <= high_p:
            if t.hours > high_h and t.priority != high_p:
                high_p = t.priority
                high_h = t.hours
                higher_task = t
    return higher_task

def sort_tasks(tasks: list):
        #using labda to sort
        return sorted(tasks, key=lambda t: (t.priority, -t.hours))

def show_tasks(old_tasks: list):
    tasks = sort_tasks(old_tasks)

    table = Table()
    console = Console()

    table.add_column("Task")
    table.add_column("Hours")
    table.add_column("Priority")
    table.add_column("Complete")

    for t in tasks:
        if t.priority == 1:
            priority = "High"
        elif t.priority == 2:
            priority = "Medium"
        else:
            priority = "low"

        if t.completed:
            table.add_row(t.title, str(t.hours), priority, "[green]:heavy_check_mark:")
        else:
            table.add_row(t.title, str(t.hours), priority, "[red]:cross_mark:")

    console.print(table)

def help():
    print("")
    print("commands: ")
    print("1. Add task")
    print("2. Complete task")
    print("3. Show tasks")
    print("4. Remove completed")
    print("5. Show completed")
    print("6. Show total hours")
    print("7. Exit")

def execute(tasks: list):
    while True:
        help()
        command = int(input("command: "))
        if command == 1:
            add_task(tasks, "Python", 3, 1)
            add_task(tasks, "gym", 1, 3)
            add_task(tasks, "SQL", 3, 2)

        elif command == 2:
            complete_task(tasks, "Python")

        elif command == 3:
            show_tasks(tasks)

        elif command == 4:
            remove_completed(tasks)

        elif command == 5:
            finished = completed_tasks(tasks)
            show_tasks(finished)

        elif command == 6:
            print(f"Total Hours: {total_hours(tasks)}")

        elif command == 7:
            break

        else:
            help()
    

tasks = []

execute(tasks)