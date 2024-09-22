import csv

def add_task():
    new_task = input("Enter your new task: ")
    with open("todo.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["*", new_task])
    print("Task added successfully!")

def delete_task():
    if not tasks:
        print("There are no tasks in the list!")
        return

    task_number = int(input("Enter the number of the task to delete: ")) - 1

    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        with open("todo.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

def mark_task():
    if not tasks:
        print("There are no tasks in the list!")
        return

    task_number = int(input("Enter the number of the task to mark: ")) - 1

    if 0 <= task_number < len(tasks):
        current_status, task_description = tasks[task_number]
        new_status = "*" if current_status == "-" else "-"
        tasks[task_number] = (new_status, task_description)
        with open("todo.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
        print(f"Task status marked as {new_status}")
    else:
        print("Invalid task number!")

def read_tasks():
    tasks = []
    try:
        with open("todo.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    tasks.append(row)
    except FileNotFoundError:
        print("The 'todo.csv' file doesn't exist. A new one will be created.")
    return tasks

def show_tasks():
    if not tasks:
        print("There are no tasks in the list!")
        return

    for i, (status, task) in enumerate(tasks, start=1):
        print(f"{i}. [{status}] {task}")

tasks = read_tasks()

while True:
    print("\n1. ADD a task")
    print("2. DELETE a task")
    print("3. MARK task (completed/incomplete)")
    print("4. SHOW the TODO List")
    print("5. EXIT")

    try:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            add_task()
        elif choice == 2:
            delete_task()
        elif choice == 3:
            mark_task()
        elif choice == 4:
            show_tasks()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Have a productive day!")