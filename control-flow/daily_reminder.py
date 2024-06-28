'''
a simplified Python script that uses conditional statements, Match Case,
 and loops to remind the user about a single, 
 priority task for the day based on time sensitivity.
'''
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case x if x == "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print("Note: '{task}' is a high priority task. Consider completing it when you have free time.")

    case x if x =="medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        elif time_bound == "no":
            print("Note: '{task}' is a low medium task. Consider completing it when you have free time.")

    case x if x == "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

