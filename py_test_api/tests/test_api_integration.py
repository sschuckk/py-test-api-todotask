import requests

ENDPOINT = 'https://todo.pixegami.io'


def test_get_api():
    response = requests.get(ENDPOINT)
    print(response)
    data = response.json()
    print(data)


def test_create_task():
    response = create_task(new_task_payload())
    assert response.status_code == 200
    data = response.json()
    task_id = data['task']['task_id']
    response = get_task(task_id)
    assert response.status_code == 200
    data = response.json()
    assert data['task_id'] == task_id
    assert data['user_id'] == new_task_payload()["user_id"]
    assert data['content'] == new_task_payload()["content"]


def test_update_task():
    # Create a task
    response = create_task(new_task_payload())
    assert response.status_code == 200
    data = response.json()
    task_id = data['task']['task_id']

    # Update the task
    updated_task_payload = {
        "task_id": task_id,
        "user_id": new_task_payload()["user_id"],
        "content": "Task content updated!",
        "is_done": True,
    }
    response = update_task(updated_task_payload)
    assert response.status_code == 200

    # Get and validate the changes
    response = get_task(task_id)
    assert response.status_code == 200
    data = response.json()
    print(data)


def get_task(task_id):
    return requests.get(ENDPOINT + f'/get-task/{task_id}')


def list_task(user_id):
    return requests.get(ENDPOINT + f'/get-task/{user_id}')


def create_task(payload):
    return requests.put(ENDPOINT + '/create-task', json=payload)


def update_task(payload):
    return requests.put(ENDPOINT + '/update-task', json=payload)


def new_task_payload():
    return {
        "content": "Default task content",
        "user_id": "user_001",
        "is_done": False,
    }