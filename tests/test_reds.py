import json
from typing import cast
from unittest import mock
from redis import StrictRedis, Redis
from reds import Reds, Task


def test_reds_create():
    key = 'test'
    redis = cast(Redis, mock.MagicMock())
    reds = Reds(redis=redis, key=key)
    assert reds.redis == redis
    assert reds.request_key == key + ':request'
    assert reds.response_key == key + ':response'
    assert reds.is_listening


def test_task_from_dict():
    redis = cast(Redis, mock.MagicMock())
    reds = Reds(redis=redis, key='test')
    task = reds.task_from({
        'task_id': 'id',
        'task_dict': {'id': 1}
    })
    assert isinstance(task, Task)
    assert task.task_id == 'id'
    assert task.task_dict == {'id': 1}


def test_task_from_json():
    redis = cast(Redis, mock.MagicMock())
    reds = Reds(redis=redis, key='test')
    task_data = {
        'task_id': 'id',
        'task_dict': {'id': 1}
    }
    task_json = json.dumps(task_data)
    task = reds.task_from(task_json)
    assert isinstance(task, Task)
    assert task.task_id == 'id'
    assert task.task_dict == task_data['task_dict']


def test_task_from_json_bytes():
    redis = cast(Redis, mock.MagicMock())
    reds = Reds(redis=redis, key='test')
    task_data = {
        'task_id': 'id',
        'task_dict': {'id': 1}
    }
    task_json = json.dumps(task_data).encode()
    task = reds.task_from(task_json)
    assert isinstance(task, Task)
    assert task.task_id == 'id'
    assert task.task_dict == task_data['task_dict']
