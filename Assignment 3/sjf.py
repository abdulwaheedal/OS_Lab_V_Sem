def read_processes():
    n = int(input("Enter the number of processes: ").strip())
    processes = []
    for i in range(n):
        default_name = f"P{i+1}"
        line = input(f"Enter details for process {i+1} (name arrival burst) [e.g. {default_name} 0 5]: ").strip()
        parts = line.split()
        name = parts[0] if len(parts) >= 1 else default_name
        arrival = int(parts[1]) if len(parts) >= 2 else 0
        burst = int(parts[2]) if len(parts) >= 3 else 0
        processes.append({"name": name, "arrival": arrival, "burst": burst})
    return processes


def sjf(processes):
    processes = sorted(processes, key=lambda p: p["arrival"])
    completed = []
    current_time = 0

    while processes:
        available = [p for p in processes if p["arrival"] <= current_time]
        if not available:
            current_time = processes[0]["arrival"]
            continue

        process = min(available, key=lambda x: x["burst"])
        processes.remove(process)
        process["start"] = max(current_time, process["arrival"])
        process["completion"] = process["start"] + process["burst"]
        process["turnaround"] = process["completion"] - process["arrival"]
        process["waiting"] = process["turnaround"] - process["burst"]
        current_time = process["completion"]
        completed.append(process)

    return completed


def print_table(processes):
    print("\n{:<8} {:<8} {:<8} {:<8} {:<12} {:<8}".format(
        "Process", "Arrival", "Burst", "Start", "Completion", "Waiting"
    ))
    for p in processes:
        print("{:<8} {:<8} {:<8} {:<8} {:<12} {:<8}".format(
            p["name"], p["arrival"], p["burst"], p["start"], p["completion"], p["waiting"]
        ))

    avg_waiting = sum(p["waiting"] for p in processes) / len(processes)
    avg_turnaround = sum(p["turnaround"] for p in processes) / len(processes)

    print(f"\nAverage waiting time: {avg_waiting:.2f}")
    print(f"Average turnaround time: {avg_turnaround:.2f}")


if __name__ == "__main__":
    processes = read_processes()
    results = sjf(processes)
    print_table(results)
