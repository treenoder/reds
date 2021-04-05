from typing import Union, Generator

from redis import StrictRedis, Redis

from .task import Task

__all__ = 'Reds'


class Reds:
    def __init__(self, redis, key):
        # type: (Union[Redis, StrictRedis], str) -> None
        self.redis = redis
        self.request_key = key + ':request'
        self.response_key = key + ':response'
        self.__is_listening = True

    def stop(self):
        """
        Stop listening after last task
        """
        self.__is_listening = False

    @property
    def is_listening(self):
        return self.__is_listening

    def listen(self):
        # type: () -> Generator[Task]
        """
        Listen for incoming tasks
        Example: for task in reds_instance.listen()
        """
        self.__is_listening = True
        while self.__is_listening:
            yield self.task_from(self.redis.brpop(self.request_key)[1])

    def create_task(self, task_dict):
        # type: (dict) -> Task
        """
        Create new task with task_dict content to send
        """
        return Task.new(reds=self, task_dict=task_dict)

    def task_from(self, data):
        # type: (Union[str, bytes, bytearray, dict]) -> Task
        """
        Create task from existing data. json string, json bytes or dict
        """
        if isinstance(data, str) or isinstance(data, bytes) or isinstance(data, bytearray):
            return Task.from_json(reds=self, json_data=data)
        elif isinstance(data, dict):
            return Task.from_dict(reds=self, data=data)
        raise Exception('Received unknown data: {}'.format(data))
