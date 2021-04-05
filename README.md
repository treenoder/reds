[![Python package](https://github.com/treenoder/reds/actions/workflows/python-package.yml/badge.svg)](https://github.com/treenoder/reds/actions/workflows/python-package.yml)
[![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)](https://pypi.org/project/reds)
# reds
Request/Response library on top of Redis.

## Simple Client/Server example
### Client:
```python
from redis import StrictRedis
from reds import Reds


def main():
    key = 'test:queue'
    redis = StrictRedis()
    reds = Reds(redis=redis, key=key)
    for i in range(10):
        task = reds.create_task(task_dict={
            'id': i
        })
        print(task.send())


if __name__ == '__main__':
    main()

```
### Server:
```python
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
```