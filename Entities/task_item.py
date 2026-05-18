from task_item_atributies import TaskItemStatus


class TaskItem:
    def __init__(self, _id: int, _name: str, _status: TaskItemStatus = TaskItemStatus.UNDONE):
        self._id = _id
        self._name = _name
        self._status = _status