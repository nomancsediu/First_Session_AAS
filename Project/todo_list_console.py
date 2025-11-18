task = [] #Empty List
completed = []

'''
[
[task_name,priority,category],
[task_name,priority,category],
[task_name,priority,category]
]



[task_name,priority,category]
'''
def menu():
    print("--- To-Do List ---")
    print("1. Add Task")
    print("2. View tasks")
    print("3. Complete Task")
    print("4. View Completed")
    print("5. Remove Task")
    print("6. Clear All")
    print("7. Exit")

def sort_list():
    sorted_list = []
    '''
[
    ["Learn Python", "High", "Programming"],
    ["Submit Assignment", "High", "School"],
    ["Read Book", "Medium", "Leisure"],
    ["Clean Room", "Low", "Chores"]
]
    
    '''

    for each_list in task:
        if each_list[1] == 'High':
            sorted_list.append(each_list)

    for each_list in task:
        if each_list[1] == 'Medium':
            sorted_list.append(each_list)

    for each_list in task:
        if each_list[1] == 'Low':
            sorted_list.append(each_list)
    return sorted_list


while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == '1':
        task_name = input("Enter your task: ")
        priority = input("Enter your priority: ")
        category = input("Enter your category: ")

        task_item = [task_name,priority,category]

        task.append(task_item)
        print("Task added successfully!")

    elif choice == '2':

        if len(task) == 0:
            print("No task available.")
        else:
            sorted_list = sort_list()

            #1. Learn Python [High] (Programming)
            #2. Learn Python [High] (Programming)
            #3. Learn Python [High] (Programming)
            

            # ["Learn Python", "High", "Programming"]
            i = 1
            for each in sorted_list:
                print(f"{i}. {each[0]} [{each[1]}] ({each[2]})")
                i = i+1

    elif choice == '3':
        if len(task) == 0:
            print("No task available.")
        else:
            sorted_list = sort_list()

            #1. Learn Python [High] (Programming)
            #2. Learn Python [High] (Programming)
            #3. Learn Python [High] (Programming)


            # ["Learn Python", "High", "Programming"]
            i = 1
            for each in sorted_list:
                print(f"{i}. {each[0]} [{each[1]}] ({each[2]})")
                i = i+1
            

            num = int(input("Enter your number: "))
            
            done = num-1

            item = sorted_list[done]

            completed.append(item)
            task.remove(item)
    
    elif choice == '4':
        if len(completed)==0:
            print("No task available.")
        else:
            i = 1
            for each_li in completed:
                print(f"{i}. {each_li[0]} [{each_li[1]}] ({each_li[2]})")
                i = i+1
    elif choice =='5':
        if len(task) == 0:
            print("No task available.")
        else:
            sorted_list = sort_list()

            #1. Learn Python [High] (Programming)
            #2. Learn Python [High] (Programming)
            #3. Learn Python [High] (Programming)


            # ["Learn Python", "High", "Programming"]
            i = 1
            for each in sorted_list:
                print(f"{i}. {each[0]} [{each[1]}] ({each[2]})")
                i = i+1
            

            n = int(input("Enter your number: "))
            
            rmv = n-1

            item_2 = sorted_list[rmv]

            task.remove(item_2)

            print("Task removed successfully!")
    elif choice == '6':
        task.clear()
        print("Tasks Cleared Successfully!")

    elif choice =='7':
        print("Goodbye!")
        break
    else:
        print("Invalid Choice.")
