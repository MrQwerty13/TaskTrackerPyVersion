#
#   file name: task_keeper.py
#   author: MrQwerty13 (Mikhail Pozur)
#   date of creation: 18.05.2026 (UTC+3)
#

# Import all necessaries
from Entities.task_item import TaskItem
from Entities.task_enum import TaskItemStatus


class TaskKeeper:
    """
        Task Keeper:
            Attributes:
                _tasks (dict[int, TaskItem]):
                    dictionary of task items

            Methods:
                add_task:
                    :argument - name of task to add (str)
                    :return - True if task was added else False

                remove_task:
                    :argument - _id of task to remove (int)
                    :return - True if task was removed else False

                change_task_status:
                    :argument - _id of task to change (int)
                    :return - True if task's status was changed else False

                tasks:
                    :argument - None
                    :return - dictionary of task items (dict[int, TaskItem])
    """
    def __init__(self, tasks: dict[int, TaskItem]) -> None:
        self._tasks = tasks

    def add_task(self, name: str) -> bool:
        if len(self._tasks.keys()) > 0:
            _id = max(self._tasks.keys()) + 1
            if _id <= 10:
                self._tasks[_id] = TaskItem(_id, name)
                return True
        else:
            self._tasks[1] = TaskItem(1, name)
        return False

    def remove_task(self, _id: int) -> bool:
        if _id in self._tasks.keys():
            self._tasks.pop(_id)
            return True
        return False

    def change_task_status(self, _id: int) -> bool:
        if _id in self._tasks.keys():
            task = self._tasks[_id]
            match (task._status):
                case TaskItemStatus.DONE:
                    task._status = TaskItemStatus.UNDONE
                    return True
                case TaskItemStatus.UNDONE:
                    task._status = TaskItemStatus.DONE
                    return True
        return False

    def tasks(self) -> dict[int, TaskItem]:
        return self._tasks