#
#   file name: task_item_atributies.py
#   author: MrQwerty13 (Mikhail Pozur)
#   date of creation: 18.05.2026 (UTC+3)
#

# Import all necessaries
from enum import Enum


class TaskItemStatus(Enum):
    """
        Task Item Status:
            Available options:
            — Done = ✓
            — Undone = ✕
    """
    DONE = "✓"
    UNDONE = "✕"