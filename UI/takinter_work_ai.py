# Modernized `tkinter_work.py`


#!/usr/bin/env python3
#
#   file name: tkinter_work.py
#   author: MrQwerty13 (Mikhail Pozur)
#   redesigned GUI: ChatGPT
#   date of redesign: 20.05.2026
#

"""
Modern Tkinter GUI for the Task Tracker application.
Backend logic is fully preserved.
Only the GUI/UX layer was redesigned.
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from Keeper.task_keeper import TaskKeeper
from Repository.task_repo import TaskRepo


class TkinterWorkAI:
    """
    Modern GUI application for managing tasks.
    """

    BG_COLOR = "#1e1f26"
    SECONDARY_BG = "#2b2d3a"
    CARD_COLOR = "#313446"
    ACCENT_COLOR = "#6c63ff"
    SUCCESS_COLOR = "#3ecf8e"
    TEXT_COLOR = "#f5f5f5"
    MUTED_TEXT = "#b0b3c0"

    def __init__(self, file_name: str = "tasks.txt"):
        # ------------------------------------------------------------------
        # Backend initialization (UNCHANGED)
        # ------------------------------------------------------------------
        self._task_repo = TaskRepo(file_name)
        self._keeper = TaskKeeper(self._task_repo.format_data())

        # ------------------------------------------------------------------
        # Main window
        # ------------------------------------------------------------------
        self._root = tk.Tk()
        self._root.title("Task Tracker")
        self._root.geometry("850x550")
        self._root.minsize(700, 450)
        self._root.configure(bg=self.BG_COLOR)

        # ------------------------------------------------------------------
        # Style configuration
        # ------------------------------------------------------------------
        self._style = ttk.Style()
        self._style.theme_use("clam")

        self._style.configure(
            "Treeview",
            background=self.CARD_COLOR,
            foreground=self.TEXT_COLOR,
            fieldbackground=self.CARD_COLOR,
            rowheight=38,
            borderwidth=0,
            font=("SF Pro Display", 11)
        )

        self._style.configure(
            "Treeview.Heading",
            background=self.ACCENT_COLOR,
            foreground="white",
            relief="flat",
            font=("SF Pro Display", 11, "bold")
        )

        self._style.map(
            "Treeview",
            background=[("selected", self.ACCENT_COLOR)],
            foreground=[("selected", "white")]
        )

        self._style.configure(
            "Vertical.TScrollbar",
            background=self.SECONDARY_BG,
            troughcolor=self.BG_COLOR,
            bordercolor=self.BG_COLOR,
            arrowcolor="white"
        )

        # ------------------------------------------------------------------
        # Header
        # ------------------------------------------------------------------
        header_frame = tk.Frame(self._root, bg=self.BG_COLOR)
        header_frame.pack(fill="x", padx=20, pady=(20, 10))

        title_label = tk.Label(
            header_frame,
            text="📋 Task Tracker",
            font=("SF Pro Display", 24, "bold"),
            bg=self.BG_COLOR,
            fg=self.TEXT_COLOR
        )
        title_label.pack(anchor="w")

        subtitle_label = tk.Label(
            header_frame,
            text="Simple and modern task management",
            font=("SF Pro Display", 11),
            bg=self.BG_COLOR,
            fg=self.MUTED_TEXT
        )
        subtitle_label.pack(anchor="w", pady=(4, 0))

        # ------------------------------------------------------------------
        # Main card container
        # ------------------------------------------------------------------
        container = tk.Frame(
            self._root,
            bg=self.CARD_COLOR,
            highlightthickness=0,
            bd=0
        )
        container.pack(fill="both", expand=True, padx=20, pady=10)

        # ------------------------------------------------------------------
        # Stats section
        # ------------------------------------------------------------------
        stats_frame = tk.Frame(container, bg=self.CARD_COLOR)
        stats_frame.pack(fill="x", padx=20, pady=(20, 10))

        self._stats_label = tk.Label(
            stats_frame,
            text="0 tasks",
            font=("SF Pro Display", 11, "bold"),
            bg=self.CARD_COLOR,
            fg=self.SUCCESS_COLOR
        )
        self._stats_label.pack(anchor="w")

        # ------------------------------------------------------------------
        # Treeview frame
        # ------------------------------------------------------------------
        tree_frame = tk.Frame(container, bg=self.CARD_COLOR)
        tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("ID", "Name", "Status")

        self._tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        # Headings
        self._tree.heading("ID", text="ID")
        self._tree.heading("Name", text="Task")
        self._tree.heading("Status", text="Status")

        # Columns
        self._tree.column("ID", width=80, anchor="center")
        self._tree.column("Name", width=500, anchor="w")
        self._tree.column("Status", width=140, anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            tree_frame,
            orient=tk.VERTICAL,
            command=self._tree.yview
        )

        self._tree.configure(yscrollcommand=scrollbar.set)

        self._tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # ------------------------------------------------------------------
        # Bottom controls
        # ------------------------------------------------------------------
        controls_frame = tk.Frame(container, bg=self.CARD_COLOR)
        controls_frame.pack(fill="x", padx=20, pady=(10, 20))

        self._create_button(
            controls_frame,
            text="➕ Add Task",
            command=self._add_task,
            color="#FFFFFF"
        ).pack(side="left", padx=5)

        self._create_button(
            controls_frame,
            text="🗑 Remove",
            command=self._remove_task,
            color="#FFFFFF"
        ).pack(side="left", padx=5)

        self._create_button(
            controls_frame,
            text="🔄 Toggle Status",
            command=self._toggle_status,
            color="#059669"
        ).pack(side="left", padx=5)

        self._create_button(
            controls_frame,
            text="🚪 Exit",
            command=self._on_exit,
            color="#6b7280"
        ).pack(side="right", padx=5)

        # Double-click to toggle task status
        self._tree.bind("<Double-1>", lambda event: self._toggle_status())

        # Load tasks
        self._refresh_tree()

    # ----------------------------------------------------------------------
    # UI helper methods
    # ----------------------------------------------------------------------

    def _create_button(self, parent, text, command, color):
        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=18,
            pady=10,
            cursor="hand2",
            font=("SF Pro Display", 10, "bold")
        )

    # ----------------------------------------------------------------------
    # Main loop
    # ----------------------------------------------------------------------

    def run(self):
        """Start Tkinter main loop."""
        self._root.mainloop()

    # ----------------------------------------------------------------------
    # GUI actions
    # ----------------------------------------------------------------------

    def _add_task(self):
        """Prompt for a task name and add it."""

        name = simpledialog.askstring(
            "Add Task",
            "Enter task name:",
            parent=self._root
        )

        if name is None:
            return

        name = name.strip()

        if not name:
            messagebox.showwarning(
                "Invalid Name",
                "Task name cannot be empty."
            )
            return

        if self._keeper.add_task(name):
            self._save_and_refresh()
        else:
            messagebox.showerror(
                "Add Failed",
                f"Cannot add more than {TaskKeeper.MAX_TASKS} tasks."
            )

    def _remove_task(self):
        """Remove selected task."""

        selected = self._tree.selection()

        if not selected:
            messagebox.showinfo(
                "No Selection",
                "Please select a task to remove."
            )
            return

        task_id = int(self._tree.item(selected[0], "values")[0])

        confirm = messagebox.askyesno(
            "Remove Task",
            f"Are you sure you want to remove task #{task_id}?"
        )

        if not confirm:
            return

        if self._keeper.remove_task(task_id):
            self._save_and_refresh()
        else:
            messagebox.showerror(
                "Error",
                f"Task {task_id} could not be removed."
            )

    def _toggle_status(self):
        """Toggle DONE/UNDONE for selected task."""

        selected = self._tree.selection()

        if not selected:
            messagebox.showinfo(
                "No Selection",
                "Please select a task to toggle."
            )
            return

        task_id = int(self._tree.item(selected[0], "values")[0])

        if self._keeper.change_task_status(task_id):
            self._save_and_refresh()
        else:
            messagebox.showerror(
                "Error",
                f"Task {task_id} could not be toggled."
            )

    # ----------------------------------------------------------------------
    # Utility methods
    # ----------------------------------------------------------------------

    def _save_and_refresh(self):
        """Save tasks and refresh table."""

        self._task_repo.write_file(self._keeper.tasks())
        self._refresh_tree()

    def _refresh_tree(self):
        """Refresh Treeview from backend data."""

        for item in self._tree.get_children():
            self._tree.delete(item)

        tasks = self._keeper.tasks()

        done_count = 0

        for task_id, task in sorted(tasks.items()):
            status = task.status().value

            if "DONE" in status.upper():
                done_count += 1

            item = self._tree.insert(
                "",
                tk.END,
                values=(task_id, task.name(), status)
            )

            if "DONE" in status.upper():
                self._tree.item(item, tags=("done",))
            else:
                self._tree.item(item, tags=("undone",))

        self._tree.tag_configure(
            "done",
            foreground=self.SUCCESS_COLOR
        )

        self._tree.tag_configure(
            "undone",
            foreground=self.TEXT_COLOR
        )

        total = len(tasks)

        self._stats_label.config(
            text=f"{total} tasks • {done_count} completed"
        )

    def _on_exit(self):
        """Save tasks and close app."""

        self._task_repo.write_file(self._keeper.tasks())
        self._root.destroy()

