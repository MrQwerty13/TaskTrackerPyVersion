#   file name: task_item.py
#   author: MrQwerty13 (Mikhail Pozur)
#   date of creation: 18.05.2026 (UTC+3)
#

from Entities.task_enum import TaskItemStatus


class TaskItem:
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
        self._status = (
            TaskItemStatus.UNDONE if self._status == TaskItemStatus.DONE
            else TaskItemStatus.DONE
        )

    def set_id(self, new_id: int) -> None:
        """Update the internal ID (used after renumbering)."""
        self._id = new_id