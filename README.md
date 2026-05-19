# Task Tracker

A simple, dual‑interface task management application written in Python.  
Keep track of your daily tasks in either the terminal or a clean graphical window, with persistent storage in a plain text file.

---

## Features

- ✅ Add new tasks (up to 10)  
- ❌ Remove tasks by ID  
- ✓ Toggle status between **Done** (✓) and **Undone** (✕)  
- 💾 Automatic save to `tasks.txt` – no database required  
- 🖥️ Console interface with interactive menu  
- 🧩 Tkinter GUI with a resizable table view and double‑click to toggle  
- 🔀 Launcher that lets you choose your preferred interface at start  

---

## Requirements

- **Python 3.7+** (uses `dataclasses`, `pathlib`, and `tkinter`)
- No external libraries – everything is from the standard library.

---

## Installation & Running

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/task-tracker.git
   cd task-tracker
   ```

2. **Run the main launcher**
   ```bash
   python main.py
   ```
   You will be prompted to choose a view:
   - `C` – console mode
   - `W` – windowed (Tkinter) mode  
   - `Q` – quit

---

## Usage

### Console Interface

- The console displays all tasks in a simple list.
- Choose from the menu:
  1. Add a task
  2. Remove a task (by ID)
  3. Toggle status (by ID)
  4. Exit

### GUI (Tkinter)

- The table shows **ID**, **Name**, and **Status**.
- Buttons at the bottom: **Add Task**, **Remove Task**, **Toggle Status**, **Exit**.
- Double‑click a row to quickly toggle its status.
- Resize the window to see longer task names.

---

## File Structure

```
task-tracker/
├── main.py                   # Launcher (choose console or GUI)
├── Entities/
│   ├── task_item.py          # TaskItem class
│   └── task_enum.py          # TaskItemStatus enum
├── Keeper/
│   └── task_keeper.py        # TaskKeeper logic (max 10 tasks)
├── Repository/
│   └── task_repo.py          # File reading/writing (tasks.txt)
└── UI/
    ├── console_work.py       # Console interface
    └── tkinter_work.py       # Tkinter GUI interface
```

---

## How It Works

1. `TaskRepo` reads/writes tasks from a simple text file (`tasks.txt`) in the format:  
   `ID: 1 | NAME: Buy milk | STATUS: ✓`
2. `TaskKeeper` keeps tasks in memory, enforces the 10‑task limit, and reuses deleted IDs.
3. Both UIs call the same backend, so switching between console and GUI never loses data.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

Enjoy tracking your tasks! ☑️
