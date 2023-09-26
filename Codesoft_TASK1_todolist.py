#TASK 1
#creating a to do list
from tkinter import *
todo_list = []
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")
def display_todo_list():
    print("\nTo-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
    print()
while True:
    print("Options:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display to-do list")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task you want to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task you want to remove: ")
        remove_task(task)
    elif choice == '3':
        display_todo_list()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")