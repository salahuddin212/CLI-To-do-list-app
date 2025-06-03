"""
Welcome to my modest CLI To-do list :)

Features:
- Add tasks
- View tasks
- Mark tasks as done
- Delete tasks

Author: Salahuddin (Me) 
"""


from datetime import datetime  # Used to parse and format dates

# Store all tasks in a list
tasks = []

def show_menu():
    """Displays the main menu."""
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    """Adds a new task with an optional due date."""
    title = input("Enter task title: ")
    due_input = input("Enter due date (YYYY-MM-DD) or leave blank: ")
    try:
        # Convert input string to a date object
        due_date = datetime.strptime(due_input, "%Y-%m-%d").date() if due_input else None
    except ValueError:
        print("Invalid date format. Task will have no due date.")
        due_date = None

    # Create the task dictionary and add it to the list
    task = {"title": title, "done": False, "due": due_date}
    tasks.append(task)
    print(f"Task '{title}' added with due date: {due_date if due_date else 'None'}.")

def view_tasks():
    """Displays all tasks with their status and due dates."""
    if not tasks:
        print("No tasks added yet.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        due = task["due"].strftime("%Y-%m-%d") if task["due"] else "No due date"
        print(f"{i}. [{status}] {task['title']} (Due: {due})")

def mark_done():
    """Marks a selected task as done."""
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"Task '{tasks[index]['title']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    """Deletes a selected task."""
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop that runs the CLI app
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
