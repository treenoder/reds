import json
import uuid


__all__ = 'Task'

from typing import Optional


class Task:
    def __init__(self, reds, task_id, task_dict):
        self.reds = reds
        self.task_id = task_id
        self.task_dict = task_dict

    @classmethod
    def new(cls, reds, task_dict):
        return cls(reds=reds, task_id=str(uuid.uuid4()), task_dict=task_dict)

    @classmethod
    def from_json(cls, reds, json_data):
        data = json.loads(json_data)
        return cls.from_dict(reds=reds, data=data)

    @classmethod
    def from_dict(cls, reds, data):
        return cls(
            reds=reds,
            task_id=data['task_id'],
            task_dict=data['task_dict']
        )

    def to_dict(self):
        # type: () -> dict
        return {
            'task_id': self.task_id,
            'task_dict': self.task_dict
        }

    def get_response(self, block=True, timeout=0):
        # type: (bool, int) -> Optional[dict]
        key = self.reds.response_key + ':' + self.task_id
        if block:
            result = self.reds.redis.brpop(key, timeout)
            if result is None:
                return None
            json_data = result[1]
        else:
            json_data = self.reds.redis.rpop(key)
        if json_data is None:
            return None
        self.reds.redis.delete(key)
        return json.loads(json_data)

    def send(self, wait_for_response=True, timeout=0):
        # type: (bool, int) -> Optional[dict]
        self.reds.redis.lpush(self.reds.request_key, json.dumps(self.to_dict()))
        if wait_for_response:
            return self.get_response(block=wait_for_response, timeout=timeout)

    def respond(self, task_dict):
        # type: (dict) -> None
        self.reds.redis.lpush(self.reds.response_key + ':' + self.task_id, json.dumps(task_dict))

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return 'Task(task_id={}, task_dict={})'.format(self.task_id, self.task_dict)
