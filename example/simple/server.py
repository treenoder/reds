import time
from random import random

from redis import StrictRedis
from reds import Reds


def main():
    key = 'test:queue'
    redis = StrictRedis()
    reds = Reds(redis=redis, key=key)
    for task in reds.listen():
        print(task)
        time.sleep(1)
        task.respond(task_dict={
            'success': random() > 0.5
        })


if __name__ == '__main__':
    main()
