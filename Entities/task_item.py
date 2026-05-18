#
#   file name: task_item.py
#   author: MrQwerty13 (Mikhail Pozur)
#   date of creation: 18.05.2026 (UTC+3)
#

# Import all necessaries
from Entities.task_enum import TaskItemStatus


class TaskItem:
    """
        Class TaskItem:
            Attributes:
                _id (int):
                    id for this TaskItem which is given by database
                _name (str):
                    name of the TaskItem which is given by user
                _status (TaskItemStatus):
                    status of the TaskItem which is given by default
    """
    def __init__(self, _id: int, _name: str, _status: TaskItemStatus = TaskItemStatus.UNDONE):
        self._id = _id
        self._name = _name
        self._status = _status

    def id(self) -> int:
        return self._id

    def name(self) -> str:
        return self._name

    def status(self) -> TaskItemStatus:
        return self._status