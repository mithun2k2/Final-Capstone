import os
from datetime import datetime

DATETIME_STRING_FORMAT = "%Y-%m-%d"


# Function to register a new user
def reg_user():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Please choose a different username.")
    else:
        users.append(username)
        with open("user.txt", "a") as user_file:
            user_file.write(username + "\n")
        print(f"User '{username}' has been registered successfully.")


    # The user will then be promted to enter password
        new_password = input("Please enter a new passpword: ")

    # The user is asked to confirm their password
        
        pass_confirm = input ("Please confirm your new password: ")
    # If the new and confirmed password values do not match, an appropriate error message is displayed.
    # The user is then prompted to enter their new password and confirm it until they match.
        
        while new_password != pass_confirm: 
            print(" Your confirmed password doesnt match with the original password.")

            new_password = input("Pleasec enter your password: \n")
            pass_confirm = input("Please confirm your new password: \n")

        if new_password == pass_confirm:
            print("Your Password is valid.")

            passwords_list.append(new_password) # The new passwrod is added to the password list

            users["Passwords"] = passwords_list # the list is updated in the user details.

             # user.txt file opened to write to.
            with open('user.txt', 'r+') as f:

                # Using for statement to print username and passwords on separate lines.
                # The number of lines is equal to the number of items in usernames_list.
                for i in range(len(users)):

                        # Writing from the apppropriate dictionary keys, in the correct format. 
                        f.write(username["Usernames"][i] + ", " + username["Passwords"][i] + '\n')
                        
        # Message returned at the end of function.
        return("Your new username and password have been successfully added.")


        

# Function to add a new task
def add_task():
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    assigned_to = input("Enter the username of the person the task is assigned to: ")
    date_assigned = datetime.today().strftime('%Y-%m-%d')
    due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
    task_completed = "No"
    
    task = f"{title}, {description}, {assigned_to}, {date_assigned}, {due_date}, {task_completed}\n"
    
    tasks.append(task)
    with open("tasks.txt", "a") as tasks_file:
        tasks_file.write(task)
    print("Task has been added successfully.")

# Function to view all tasks
def view_all():
    print("\nAll Tasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

# Function to view tasks assigned to the current user
def view_mine():
    username = input("Enter your username: ")
    print(f"\nTasks assigned to {username}:")
    
    for index, task in enumerate(tasks):
        task_details = task.split(", ")
        if task_details[2] == username:
            print(f"{index + 1}. Title: {task_details[0]}, Due Date: {task_details[4]}, Completed: {task_details[5]}")

    selected_task = int(input("Enter the number of the task to edit or mark as complete (-1 to return to main menu): "))
    if selected_task != -1:
        edit_or_complete_task(selected_task - 1)

# Function to edit or mark a task as complete
def edit_or_complete_task(task_index):
    task_details = tasks[task_index].split(", ")
    if task_details[5].strip() == "Yes":
        print("Cannot edit a completed task.")
    else:
        print(f"Selected Task: Title: {task_details[0]}, Description: {task_details[1]}, "
              f"Assigned to: {task_details[2]}, Due Date: {task_details[4]}, Completed: {task_details[5]}")
        choice = input("Enter 'M' to mark as complete, 'E' to edit, or any other key to cancel: ")
        if choice.upper() == 'M':
            tasks[task_index] = tasks[task_index].replace("No", "Yes")
            print("Task marked as complete.")
        elif choice.upper() == 'E':
            new_assigned_to = input("Enter the new username for assignment: ")
            new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
            tasks[task_index] = f"{task_details[0]}, {task_details[1]}, {new_assigned_to}, " \
                                f"{task_details[3]}, {new_due_date}, {task_details[5]}\n"
            print("Task edited successfully.")
        else:
            print("Task not modified.")

# Function to generate reports

# This funtion generate report for all type of user tasks based upon due or completion.


def generate_reports():
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task.split(", ")[5].strip() == "Yes")
    incomplete_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for task in tasks if task.split(", ")[5].strip() == "No" and datetime.strptime(task.split(", ")[4], DATETIME_STRING_FORMAT) < datetime.today())

    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write(f"Total tasks: {total_tasks}\n")
        task_overview_file.write(f"Completed tasks: {completed_tasks}\n")
        task_overview_file.write(f"Incomplete tasks: {incomplete_tasks}\n")
        task_overview_file.write(f"Overdue tasks: {overdue_tasks}\n")
        task_overview_file.write(f"Percentage of incomplete tasks: {(incomplete_tasks / total_tasks) * 100:.2f}%\n")
        task_overview_file.write(f"Percentage of overdue tasks: {(overdue_tasks / incomplete_tasks) * 100:.2f}%\n")

    with open("user_overview.txt", "w") as user_overview_file:
        user_overview_file.write(f"Total users: {len(users)}\n")
        user_overview_file.write(f"Total tasks: {total_tasks}\n")
        
        for user in users:
            user_tasks = sum(1 for task in tasks if task.split(", ")[2] == user)
            user_completed_tasks = sum(1 for task in tasks if task.split(", ")[2] == user and task.split(", ")[5].strip() == "Yes")
            user_incomplete_tasks = user_tasks - user_completed_tasks
            user_overdue_tasks = sum(1 for task in tasks if task.split(", ")[2] == user and task.split(", ")[5].strip() == "No" and datetime.strptime(task.split(", ")[4], DATETIME_STRING_FORMAT ) < datetime.today())

            user_overview_file.write(f"\nUser: {user}\n")
            user_overview_file.write(f"Total tasks assigned: {user_tasks}\n")
            user_overview_file.write(f"Percentage of total tasks: {(user_tasks / total_tasks) * 100:.2f}%\n")
            user_overview_file.write(f"Percentage of completed tasks: {(user_completed_tasks / user_tasks) * 100:.2f}%\n")
            user_overview_file.write(f"Percentage of incomplete tasks: {(user_incomplete_tasks / user_tasks) * 100:.2f}%\n")
            user_overview_file.write(f"Percentage of overdue tasks: {(user_overdue_tasks / user_incomplete_tasks) * 100:.2f}%\n")

# Main loop
users = []  # List to store registered users
tasks = []  # List to store tasks
passwords_list = []

# Load existing users and tasks from files
if not os .path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

if os.path.exists("user.txt"):
    with open("user.txt", "r") as user_file:
        users = user_file.read().splitlines()
        passwords_list.append(users)

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as tasks_file:
        tasks = tasks_file.read().splitlines()

# Writing the program for the task manager.
# Getting input from the user on their login details.
username = input("Please enter your username: \n")
password = input("Please enter your password: \n")

# Creating a while loop to run indefinitely whilst login details are incorrect.
# Appropriate error messages are displayed.
# Use of the words 'in' and 'not in' used to test whether the username and password appear in the appropriate lists.
while (username not in username) or (password not in passwords_list):

        # If username is correct and password is correct, the following message is displayed.
        if (username not in username) and (password in passwords_list):

            print("Your username is not listed.")

            username = input("Please re-enter your username: \n")  # User is prompted to re-enter details. 
            password = input("Please re-enter your password: \n")

        # If password is incorrect and username is correct, the following message is displayed.
        elif (password not in passwords_list) and (username in username):

            print("Your password is incorrect.")

            username = input("Please re-enter your username: \n")
            password = input("Please re-enter your password: \n")

        # If both the username and password are incorrect, the following message is displayed. 
        elif (username not in username) and (password not in passwords_list):

            print("Your username and password are incorrect.")

            username = input("Please re-enter your username: \n")
            password = input("Please re-enter your password: \n")

# If both username and password are correct, the successful login message is displayed.            
if (username in username) and (password in passwords_list):

    print("You are successfully logged in.")


# Indefinite loop created to display the menu once the user is logged in.
# This allows the user to return to the menu after each option.
# If they wish to exit the program, they can choose the 'exit' option from the menu. 
while True:

    if username == "admin" and password == "password":  # The admin user views a specific menu with extra options (gr and ds).

        menu = input("""\nPlease select one of the following options:

r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit

""").lower()            

    else:  # All other users can only view the basic menu. 

       menu = input("""\nPlease select one of the following options:

r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
e - exit

""").lower()

    choice = input("Enter your choice: ")

    if choice == 'r':
        reg_user()
    elif choice == 'a':
        add_task()
    elif choice == 'va':
        view_all()
    elif choice == 'vm':
        view_mine()
    elif choice == 'gr':
        generate_reports() # Calling function to generate report
        print("Reports generated successfully.")
    elif choice == 'ds':
        generate_reports() # Calling function generate files incase they do not exist yet

        print ("""\n------------------------------------
               
               The Task Overview Report is as follows:

               -----------------------------------------\n""")      # Heading printed for user friendly display
        with open ('task_overview.txt', 'r+') as f1: # Opening the taskover_view file to get info from it
            for line in f1:
                print(line) # Printing/displaying each line in the file
        print ("""\n------------------------------------
               
               The User Overview Report is as follows:

               -----------------------------------------\n""")      # Heading printed for user friendly display
        with open ('user_overview.txt', 'r+') as f2: # Opening the taskover_view file to get info from it
            for line in f2:
                print(line) # Printing/displaying each line in the file
        print("""\n---------------------------------------------------

                    End of Statistics Reports
              
                ------------------------------------------------------\n""")  # End of reports display.
        
    elif choice == 'e':
        print("\nQuitting application. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.")