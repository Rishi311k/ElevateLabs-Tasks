import json
import os

FILENAME = "tasks.json"
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title == "":
        print("Task cannot be empty!")
        return
    task = {"title": title, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")


def view_tasks(tasks, filter_type="all"):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        if filter_type == "completed" and not task["completed"]:
            continue
        if filter_type == "pending" and task["completed"]:
            continue

        status = "✔" if task["completed"] else "✘"
        print(f"{i}. [{status}] {task['title']}")


def mark_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print("🎉 Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"🗑 Removed task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. View All Tasks")
        print("2. View Completed Tasks")
        print("3. View Pending Tasks")
        print("4. Add Task")
        print("5. Mark Task as Completed")
        print("6. Remove Task")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks, "all")
        elif choice == "2":
            view_tasks(tasks, "completed")
        elif choice == "3":
            view_tasks(tasks, "pending")
        elif choice == "4":
            add_task(tasks)
        elif choice == "5":
            mark_completed(tasks)
        elif choice == "6":
            remove_task(tasks)
        elif choice == "7":
            print("Saving and exiting... Goodbye! 👋")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
