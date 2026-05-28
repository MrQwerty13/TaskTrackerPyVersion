#
#   file name: task_keeper.py
#   author: MrQwerty13 (Mikhail Pozur)
#   date of creation: 18.05.2026 (UTC+3)
#

from Entities.task_item import TaskItem


class TaskKeeper:
    MAX_TASKS = 10   # maximum number of tasks allowed

    def __init__(self, tasks: dict[int, TaskItem]) -> None:
        self._tasks = tasks

    def add_task(self, name: str) -> bool:
        """Add a new task with the smallest available ID (1..MAX_TASKS)."""
        if len(self._tasks) >= self.MAX_TASKS:
            return False

        # Find the first unused ID (after renumbering this will be len+1)
        for _id in range(1, self.MAX_TASKS + 1):
            if _id not in self._tasks:
                self._tasks[_id] = TaskItem(_id, name)
                return True
        return False   # should never be reached due to the length check

    def remove_task(self, _id: int) -> bool:
        """Remove a task and renumber all higher IDs so they stay contiguous."""
        if _id not in self._tasks:
            return False

        # Get all tasks sorted by current ID
        sorted_tasks = sorted(self._tasks.values(), key=lambda t: t.id())

        # Remove the target task
        remaining = [t for t in sorted_tasks if t.id() != _id]

        # Rebuild the dictionary with new keys 1..N, updating each task's ID
        new_tasks = {}
        for new_id, task in enumerate(remaining, start=1):
            task.set_id(new_id)
            new_tasks[new_id] = task

        self._tasks = new_tasks
        return True

    def change_task_status(self, _id: int) -> bool:
        if _id in self._tasks:
            self._tasks[_id].toggle_status()
            return True
        return False

    def tasks(self) -> dict[int, TaskItem]:
        return self._tasks