#
#   file name: console_work.py
#   author: MrQwerty13 (Mikhail Pozur)
#   date of creation: 18.05.2026 (UTC+3)
#

# Import all necessaries
from Keeper.task_keeper import TaskKeeper

from Repository.task_repo import TaskRepo


class ConsoleWork:
    def __init__(self, running: bool, file_name: str):
        self._running = running
        self._task_repo = TaskRepo(file_name)
        self._keeper = TaskKeeper(self._task_repo.format_data())

    def run(self) -> None:
        def logo():
            print("=== Tasks ===")

        def tasks():
            for task in self._task_repo.read_file():
                print(task)

        def options():
            print("=== Options ===")
            print("1. Add task")
            print("2. Remove task")
            print("3. Change task status")
            print("4. Exit")

        while self._running:
            logo()
            tasks()
            options()
            user_choice = int(input("Enter your choice: "))
            match user_choice:
                case 1:
                    name = input("Enter task name: ")
                    self._keeper.add_task(name)
                    self._task_repo.write_file(self._keeper.tasks())
                case 2:
                    _id = int(input("Enter task id: "))
                    self._keeper.remove_task(_id)
                    self._task_repo.write_file(self._keeper.tasks())
                case 3:
                    _id = int(input("Enter task id: "))
                    self._keeper.change_task_status(_id)
                    self._task_repo.write_file(self._keeper.tasks())
                case 4:
                    print("Exiting...")
                    break
                case _:
                    print("Invalid input")