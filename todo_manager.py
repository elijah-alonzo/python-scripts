import sys
import os
TODO_FILE = "todo.txt"

def show_tasks():
    if not os.path.exists(TODO_FILE):
        print("No tasks yet.")
        return
    with open(TODO_FILE, "r") as f:
        tasks = f.readlines()
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")

def add_task(task):
    with open(TODO_FILE, "a") as f:
        f.write(task + "\n")
    print("Task added.")

def remove_task(index):
    if not os.path.exists(TODO_FILE):
        print("No tasks to remove.")
        return
    with open(TODO_FILE, "r") as f:
        tasks = f.readlines()
    try:
        removed = tasks.pop(index - 1)
        with open(TODO_FILE, "w") as f:
            f.writelines(tasks)
        print(f"Removed: {removed.strip()}")
    except IndexError:
        print("Invalid task number.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python todo_manager.py [add <task> | show | remove <number>]")
    elif sys.argv[1] == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "show":
        show_tasks()
    elif sys.argv[1] == "remove" and len(sys.argv) > 2:
        remove_task(int(sys.argv[2]))
    else:
        print("Invalid command.")
