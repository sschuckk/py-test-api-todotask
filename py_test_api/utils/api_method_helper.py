import requests
import uuid

ENDPOINT = 'https://todo.pixegami.io'


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
