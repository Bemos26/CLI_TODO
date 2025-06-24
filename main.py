# main.py

import json
from task import Task, greet

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return  []
            data = json.loads(content)
            return [Task.from_dict(item) for item in data]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append(Task(title))
        save_tasks(tasks)
        print("✅ Task added!\n")
    else:
        print("⚠️ Task title cannot be empty.\n")

def list_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.\n")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task.completed else "✗"
            print(f"{i}. [{status}] {task.title}")
        print()

def mark_complete(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index].completed = True
            save_tasks(tasks)
            print("✅ Task marked as complete!\n")
        else:
            print("❌ Invalid number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑️ Deleted task: {deleted.title}\n")
        else:
            print("❌ Invalid number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

def show_menu():
    print("What do you want to do?")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

def main():
    user_name = input("Enter your name: ")
    print(greet(user_name))
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print(f"👋 Goodbye, {user_name}!\n")
            break
        else:
            print("❌ Invalid option. Please choose 1-5.\n")

if __name__ == "__main__":
    main()