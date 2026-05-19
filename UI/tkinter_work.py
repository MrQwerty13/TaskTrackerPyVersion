#!/usr/bin/env python3
#
#   file name: tkinter_work.py
#   author: MrQwerty13 (Mikhail Pozur)
#   date of creation: 18.05.2026 (UTC+3)
#

"""
Tkinter windowed GUI for the Task Tracker application.
Uses a ttk.Treeview for a clear table display of tasks.
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from Keeper.task_keeper import TaskKeeper
from Repository.task_repo import TaskRepo


class TkinterWork:
    """
    GUI application for managing tasks with a table view (Treeview).
    """

    def __init__(self, file_name: str = "tasks.txt"):
        # Initialize backend
        self._task_repo = TaskRepo(file_name)
        self._keeper = TaskKeeper(self._task_repo.format_data())

        # Main window
        self._root = tk.Tk()
        self._root.title("Task Tracker")
        self._root.geometry("600x450")
        self._root.resizable(True, True)

        # Treeview (table) for tasks
        columns = ("ID", "Name", "Status")
        self._tree = ttk.Treeview(self._root, columns=columns, show="headings", selectmode="browse")
        self._tree.heading("ID", text="ID")
        self._tree.heading("Name", text="Name")
        self._tree.heading("Status", text="Status")
        self._tree.column("ID", width=60, anchor="center")
        self._tree.column("Name", width=350, anchor="w")
        self._tree.column("Status", width=100, anchor="center")
        self._tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self._root, orient=tk.VERTICAL, command=self._tree.yview)
        self._tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Button frame
        btn_frame = tk.Frame(self._root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Task", command=self._add_task, width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Remove Task", command=self._remove_task, width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Toggle Status", command=self._toggle_status, width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Exit", command=self._on_exit, width=12).pack(side=tk.LEFT, padx=5)

        # Optional: double-click a row to toggle its status
        self._tree.bind("<Double-1>", lambda event: self._toggle_status())

        # Load initial data
        self._refresh_tree()

    def run(self):
        """Start the Tkinter main loop."""
        self._root.mainloop()

    # ----------------------------------------------------------------------
    # GUI actions
    # ----------------------------------------------------------------------

    def _add_task(self):
        """Prompt for a task name and add it."""
        name = simpledialog.askstring("Add Task", "Enter task name:", parent=self._root)
        if name is None:
            return
        name = name.strip()
        if not name:
            messagebox.showwarning("Invalid Name", "Task name cannot be empty.")
            return

        if self._keeper.add_task(name):
            self._save_and_refresh()
        else:
            messagebox.showerror("Add Failed",
                                 f"Cannot add more than {TaskKeeper.MAX_TASKS} tasks.")

    def _remove_task(self):
        """Remove the selected task."""
        selected = self._tree.selection()
        if not selected:
            messagebox.showinfo("No Selection", "Please select a task to remove.")
            return

        task_id = int(self._tree.item(selected[0], "values")[0])
        if self._keeper.remove_task(task_id):
            self._save_and_refresh()
        else:
            messagebox.showerror("Error", f"Task {task_id} could not be removed.")

    def _toggle_status(self):
        """Toggle DONE/UNDONE for the selected task."""
        selected = self._tree.selection()
        if not selected:
            messagebox.showinfo("No Selection", "Please select a task to toggle.")
            return

        task_id = int(self._tree.item(selected[0], "values")[0])
        if self._keeper.change_task_status(task_id):
            self._save_and_refresh()
        else:
            messagebox.showerror("Error", f"Task {task_id} could not be toggled.")

    # ----------------------------------------------------------------------
    # Utility methods
    # ----------------------------------------------------------------------

    def _save_and_refresh(self):
        """Persist tasks to file and update the table."""
        self._task_repo.write_file(self._keeper.tasks())
        self._refresh_tree()

    def _refresh_tree(self):
        """Reload the Treeview from the keeper's task dictionary."""
        # Clear current items
        for item in self._tree.get_children():
            self._tree.delete(item)

        tasks = self._keeper.tasks()
        for task_id, task in sorted(tasks.items()):
            self._tree.insert("", tk.END, values=(task_id, task.name(), task.status().value))

    def _on_exit(self):
        """Save and close."""
        self._task_repo.write_file(self._keeper.tasks())
        self._root.destroy()