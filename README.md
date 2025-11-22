# 🧠 Operating Systems Lab (V Semester)

**Developer:** Abdul Waheed Al Faaiz
**Course:** Operating Systems Laboratory (V Sem)
**Language:** Python 3
**Platform:** Linux / Ubuntu / WSL / Kali Linux

---

## 📁 Repository Structure

```
abdulwaheedal-os_lab_v_sem/
├── README.md
├── Assignment 1/
│   ├── task1_OSLAB.py
│   ├── task2_OSLAB.py
│   ├── task3_OSLAB.py
│   ├── task4_OSLAB.py
│   └── task5_OSLAB.py
├── Assignment 2/
│   ├── FullCode.py
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   └── task4.py
├── Assignment 3/
│   ├── fcfs.py
│   ├── memory_allocation.py
│   ├── mft_mvt.py
│   ├── rr.py
│   ├── sjf.py
│   └── srtf.py
└── Assignment 4/
    ├── batchRun.py
    ├── batchRunOutput.txt
    ├── task2_startup.py
    ├── task2Output.txt
    ├── task2System_log.txt
    ├── task3_system.py
    ├── task3Output.txt
    ├── task4_vm_detection.py
    └── task4Output.txt
```

---

## 🎯 Overview

This repository contains a collection of **Operating Systems lab experiments** implemented in **Python**, focusing on:

* Linux **process management**
* **CPU scheduling algorithms**
* **Memory management techniques**
* **System programming** and **virtualization detection**

Each assignment demonstrates a different OS concept through hands-on Python simulations.

| Assignment | Topic                              | Core Concepts                                              |
| ---------- | ---------------------------------- | ---------------------------------------------------------- |
| **1**      | Linux Process Management           | Fork, exec, zombies/orphans, `/proc`, nice()               |
| **2**      | Multiprocessing & Logging          | System startup/shutdown, modular multiprocessing           |
| **3**      | CPU Scheduling & Memory Allocation | FCFS, SJF, SRTF, RR, MFT, MVT, First/Best/Worst Fit        |
| **4**      | System Operations & Virtualization | Batch execution, inter-process communication, VM detection |

---

## ⚙️ Requirements

* Python **3.8+**
* Linux environment (Ubuntu, Kali, or WSL)
* Terminal access

Optional tools (for VM detection):

```bash
sudo apt install dmidecode lscpu
```

---

## 🧩 Assignment 1 – Linux Process Management

This assignment explores how processes work in Linux using the `os` module.

### 📜 Files

| File             | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| `task1_OSLAB.py` | Create multiple child processes using `os.fork()`             |
| `task2_OSLAB.py` | Execute Linux commands in child processes using `os.execvp()` |
| `task3_OSLAB.py` | Simulate **Zombie** and **Orphan** processes                  |
| `task4_OSLAB.py` | Inspect process information from `/proc/<pid>`                |
| `task5_OSLAB.py` | Demonstrate **priority scheduling** using `nice()`            |

### ▶️ Example Usage

```bash
python3 task1_OSLAB.py
Enter number of child processes to create: 3
```

**To observe zombies:**

```bash
ps -el | grep defunct
```

📌 **Note:**
These programs rely on Linux system calls and will not run on Windows CMD.

---

## ⚙️ Assignment 2 – Multiprocessing & System Simulation

This assignment demonstrates how to simulate **system boot and shutdown** using Python’s `multiprocessing` and `logging` modules.

### 📜 Files

| File          | Description                                       |
| ------------- | ------------------------------------------------- |
| `task1.py`    | Configures process logging                        |
| `task2.py`    | Defines the simulated system process              |
| `task3.py`    | Starts multiple processes                         |
| `task4.py`    | Waits for all processes to terminate              |
| `FullCode.py` | Combines all tasks into a complete working system |

### ▶️ Example Run

```bash
python3 FullCode.py
```

**Output:**

```
System Starting...
System Shutdown.
```

**Log file (`process_log.txt`):**

```
2025-11-22 14:12:05 - Process-1 - Process-1 started
2025-11-22 14:12:07 - Process-1 - Process-1 ended
```

---

## 🧮 Assignment 3 – CPU Scheduling & Memory Management

Implements major **CPU scheduling** and **memory management** algorithms used in operating systems.

---

### ⚡ CPU Scheduling Algorithms

| File      | Algorithm                     | Description                                      |
| --------- | ----------------------------- | ------------------------------------------------ |
| `fcfs.py` | First Come First Serve        | Non-preemptive scheduling based on arrival order |
| `sjf.py`  | Shortest Job First            | Picks process with shortest burst time           |
| `srtf.py` | Shortest Remaining Time First | Preemptive version of SJF                        |
| `rr.py`   | Round Robin                   | Time-sharing with defined time quantum           |

#### ▶️ Example Run (FCFS)

```bash
python3 fcfs.py
Enter the number of processes: 3
Enter details for process 1 (name arrival burst): P1 0 5
Enter details for process 2 (name arrival burst): P2 1 3
Enter details for process 3 (name arrival burst): P3 2 8
```

**Output:**

```
Process  Arrival  Burst  Start  Completion  Waiting
P1       0        5      0      5           0
P2       1        3      5      8           4
P3       2        8      8      16          6

Average waiting time: 3.33
Average turnaround time: 7.33
```

---

### 💾 Memory Management Techniques

| File                   | Technique                      | Description                                 |
| ---------------------- | ------------------------------ | ------------------------------------------- |
| `memory_allocation.py` | First Fit, Best Fit, Worst Fit | Simulates contiguous memory allocation      |
| `mft_mvt.py`           | MFT (Fixed) & MVT (Variable)   | Demonstrates memory partitioning strategies |

#### ▶️ Example Run (First/Best/Worst Fit)

```bash
python3 memory_allocation.py
Enter partition sizes: 100 500 200 300 600
Enter process sizes: 212 417 112 426
```

#### ▶️ Example Run (MFT/MVT)

```bash
python3 mft_mvt.py
Enter total memory size: 1000
Enter partition size: 200
```

---

## 💻 Assignment 4 – System Operations & Virtual Machine Detection

Demonstrates **system-level operations** such as batch execution, system logging, **interprocess communication**, and **VM detection**.

### 📜 Files

| File                    | Description                                         |
| ----------------------- | --------------------------------------------------- |
| `batchRun.py`           | Executes multiple Python scripts sequentially       |
| `task2_startup.py`      | Simulates system boot and shutdown with logs        |
| `task3_system.py`       | Demonstrates interprocess communication using pipes |
| `task4_vm_detection.py` | Detects virtual machines and prints system details  |
| `*.txt`                 | Output logs for verification                        |

---

### ▶️ Example Outputs

#### 🧩 `batchRun.py`

```
Executing script1.py...
Script 1 count: 0
Script 1 count: 1
Script 1 count: 2
```

#### 🧩 `task3_system.py`

```
Child received: Hello from parent
```

#### 🧩 `task4_vm_detection.py`

```
==== System Details ====
Kernel Version: 6.12.33+kali-amd64
User: faaizChoudhary_47
Virtual Machine Detected
 - CPU flags show 'hypervisor' → running in VM.
```

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/abdulwaheedal-os_lab_v_sem.git
   cd abdulwaheedal-os_lab_v_sem
   ```

2. Navigate to any assignment:

   ```bash
   cd "Assignment 1"
   python3 task1_OSLAB.py
   ```

3. Follow on-screen instructions for each program.

---

## 🧾 Notes

* Scripts rely on **Linux-specific system calls** (`fork`, `exec`, `/proc`).
* Use `Ctrl+C` to stop long-running tasks.
* Output logs (`*.txt`) show verified test results.
* For virtualization detection, run with **sudo** for complete info.

---

## 🧑‍💻 Developer

**Name:** Abdul Waheed Al Faaiz
**Course:** B.Tech – Computer Science (V Semester)
**Subject:** Operating Systems Laboratory

---

## 📘 Learning Outcomes

✅ Understand **Linux process creation and management**
✅ Implement **classic CPU scheduling algorithms**
✅ Simulate **memory allocation techniques**
✅ Explore **system calls, process control, and logging**
✅ Detect and analyze **virtual machine environments**

---

### ⭐ Final Note

This repository serves as a **comprehensive reference for OS Lab experiments**, providing both **theoretical understanding** and **practical Python implementations** for real-world system concepts.

---

