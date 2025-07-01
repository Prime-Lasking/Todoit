def add_task(tasks, task):
    tasks.append(task)
    print(f'Added {task}')          

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed successfully.")
    else:
        print(f"Task '{task}' not found.")

def load_tasks_from_file(tasks, filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            for line in f:
                task = line.strip()
                if task:
                    tasks.append(task)

def clear_tasks(tasks):
    tasks.clear()
    print("All tasks cleared.")
