from reds import Task


def test_create(reds):
    task = Task(reds=reds, task_id='id', task_dict={'id': 1})
    assert isinstance(task, Task)
    assert task.task_id == 'id'
    assert task.task_dict == {'id': 1}


def test_get_response(reds):
    task = Task(reds=reds, task_id='id', task_dict={'id': 1})
    assert task.get_response(block=False) is None
    result = {
        'result': 'success'
    }
    task.respond(result)
    assert task.get_response(block=False) == result
    task.respond(result)
    assert task.get_response() == result


def test_get_response_timeout(reds):
    task = Task(reds=reds, task_id='id', task_dict={'id': 1})
    assert task.get_response(block=True, timeout=1) is None
