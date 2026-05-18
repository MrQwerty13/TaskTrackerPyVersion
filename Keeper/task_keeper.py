from Entities.task_item import TaskItem
from Entities.task_item_atributies import TaskItemStatus


class TaskKeeper:
    def __init__(self, tasks: dict[int, TaskItem]) -> None:
        self._tasks = tasks

    def add_task(self, name: str) -> bool:
        _id = max(self._tasks.keys()) + 1
        if _id <= 10:
            self._tasks[_id] = TaskItem(_id, name)
            return True
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