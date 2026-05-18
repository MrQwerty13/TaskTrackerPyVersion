#
#   file name: main.py
#   author: MrQwerty13 (Mikhail Pozur)
#   date of creation: 18.05.2026 (UTC+3)
#

# Import all necessaries
from UI.console_work import ConsoleWork


task_tracker = ConsoleWork(True, "tasks.txt")
task_tracker.run()