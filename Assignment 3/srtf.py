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
        processes.append({
            "name": name,
            "arrival": arrival,
            "burst": burst,
            "remaining": burst
        })
    return processes


def srtf(processes):
    n = len(processes)
    current_time = 0
    completed = 0

    while completed < n:
        available = [p for p in processes if p["arrival"] <= current_time and p["remaining"] > 0]

        if available:
            current_process = min(available, key=lambda p: p["remaining"])
            if "start" not in current_process:
                current_process["start"] = current_time

            current_process["remaining"] -= 1
            current_time += 1

            if current_process["remaining"] == 0:
                current_process["completion"] = current_time
                current_process["turnaround"] = current_process["completion"] - current_process["arrival"]
                current_process["waiting"] = current_process["turnaround"] - current_process["burst"]
                completed += 1
        else:
            current_time += 1

    return processes


def print_table(processes):
    print("\n{:<8} {:<8} {:<8} {:<8} {:<12} {:<8}".format(
        "Process", "Arrival", "Burst", "Start", "Completion", "Waiting"
    ))
    for p in processes:
        print("{:<8} {:<8} {:<8} {:<8} {:<12} {:<8}".format(
            p["name"], p["arrival"], p["burst"], p.get("start", 0), p["completion"], p["waiting"]
        ))

    avg_waiting = sum(p["waiting"] for p in processes) / len(processes)
    avg_turnaround = sum(p["turnaround"] for p in processes) / len(processes)

    print(f"\nAverage waiting time: {avg_waiting:.2f}")
    print(f"Average turnaround time: {avg_turnaround:.2f}")


if __name__ == "__main__":
    processes = read_processes()
    results = srtf(processes)
    print_table(results)
