import requests
import uuid

ENDPOINT = 'https://todo.pixegami.io'


def test_get_api():
    response = requests.get(ENDPOINT)
    print(response)
    data = response.json()
    print(data)


def test_create_task():
    # Create a task
    payload = new_task_payload()
    response = create_task(payload)
    assert response.status_code == 200
    data = response.json()
    task_id = data['task']['task_id']

    # Get and validate the values
    response = get_task(task_id)
    assert response.status_code == 200
    data = response.json()
    assert data['task_id'] == task_id
    assert data['user_id'] == payload["user_id"]
    assert data['content'] == payload["content"]


def test_update_task():
    payload = new_task_payload()
    # Create a task
    response = create_task(payload)
    assert response.status_code == 200
    data = response.json()
    task_id = data['task']['task_id']

    # Update the task
    updated_task_payload = {
        "task_id": task_id,
        "user_id": payload["user_id"],
        "content": "Task content updated!",
        "is_done": True,
    }
    response = update_task(updated_task_payload)
    assert response.status_code == 200

    # Get and validate the changes
    response = get_task(task_id)
    assert response.status_code == 200
    data = response.json()
    assert data['task_id'] == updated_task_payload['task_id']
    assert data['user_id'] == updated_task_payload['user_id']
    assert data['content'] == updated_task_payload['content']
    assert data['is_done'] == updated_task_payload['is_done']
    print(data)


def test_list_tasks():
    # Create N tasks under same user_id
    n = 10
    payload = new_task_payload()
    for _ in range(n):
        response = create_task(payload)
        assert response.status_code == 200

    # List tasks, and check items
    response = list_tasks(payload['user_id'])
    assert response.status_code == 200
    data = response.json()
    assert len(data['tasks']) == n
    print(data)


def test_delete_task():
    payload = new_task_payload()
    # Create task
    response = create_task(payload)
    assert response.status_code == 200
    task_id = response.json()['task']['task_id']

    # Delete task
    response = delete_task(task_id)
    assert response.status_code == 200

    # Get and verify task
    response = get_task(task_id)
    assert response.status_code == 404


def get_task(task_id):
    return requests.get(ENDPOINT + f'/get-task/{task_id}')


def list_tasks(user_id):
    return requests.get(ENDPOINT + f'/list-tasks/{user_id}')


def create_task(payload):
    return requests.put(ENDPOINT + '/create-task', json=payload)


def update_task(payload):
    return requests.put(ENDPOINT + '/update-task', json=payload)


def delete_task(task_id):
    return requests.delete(ENDPOINT + f'/delete-task/{task_id}')


def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"  # Return a string hex representation a a user_id
    content = f"test_content_{uuid.uuid4().hex}"
    return {
        'content': content,
        'user_id': user_id,
        'is_done': False
    }
