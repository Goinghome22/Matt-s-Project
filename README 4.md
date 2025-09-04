# 6-Month • Semester 1 — Unix, Python, and Automation

This semester focuses on hands-on Unix usage, iterative Python projects, and lightweight security automation.

## Modules

- Unix 1 (`unix_1`)
  - Key file: `unix_notes.txt` — documents commands, options, editors, permissions, environment, and aliases used during the budgeting project.

- Unix 2 (`unix_2`)
  - Continuation of shell usage with directory management, backups, grep, and environment concepts.

- Python 2 (`python_2`)
  - CLI Budget Calculator: `vacation_budget.py`
    - Prompts for flight/hotel/food/transport, totals expenses, and reports if in budget.
  - GUI Budget Calculator: `import tkinter as tk.py`
    - Tkinter-based inputs and a popup summary; also prints an expense breakdown to terminal.

- Logic 1 (`logic_1`)
  - Planning assets and outlines to support algorithmic thinking.

- File Integrity Monitor (`FileIntegrityMonitor`)
  - Scripts: `file_integrity_monitor.py`, example input `example_file.txt`.
  - Behavior: Generates MD5/SHA1 hashes at intervals, compares to prior run, and logs to `file_integrity_report.txt`.

## How to Run

Requirements: Python 3

- CLI Budget Calculator
  ```bash
  cd "python_2"
  python3 vacation_budget.py
  ```

- GUI Budget Calculator (Tkinter)
  ```bash
  cd "python_2"
  python3 "import tkinter as tk.py"
  ```

- File Integrity Monitor
  ```bash
  cd "FileIntegrityMonitor"
  # (Optional) edit file_integrity_monitor.py to set file_to_monitor
  python3 file_integrity_monitor.py
  ```

## Notes

- On macOS, you may need to allow Python to open GUI windows for Tkinter.
- The integrity monitor writes `file_integrity_report.txt` in its working directory. 