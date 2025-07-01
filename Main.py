import time
import os
from function import *

Tasks = []

# Load tasks from file if it exists
folder_name = 'Todoit'
file_name = 'Task.txt'
full_file_path = os.path.join(folder_name, file_name)
if os.path.exists(full_file_path):
    with open(full_file_path, 'r') as f:
        Tasks = [line.strip() for line in f if line.strip()]

bot_name: str = 'Todoit'

print(f'Hello! I\'m {bot_name}!')
print(f'Press 1 for adding Tasks')
print(f'Press 2 for removing Tasks')
print(f'Press 3 for viewing Tasks')
print(f'Press 4 for Shutting Down')
print(f'Press 5 for save Tasks')
print(f'Press 6 for clear all Tasks')

flag = True
while flag is True:
    user_input: str = input('You:').lower()

    if user_input == '1':
        task = input('What task do you want added: ')
        add_task(Tasks, task)
    elif user_input == '2':
        if not Tasks:
            print("No tasks to remove.")
            continue
        print("Here are your tasks:")
        for idx, task in enumerate(Tasks, 1):
            print(f"{idx}. {task}")
        task_to_remove = input("Enter the task you want to remove: ")
        remove_task(Tasks, task_to_remove)
    elif user_input == '3':
        if not Tasks:
            print("No tasks to show.")
        else:
            for idx, task in enumerate(Tasks, 1):
                print(f"{idx}. {task}")
    elif user_input == '4':
        print("Shutting Down")
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        break
    elif user_input == '5':
        with open(full_file_path, 'w') as f:
            for task in Tasks:
                f.write(task + '\n')
        print("Tasks saved")
    elif user_input == '6':
        choice = input("Are you sure?")
        if choice in ['Yes','yes']:
         clear_tasks(Tasks)
         with open(full_file_path, 'w') as f:
            f.write('                                                                                                  ')
    else:
        print("Invalid input. Please try again.")
        if choice in ['no','No']:
            print('Ok')


