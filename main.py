#
#   file name: main.py
#   author: MrQwerty13 (Mikhail Pozur)
#   date of creation: 18.05.2026 (UTC+3)
#

"""Entry point for the Task Tracker application."""

from UI.console_work import ConsoleWork


def main_console():
    """Create and run the console-based task tracker."""
    task_tracker = ConsoleWork(running=True, file_name="tasks.txt")
    task_tracker.run()


if __name__ == "__main__":
    main_console()