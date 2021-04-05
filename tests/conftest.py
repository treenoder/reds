import time
from typing import cast
try:
    from unittest import mock
except ImportError:
    import mock


import pytest
from redis import Redis

from reds import Reds


@pytest.fixture
def redis(monkeypatch):
    r = cast(Redis, mock.MagicMock())
    requests = {}
    responses = {}

    def get_storage(key):
        if ':request' in key:
            return requests
        elif ':response' in key:
            return responses
        else:
            raise Exception('invalid key {}'.format(key))

    def mock_lpush(key, val):
        storage = get_storage(key)
        if key not in storage:
            storage[key] = []
        storage[key].insert(0, val)

    def mock_rpop(key):
        storage = get_storage(key)
        if key not in storage:
            return None
        return storage[key].pop()

    def mock_brpop(key, timeout=0):
        storage = get_storage(key)
        time.sleep(0.1)
        return key, storage[key].pop()

    def mock_delete(key):
        storage = get_storage(key)
        del storage[key]

    monkeypatch.setattr(r, 'lpush', mock_lpush)
    monkeypatch.setattr(r, 'rpop', mock_rpop)
    monkeypatch.setattr(r, 'brpop', mock_brpop)
    monkeypatch.setattr(r, 'delete', mock_delete)
    return r


@pytest.fixture
def reds(redis):
    return Reds(redis=redis, key='test')
