import re

ALLOWED_CHARACTERS = re.compile("^[a-zA-Z0-9\s,.'-]+$")  # Letters, digits, spaces, and common punctuation

MAX_TASK_LENGTH = 255
MIN_TASK_LENGTH = 1  

tasks = []

def add_task(task_name: str):
    if not isinstance(task_name, str):
        raise ValueError("Task name must be a string.")
    

    task_length = len(task_name)
    if task_length < MIN_TASK_LENGTH or task_length > MAX_TASK_LENGTH:
        raise ValueError(f"Task name must be between {MIN_TASK_LENGTH} and {MAX_TASK_LENGTH} characters.")
    
    # Validate task description using allow characters list
    if not ALLOWED_CHARACTERS.match(task_name):
        raise ValueError("Task name contains invalid characters.")

    # If the validation passes, add the task to the list of tasks
    task = {
        "task": task_name,
        "status": "pending"
    }
    tasks.append(task)
    return "Task added successfully."

def view_tasks():
    if not tasks:
        return "No tasks available."
    return tasks

def update_task_status(task_name, status):
    for task in tasks:
        if task["task"] == task_name:
            task["status"] = status
            return f"Task '{task_name}' status updated to {status}."
    return "Task not found."

def delete_task(task_name):
    for task in tasks:
        if task["task"] == task_name:
            tasks.remove(task)
            return f"Task '{task_name}' deleted."
    return "Task not found."

def search_task(search_term):
    found_tasks = [task for task in tasks if search_term.lower() in task["task"].lower()]
    return found_tasks if found_tasks else "No tasks found matching the search term."
