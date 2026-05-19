#!/usr/bin/env python3
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
    """Create and run the Tkinter windowed task tracker."""
    tkinter_work = TkinterWork(file_name="tasks.txt")
    tkinter_work.run()


def main():
    print("Task Tracker")
    while True:
        choice = input("Choose view: (C)onsole, (W)indowed, (Q)uit: ").strip().upper()
        if choice == "C":
            main_console()
            break
        elif choice == "W":
            main_tkinter()
            break
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter C, W, or Q.")


if __name__ == "__main__":
    main()