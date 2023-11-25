Task_list = []

def add_task(task):
    Task_list.append(task)
    print("Task Added Sucessfully")

def show_task():
    if len(Task_list)==0:
        print("No tasks available in the list")
    else:
        print("Tasks:")
        for i in Task_list:
            print("-",i)
def del_task(task):
    if task in Task_list:
        Task_list.remove(task)
        print("Task deleted successfully")
    else:
        print("No Task found")

while True:
    print("\nMenu")
    print("1- Add Task")
    print("2- View task")
    print("3- delete task")
    print("4- exit")

    choice = input("Enter your option: ")

    if choice == "1":
        task = input("Enter a task: ")
        add_task(task)
    elif choice == "2":
        show_task()
    elif choice == "3":
        task = input("Enter a task: ")
        del_task(task)
    elif choice == "4":
        break
    else:
        print("Invalid inout, enter your choice")

