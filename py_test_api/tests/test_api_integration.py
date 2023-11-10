from py_test_api.utils.api_method_helper import *
import logging

logger = logging.getLogger(__name__)


def test_get_api():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_create_task():
    # Create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    # Get and validate the values
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    data = get_task_response.json()
    assert data['task_id'] == task_id
    assert data['user_id'] == payload["user_id"]
    assert data['content'] == payload["content"]


def test_update_task():
    # Create a task
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

    # Get and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    data = get_task_response.json()
    assert data['task_id'] == updated_task_payload['task_id']
    assert data['user_id'] == updated_task_payload['user_id']
    assert data['content'] == updated_task_payload['content']
    assert data['is_done'] == updated_task_payload['is_done']


def test_list_tasks():
    # Create N tasks under same user_id
    n = 10
    payload = new_task_payload()
    for _ in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    # List tasks, and check items
    list_tasks_response = list_tasks(payload['user_id'])
    assert list_tasks_response.status_code == 200
    data = list_tasks_response.json()
    assert len(data['tasks']) == n


def test_delete_task():
    # Create task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    # Delete task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    # Get and verify task
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404
