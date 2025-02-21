class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

if __name__ == "__main__":
    app = ToDoApp()
    while True:
        print("\n1. Add Task\n2. Show Tasks\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter the task: ")
            app.add_task(task)
        elif choice == '2':
            app.show_tasks()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")