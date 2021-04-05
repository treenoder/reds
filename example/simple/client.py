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
