"""A module for interacting with a todo application API hosted at https://todo.pixegami.io.

Functions:
- get_task(task_id): Retrieve details of a specific task.
- list_tasks(user_id): Retrieve a list of tasks associated with a user.
- create_task(payload): Create a new task using the provided payload.
- update_task(payload): Update an existing task with the provided payload.
- delete_task(task_id): Delete a task with the specified task_id.
- new_task_payload(): Generate a new payload for creating a task, including a unique user_id and content.
"""

import requests
import uuid
import logging

logger = logging.getLogger(__name__)
ENDPOINT = 'https://todo.pixegami.io'


def get_task(task_id):
    """
    Retrieve details of a specific task.

    Args:
        task_id (str): The unique identifier for the task.

    Returns:
        requests.Response: The response object from the API request.
    """
    logger.info('Starting GET request')
    return requests.get(ENDPOINT + f'/get-task/{task_id}')


def list_tasks(user_id):
    """
    Retrieve a list of tasks associated with a user.

    Args:
        user_id (str): The unique identifier for the user.

    Returns:
        requests.Response: The response object from the API request.
    """
    logger.info('Starting GET request')
    return requests.get(ENDPOINT + f'/list-tasks/{user_id}')


def create_task(payload):
    """
    Create a new task using the provided payload.

    Args:
        payload (dict): A dictionary containing task information.

    Returns:
        requests.Response: The response object from the API request.
     """
    logger.info('Starting PUT request')
    return requests.put(ENDPOINT + '/create-task', json=payload)


def update_task(payload):
    """
    Update an existing task with the provided payload.

    Args:
        payload (dict): A dictionary containing task information.

    Returns:
        requests.Response: The response object from the API request.
    """
    logger.info('Starting PUT request')
    return requests.put(ENDPOINT + '/update-task', json=payload)


def delete_task(task_id):
    """
    Delete a task with the specified task_id.

    Args:
        task_id (str): The unique identifier for the task.

    Returns:
        requests.Response: The response object from the API request.
    """
    logger.info('Starting DELETE request')
    return requests.delete(ENDPOINT + f'/delete-task/{task_id}')


def new_task_payload():
    """
    Generate a new payload including a random unique user_id and content.

    Returns:
        dict: A dictionary containing information to creating a new task.
    """
    user_id = f"test_user_{uuid.uuid4().hex}"  # Return a string hex representation of a user_id
    content = f"test_content_{uuid.uuid4().hex}"  # Return a string hex representation of a content
    return {
        'content': content,
        'user_id': user_id,
        'is_done': False
    }
