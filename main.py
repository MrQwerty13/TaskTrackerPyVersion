#
#   file name: main.py
#   author: MrQwerty13 (Mikhail Pozur)
#   date of creation: 18.05.2026 (UTC+3)
#

"""Entry point for the Task Tracker application."""

from UI.console_work import ConsoleWork
from UI.tkinter_work import TkinterWork


def main_console():
    """Create and run the console-based task tracker."""
    task_tracker = ConsoleWork(running=True, file_name="tasks.txt")
    task_tracker.run()

def main_tkinter():
    tkinter_work = TkinterWork()
    tkinter_work.run()

def main():
    app_view = input("Choose app view (C - console / W - windowed): ")
    if app_view == "C":
        main_console()
    elif app_view == "W":
        main_tkinter()
    else:
        print("Invalid choice.")
        main()

if __name__ == "__main__":
    main()