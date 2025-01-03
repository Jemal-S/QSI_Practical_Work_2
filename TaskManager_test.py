import pytest
from task_manager import add_task, view_tasks, update_task_status, delete_task, search_task, tasks

@pytest.fixture(autouse=True)
def setup_and_teardown():
    tasks.clear()
    yield
    tasks.clear()

#Owasp Input validation standard tests
def test_add_task_valid_input():
    response = add_task("Buy groceries")
    assert response == "Task added successfully."
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Buy groceries"

def test_add_task_invalid_characters():
    with pytest.raises(ValueError, match="Task name contains invalid characters."):
        add_task("Buy groceries <script>alert('hack');</script>")

def test_add_task_length_check():
    with pytest.raises(ValueError, match="Task name must be between 1 and 255 characters."):
        add_task("")  # Too short
    with pytest.raises(ValueError, match="Task name must be between 1 and 255 characters."):
        add_task("A" * 256)  # Too long



def test_view_tasks():
    add_task("Buy groceries")
    add_task("Walk the dog")
    task_list = view_tasks()
    assert len(task_list) == 2
    assert task_list[0]["task"] == "Buy groceries"
    assert task_list[1]["task"] == "Walk the dog"

def test_update_task_status():
    add_task("Buy groceries")
    response = update_task_status("Buy groceries", "completed")
    assert response == "Task 'Buy groceries' status updated to completed."
    assert tasks[0]["status"] == "completed"

def test_update_task_status_not_found():
    response = update_task_status("Nonexistent Task", "completed")
    assert response == "Task not found."

def test_delete_task():
    add_task("Buy groceries")
    response = delete_task("Buy groceries")
    assert response == "Task 'Buy groceries' deleted."
    assert len(tasks) == 0

def test_delete_task_not_found():
    response = delete_task("Nonexistent Task")
    assert response == "Task not found."

def test_search_task():
    add_task("Buy groceries")
    add_task("Walk the dog")
    result = search_task("groceries")
    assert len(result) == 1
    assert result[0]["task"] == "Buy groceries"

def test_search_task_not_found():
    add_task("Buy groceries")
    result = search_task("nonexistent")
    assert result == "No tasks found matching the search term."
