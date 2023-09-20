import json
from datetime import datetime

def add(plan_list, day:str, start_time, end_time, plan:str):
    plan_list[day].append([start_time, end_time, plan])
    schedule = plan_list
    return schedule

def show(plan_list,day:str):
    schedule_plan_day = plan_list[day]
    if not schedule_plan_day:
        print(f'You have no plans for {day}.')
    else:
        print(f'Your plans for {day} are:')
        for start_time, end_time, plan in schedule_plan_day:
            print(f'start_time: {start_time} - end_tine: {end_time} - plan: {plan}')
    return schedule_plan_day

def save(schedule_list:list,filename:str):
    with open(filename, "w") as outfile:
        json.dump(schedule_list, outfile)
        exit_code = 0
    return exit_code

def load(filename:str):
    with open(filename) as json_file:
        schedule_list = json.load(json_file)
    return schedule_list

def correct_time(start_time, end_time):
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    delta = end - start 
    if int(delta.total_seconds()) < 0:
        result = False
    else:
        result = True
    return result

plan_dict = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': [],
    'Saturday': [],
    'Sunday': []
    }


print("This is a scheduled time where you can input your plans, and it will display them on a specific day")
print("Please note that the time format is %H:%M, such as 13:10.")


while True:
    option = input("Choose: load, add, show, save, exit: ")
    if option == "load":
        filename = input("Choose plan filename to upload: ")
        plan_dict=load(filename)
    elif option == "add":
        day = input("Which day do have a plan: ").capitalize()
        start_time = input("What time do you start: ")
        end_time = input("What time do you end: ")
        plan =  input("What is your plan: ")
        if correct_time(start_time, end_time):
            plan_dict = add(plan_dict, day, start_time, end_time, plan)
            print("Added successfully!")
        else:
            print(f"Error! {end_time} cannot be before {start_time}")
        
    elif option == "show":
        day = input("Which day do want to check: ").capitalize()
        show(plan_dict, day)
    elif option == "save":
        filename = input("Choose plan filename to save: ")
        save(plan_dict, filename)

    elif option == "exit":
        print("Goodbye!")
        break
    else:
        print(f"{option} is not a correct choice, try again...")