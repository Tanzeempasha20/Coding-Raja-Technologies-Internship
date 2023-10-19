import json
import os
from datetime import datetime
TASKS_FILE = "tasks.json"
tasks = []

if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "r") as file:
        tasks = json.load(file)

def display_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task['completed'] else " "
            print(f"{i}. [{status}] {task['title']} (Priority: {task['priority']}, Due Date: {task['due_date']})")


def add_task():
    title = input("Enter task title: ")
    priority = input("Enter task priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")


def remove_task():
    display_tasks()
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks()
        print(f"Removed task: {removed_task['title']}")
    else:
        print("Invalid task number.")


def mark_completed():
    display_tasks()
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks()
        print("Task marked as completed.")
    else:
        print("Invalid task number.")


def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)
while True:
    print("\nTo-Do List Application")
    print("1. Display tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Mark a task as completed")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_completed()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")
