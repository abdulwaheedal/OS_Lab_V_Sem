#!/usr/bin/env python3

def allocate_memory(strategy, partitions, processes):
    print(f"\n{strategy.upper()}-FIT STRATEGY")
    print("-" * 45)

    part_copy = partitions.copy()
    allocation = [-1] * len(processes)

    print(f"Partitions: {part_copy}")
    print(f"Processes: {processes}\n")

    for i, process_size in enumerate(processes):
        index = -1

        if strategy == "first":
            for j, partition_size in enumerate(part_copy):
                if partition_size >= process_size:
                    index = j
                    break

        elif strategy == "best":
            best_fit = float("inf")
            for j, partition_size in enumerate(part_copy):
                if partition_size >= process_size and partition_size < best_fit:
                    best_fit = partition_size
                    index = j

        elif strategy == "worst":
            worst_fit = -1
            for j, partition_size in enumerate(part_copy):
                if partition_size >= process_size and partition_size > worst_fit:
                    worst_fit = partition_size
                    index = j

        if index != -1:
            allocation[i] = index
            part_copy[index] -= process_size
            print(f"Process {i+1} (size {process_size}) → Partition {index+1}")
            print(f"Remaining partitions: {part_copy}")
        else:
            print(f"Process {i+1} (size {process_size}) → Not allocated")

    return allocation


def main():
    print("=" * 55)
    print("CONTIGUOUS MEMORY ALLOCATION SIMULATION")
    print("=" * 55)

    partitions = list(map(int, input("Enter partition sizes (space-separated): ").split()))
    processes = list(map(int, input("Enter process sizes (space-separated): ").split()))

    print("\nInitial Configuration")
    print(f"Partitions: {partitions}")
    print(f"Processes: {processes}")

    for strategy in ["first", "best", "worst"]:
        allocate_memory(strategy, partitions, processes)


if __name__ == "__main__":
    main()
