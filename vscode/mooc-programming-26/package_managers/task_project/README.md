Exercise using uv to understand package managers
Exercise: Task Statistics Package (using uv)
Requirements
Create a new project using uv.
Create a virtual environment.
Install the rich package.
Create a file called task_stats.py.
Display a table of tasks using rich.
Save your dependencies (handled automatically by uv).
Delete the virtual environment.
Recreate it from the project files.
Expected Project Structure
task_project/
│
├── task_stats.py
├── pyproject.toml
├── uv.lock
└── .venv/
Program Requirements

Use this data:

tasks = [
    ("Study Python", 3),
    ("Gym", 1),
    ("Read a book", 2),
    ("Watch course", 4),
]

Display something similar to:

┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Task             ┃ Hours ┃
┣━━━━━━━━━━━━━━━━━━╋━━━━━━━┫
┃ Study Python     ┃ 3     ┃
┃ Gym              ┃ 1     ┃
┃ Read a book      ┃ 2     ┃
┃ Watch course     ┃ 4     ┃
┗━━━━━━━━━━━━━━━━━━┻━━━━━━━┛

Total hours: 10
Average hours: 2.5
Tasks You Must Complete

Without copying commands from a tutorial:

Create a project with uv.
Create a virtual environment.
Install the rich package.
Discover how to import and use rich.
Observe how pyproject.toml and uv.lock are updated.
Delete .venv.
Recreate the environment using only the project files.
Verify the program still runs.
Bonus Challenges
Easy

Add another column:

Completed

using True or False.

Medium

Display completed tasks in green and incomplete tasks in red.

Hard

Create a function:

def show_tasks(tasks):
    ...

that receives the task list and prints the table.

Expert

Allow the user to enter tasks until they type:

quit

Then display the formatted table.

What You'll Practice
Creating a project with uv
Creating and using virtual environments
Adding dependencies with uv
Understanding pyproject.toml
Understanding uv.lock
Recreating an environment from lock files
Running Python programs inside a managed environment
Organizing a modern Python project
Extra Challenge (Recommended)

After finishing with rich, install another package (for example, requests) 
and modify your program to fetch a random quote or joke from a public API and 
display it below the task table. This will prepare you for the API section of your roadmap while reinforcing package management with uv.
