````markdown
# Linux Process Management Experiment

This project contains Python scripts that simulate Linux process creation and management using the `os` module.

## Project Overview

The experiment explores various aspects of process management in a Linux environment, including:

- **Creating child processes**
- **Executing commands using `exec()`**
- **Simulating zombie and orphan processes**
- **Inspecting process details from `/proc`**
- **Demonstrating process prioritization using `nice()`**

## Files

- **`task1_process_creation.py`** – Create and manage child processes.
- **`task2_exec_command.py`** – Execute Linux commands in child processes.
- **`task3_zombie_orphan.py`** – Simulate zombie and orphan processes.
- **`task4_inspect_proc.py`** – Inspect process information from `/proc`.
- **`task5_priority.py`** – Demonstrate process priority and CPU scheduling.

## Requirements

- Python 3
- A Linux environment (e.g., Ubuntu, WSL, or similar)

## How to Run

1. Open your terminal.
2. Run each script individually, for example:

   ```bash
   python3 task1_process_creation.py
````

3. Follow any prompts that appear on the screen.

## Notes

* **Task 3:** To observe zombie processes, open another terminal and run:

  ```bash
  ps -el | grep defunct
  ```

* These scripts rely on Linux-specific system calls and will not run natively in a Windows command prompt.

* You can use `Ctrl+C` to stop any long-running tasks.

---
