from py_test_api.utils.api_method_helper import *
import logging
import allure

logger = logging.getLogger(__name__)


@allure.testcase('ITC-001')
def test_create_task():
    """
    This test case checks whether the create_task function successfully creates a task by sending a new task payload.
    It then verifies that the created task has the expected values by retrieving and validating the task details.
    """
    # Create a new task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    # Get and verify the task details
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    data = get_task_response.json()
    assert data['task_id'] == task_id
    assert data['user_id'] == payload["user_id"]
    assert data['content'] == payload["content"]


@allure.testcase('ITC-002')
def test_update_task():
    """
    This test case checks whether the update_task function successfully updates the details of an existing task.
    It involves creating a task, updating its content and status, and then verifying the changes.
    """
    # Create a new task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    # Update the task
    updated_task_payload = {
        "task_id": task_id,
        "user_id": payload["user_id"],
        "content": "Task content updated!",
        "is_done": True,
    }
    update_task_response = update_task(updated_task_payload)
    assert update_task_response.status_code == 200

    # Get and verify the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 201
    data = get_task_response.json()
    assert data['task_id'] == updated_task_payload['task_id']
    assert data['user_id'] == updated_task_payload['user_id']
    assert data['content'] == updated_task_payload['content']
    assert data['is_done'] == updated_task_payload['is_done']


@allure.testcase('ITC-003')
def test_list_tasks():
    """
    This test case checks whether the list_tasks function successfully retrieves a list of tasks for a given user_id.
    It involves creating a specified number of tasks under the same user_id and then verifying that the listed tasks
    match the expected count.
    """
    # Create N new tasks under same user_id. For this endpoint the limit is 10
    n = 10
    payload = new_task_payload()
    for _ in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    # List tasks, and check the number of tasks
    list_tasks_response = list_tasks(payload['user_id'])
    assert list_tasks_response.status_code == 200
    data = list_tasks_response.json()
    assert len(data['tasks']) == n


@allure.testcase('ITC-004')
def test_delete_task():
    """
    This test case verifies whether the delete_task function successfully removes a task by creating a task,
    deleting it, and then attempting to retrieve it to ensure it no longer exists.
    """
    # Create a new task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    # Delete the created task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    # Get and verify if the task exist
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404
