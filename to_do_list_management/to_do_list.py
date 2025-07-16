#load exisiting items 
# 1. create a new item
# 2. list items
# 3. mark item as complete
# 4. save items


import json

filename = "to_do_list.json"

def create_task(tasks):
    description = input("Enter description of the task").strip()

    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_task(tasks)
        print("saved the tasks")
    else:
        print("description cannot be empty")


def load_task():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except:
        return {"tasks":[]}
    

def view_task(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == '0':
        print("no tasks to display")
    else:
        print("To do list:\n")
        for i, task in enumerate(task_list):
            status = "[completed]" if task["complete"] else "[not completed]"
            print(f"{i+1}.{task['description']} | {status}\n")
            

def save_task(tasks):
    try:
        with open(filename, "w") as file:
            return json.dump(tasks,file)
    except:
        print("failed to save")

def mark_task_complete(tasks):
    view_task(tasks)
    try:
        task_number = int(input("Enter the number you want to complete : "))
        if 1 <= task_number <= len(tasks):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_task(tasks)
            print("tasks marked complete")
        else:
            print("invalid number")
    except:
        print("Enter valid number")


def main():
    # save_task({"tasks": ["save_tasks"]})
    tasks = load_task()
    # print(tasks)

    while True:
        print("To Do List \n")
        print("1. View Task")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter a choice for the to-do list").strip()

        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("you exit the program")
            break
        else:
            print("Invalid")


main()
        
