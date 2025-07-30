TASK_FILE="tasks.txt"
def show_task():
    try:
        with open(TASK_FILE,"r") as file:
            tasks=file.readlines()
            if not tasks:
                print("No tasks yet")
            else:
                print("\nYour tasks")
                for i,task in enumerate(tasks,1):
                    print(f"{i}.{task.strip()}")
    except FileNotFoundError:
        open(TASK_FILE,"w").close()
        print("Task File Created")

def add_task():
    task=input("Enter a task :- ")
    with open(TASK_FILE,"a") as file:
        file.write(task+"\n")
    print("Task added")

def delete_task():
    show_task()
    try:
        task_no=int(input("Enter task number to delete :- "))
        with open(TASK_FILE,"r") as file:
            tasks=file.readlines()
        if 1 <= task_no <= len(tasks):
            del tasks[task_no-1]
            with open(TASK_FILE,"w") as file:
                file.writelines(tasks)
            print("Task Deleted...")
        else:
            print("Invalid task number")
    except ValueError:
        print("Enter a valid number")

def main():
    while True:
        print("\n====TO DO LIST====")
        print("1. View Task")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice=int(input("Enter your choice :- "))
        if choice==1:
            show_task()
        elif choice==2:
            add_task()
        elif choice==3:
            delete_task()
        elif choice==4:
            print("Exiting....")
            break
        else:
            print("Enter a valid choice !")
if __name__=="__main__":
    main()