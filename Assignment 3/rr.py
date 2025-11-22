def read_processes():
    n = int(input("Enter the number of processes: ").strip())
    quantum = int(input("Enter the time quantum: ").strip())
    processes = []
    for i in range(n):
        default_name = f"P{i+1}"
        line = input(f"Enter details for process {i+1} (name arrival burst) [e.g. {default_name} 0 5]: ").strip()
        parts = line.split()
        name = parts[0] if len(parts) >= 1 else default_name
        arrival = int(parts[1]) if len(parts) >= 2 else 0
        burst = int(parts[2]) if len(parts) >= 3 else 0
        processes.append({
            "name": name,
            "arrival": arrival,
            "burst": burst,
            "remaining": burst
        })
    return processes, quantum


def round_robin(processes, quantum):
    time = 0
    queue = []
    completed = []
    processes = sorted(processes, key=lambda p: p["arrival"])

    while processes or queue:
        while processes and processes[0]["arrival"] <= time:
            queue.append(processes.pop(0))
        if not queue:
            time = processes[0]["arrival"]
            continue

        process = queue.pop(0)
        if "start" not in process:
            process["start"] = time

        run_time = min(process["remaining"], quantum)
        process["remaining"] -= run_time
        time += run_time

        while processes and processes[0]["arrival"] <= time:
            queue.append(processes.pop(0))

        if process["remaining"] > 0:
            queue.append(process)
        else:
            process["completion"] = time
            process["turnaround"] = process["completion"] - process["arrival"]
            process["waiting"] = process["turnaround"] - process["burst"]
            completed.append(process)

    return completed


def print_table(processes):
    print("\n{:<8} {:<8} {:<8} {:<12} {:<8}".format(
        "Process", "Arrival", "Burst", "Completion", "Waiting"
    ))
    for p in processes:
        print("{:<8} {:<8} {:<8} {:<12} {:<8}".format(
            p["name"], p["arrival"], p["burst"], p["completion"], p["waiting"]
        ))

    avg_waiting = sum(p["waiting"] for p in processes) / len(processes)
    avg_turnaround = sum(p["turnaround"] for p in processes) / len(processes)

    print(f"\nAverage waiting time: {avg_waiting:.2f}")
    print(f"Average turnaround time: {avg_turnaround:.2f}")


if __name__ == "__main__":
    processes, quantum = read_processes()
    results = round_robin(processes, quantum)
    print_table(results)
