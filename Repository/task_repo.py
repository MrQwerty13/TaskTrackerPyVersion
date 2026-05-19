#
#   file name: task_repo.py
#   author: MrQwerty13 (Mikhail Pozur)
#   date of creation: 18.05.2026 (UTC+3)
#

# Import all necessaries
from Entities.task_item import TaskItem
from Entities.task_enum import TaskItemStatus

from pathlib import Path


class TaskRepo:
    """
        Class TaskRepo:
            Attributes:
                file_name: file name of tasks

            Methods:
                read_file: read file from file
                    :argument - None
                    :return - list of all tasks

                write_file: write tasks to file
                    :argument - dictionary of tasks
                    :return - None

                format_data: format data
                    :argument - None
                    :return - dictionary of tasks
    """
    def __init__(self, file_name: str):
        # Add a default .txt extension if none is present
        if "." not in file_name:
            file_name += ".txt"
        self.file_name = file_name
        # Ensure the file exists (creates empty file if missing)
        Path(self.file_name).touch(exist_ok=True)

    def read_file(self) -> list[str]:
        """Return all lines from the file, or an empty list if the file is empty."""
        try:
            with open(self.file_name, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            # Should not happen because __init__ creates the file, but just in case
            return []

    def write_file(self, data: dict[int, TaskItem]):
        """Write tasks to the file in a consistent format."""
        with open(self.file_name, "w") as file:
            for key in data.keys():
                task = data[key]
                file.write(f"ID: {task.id()} | NAME: {task.name()} | STATUS: {task.status().value}\n")

    def format_data(self) -> dict[int, TaskItem]:
        """Parse the file and return a dictionary of TaskItem objects."""
        lines = self.read_file()
        formatted_data: dict[int, TaskItem] = {}

        for line in lines:
            line = line.strip()
            if not line:          # skip empty lines
                continue

            try:
                # Split by the known delimiter
                parts = line.split(" | ")
                if len(parts) != 3:
                    continue     # skip malformed lines

                # Extract fields safely using the colon separator
                _id_str   = parts[0].split(": ", 1)[1]
                _name_str = parts[1].split(": ", 1)[1]
                _status_str = parts[2].split(": ", 1)[1]

                _id = int(_id_str)
                _name = _name_str.strip()
                _status = TaskItemStatus.DONE if _status_str == TaskItemStatus.DONE.value else TaskItemStatus.UNDONE

                formatted_data[_id] = TaskItem(_id, _name, _status)
            except (IndexError, ValueError):
                # Skip lines that cannot be parsed
                continue

        return formatted_data