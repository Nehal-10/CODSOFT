
"""
TO-DO LIST
"""

tasks = []


def add_task(tasks,task):
    tasks.append({"task": task,"compl":False})

def view_tasks(tasks):
    if not tasks:
        print("Your to do list is empty.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task["compl"] else "Pending"
            print(f"{i}. {task['task']} - {status}")
            
            
def mark_completed(tasks,task_number):
    try:
        task = tasks[task_number - 1]
        task["compl"] = True
        print(f"Task '{task['task']}' marked as completed.")
    except IndexError:
        print("Invalid task number.")

def delete_task(tasks, task_number):
    try:
        task = tasks.pop(task_number - 1)
        print(f"Task '{task['task']}' deleted.")
    except IndexError:
        print("Invalid task number.")
    
while True:
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(tasks, task)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        task_number = int(input("Enter task number to mark as completed: "))
        mark_completed(tasks, task_number)
    elif choice == "4":
        task_number = int(input("Enter task number to delete: "))
        delete_task(tasks, task_number)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")