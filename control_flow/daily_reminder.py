task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority.lower():
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is high priority task. Please complete it immediately.")
        else:
            print(f"Note: '{task}' is high priority task. Please complete it as soon as possible.")
       
    case "medium":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is medium priority task. Please complete it within the next few days.")
        else:
            print(f"Note: '{task}' is medium priority task. Please complete it within the week.")
    
    case "low":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is low priority task. Please complete it when you have time.")
        else:
            print(f"Note: '{task}' is low priority task. You can complete it at your convenience.")
    
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")