#
#   file name: console_work.py
#   author: MrQwerty13 (Mikhail Pozur)
#   date of creation: 18.05.2026 (UTC+3)
#

from Keeper.task_keeper import TaskKeeper
from Repository.task_repo import TaskRepo


class ConsoleWork:
    def __init__(self, running: bool, file_name: str):
        self._running = running
        self._task_repo = TaskRepo(file_name)
        self._keeper = TaskKeeper(self._task_repo.format_data())

    def run(self) -> None:
        while self._running:
            self._show_logo()
            self._show_tasks()
            self._show_options()

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input – please enter a number.")
                continue

            if choice == 1:
                name = input("Enter task name: ").strip()
                if self._keeper.add_task(name):
                    print(f"Task '{name}' added.")
                else:
                    print("Failed to add task. Task list may be full.")
            elif choice == 2:
                try:
                    _id = int(input("Enter task id: "))
                except ValueError:
                    print("Invalid ID – must be a number.")
                    continue
                if self._keeper.remove_task(_id):
                    print(f"Task {_id} removed.")
                else:
                    print(f"No task with ID {_id}.")
            elif choice == 3:
                try:
                    _id = int(input("Enter task id: "))
                except ValueError:
                    print("Invalid ID – must be a number.")
                    continue
                if self._keeper.change_task_status(_id):
                    print(f"Task {_id} status toggled.")
                else:
                    print(f"No task with ID {_id}.")
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice – please enter 1, 2, 3 or 4.")

            # Persist changes to file after any modification
            self._task_repo.write_file(self._keeper.tasks())

    def _show_logo(self):
        print("\n=== Tasks ===")

    def _show_tasks(self):
        # Display from keeper for a consistent in‑memory view
        tasks = self._keeper.tasks()
        if not tasks:
            print("(no tasks)")
        else:
            for _id, task in sorted(tasks.items()):
                print(f"ID: {_id} | NAME: {task.name()} | STATUS: {task.status().value}")

    def _show_options(self):
        print("=== Options ===")
        print("1. Add task")
        print("2. Remove task")
        print("3. Change task status")
        print("4. Exit")