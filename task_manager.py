tasks = []

def add_task(task_name):
    tasks.append({"task": task_name, "status": "pending"})

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
