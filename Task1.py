class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return f"{self.title} - {self.description} - Due: {self.due_date} - Priority: {self.priority}"

task_list = []

def add_task(title, description, due_date, priority):
    new_task = Task(title, description, due_date, priority)
    task_list.append(new_task)

def view_tasks():
    if not task_list:
        print("No tasks available.\n")
    for i, task in enumerate(task_list, start=1):
        print(f"{i}. {task}")
    print()

def update_task(index, title=None, description=None, due_date=None, priority=None):
    if 0 <= index < len(task_list):
        task = task_list[index]
        if title:
            task.title = title
        if description:
            task.description = description
        if due_date:
            task.due_date = due_date
        if priority:
            task.priority = priority
        print("Task updated successfully.\n")
    else:
        print("Invalid task number.\n")

def delete_task(index):
    if 0 <= index < len(task_list):
        task_list.pop(index)
        print("Task deleted successfully.\n")
    else:
        print("Invalid task number.\n")

def menu():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date: ")
            priority = input("Priority: ")
            add_task(title, description, due_date, priority)

        elif choice == '2':
            view_tasks()

        elif choice == '3':
            view_tasks()
            index = int(input("Enter task number to update: ")) - 1
            title = input("New Title (leave blank to keep): ")
            description = input("New Description (leave blank to keep): ")
            due_date = input("New Due Date (leave blank to keep): ")
            priority = input("New Priority (leave blank to keep): ")
            update_task(index,
                        title if title else None,
                        description if description else None,
                        due_date if due_date else None,
                        priority if priority else None)

        elif choice == '4':
            view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
