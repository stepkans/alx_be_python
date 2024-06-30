task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

reminder = f"Reminder: '{task}' is a {priority} priority task"

match priority:
    case "high":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Make sure to complete it as soon as possible." 
    case "medium":
        if time_bound == "yes":
            reminder += " that should be completed soon."
        else:
            reminder += ". Try to finish this in a timely manner."    
    case "low":
        if time_bound == "yes":
            reminder += " that needs to be done probably today."
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority. Please enter high, medium, or low."

print(reminder)
