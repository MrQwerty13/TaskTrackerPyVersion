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
    def __init__(self, id: int, name: str, status: TaskItemStatus = TaskItemStatus.UNDONE):
        self._id = id
        self._name = name
        self._status = status

    def id(self) -> int:
        return self._id

    def name(self) -> str:
        return self._name

    def status(self) -> TaskItemStatus:
        return self._status

    def toggle_status(self) -> None:
        """Switch status between DONE and UNDONE."""
        self._status = (
            TaskItemStatus.UNDONE if self._status == TaskItemStatus.DONE
            else TaskItemStatus.DONE
        )