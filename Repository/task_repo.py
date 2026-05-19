#
#   file name: task_repo.py
#   author: MrQwerty13 (Mikhail Pozur)
#   date of creation: 18.05.2026 (UTC+3)
#

# Import all necessaries
from Entities.task_item import TaskItem
from Entities.task_enum import TaskItemStatus

import os


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
        if ".txt" in file_name:
            self.file_name = file_name
        else:
            os.system("touch tasks.txt")
            self.file_name = "tasks.txt"


    def read_file(self) -> list[str]:
        with open(self.file_name, "r") as file:
            return file.readlines()

    def write_file(self, data: dict[int, TaskItem]):
        with open(self.file_name, "w") as file:
            for key in data.keys():
                file.write(f"ID: {data[key].id()} | NAME: {data[key].name()} | STATUS: {data[key].status().value}\n")

    def format_data(self) -> dict[int, TaskItem]:
        to_format = self.read_file()

        formatted_data: dict[int, TaskItem] = {}

        for line in to_format:
            line = line.replace("\n", "")
            _id_str, _name_str, _status_str = line.split(" | ")

            _id = int(_id_str.replace("ID: ", ""))
            _name = (_name_str.replace("NAME: ", "")).replace("\n", "")
            _status = TaskItemStatus.DONE \
                if (_status_str.replace("Status: ", "") == TaskItemStatus.DONE.value) \
                else TaskItemStatus.UNDONE

            formatted_data[_id] = TaskItem(
                _id, _name, _status
            )

        return formatted_data