#
"""
Welcome to my modest CLI To-do list :)

Features:
- Add tasks
- View tasks
- Mark tasks as done
- Delete tasks

Author: Salahuddin (Me) 
"""

tasks = [] # List of tasks(they're going to be a dictionary for each task)

def show_menu(): # Function for the main menu
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task(): # Function for adding tasks
    title = input("Enter task title: ")
    task = {"title": title, "done": False}
    tasks.append(task) # add task dictionary into the "tasks" list
    print(f"Task '{title}' added.")

def view_tasks(): # Function for viewing tasks
    if not tasks:
        print("No tasks added yet.") # If the tass list is empty, print this.
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1): # a for loop that goes through in the list "tasks"(which is now indexed starting from 1, thanks to enumertate() function)
        status = "✅" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['title']}")

def mark_done():
    view_tasks()
    try: # to catch value errors.
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks): # the number enterd by user have to be non-negative and not exceed the number of tasks.
            tasks[index]["done"] = True 
            print(f"Task '{tasks[index]['title']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError: 
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1 # -1 is here because python index start from 0 not one.
        if 0 <= index < len(tasks): # check that user's input is valid
            removed = tasks.pop(index) 
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# The main while loop for the program
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
        break # exit the while loop
    else:
        print("Invalid choice. Please try again.") # if user inputs something else other than no. from 1-5
