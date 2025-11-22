#!/usr/bin/env python3

def MFT_simulation():
    print("=" * 55)
    print("MFT (FIXED PARTITIONING) SIMULATION")
    print("=" * 55)
    
    mem_size = int(input("Enter total memory size: "))
    part_size = int(input("Enter partition size: "))
    
    num_partitions = mem_size // part_size
    internal_fragmentation = 0
    allocated = 0
    
    print(f"\nMemory divided into {num_partitions} partitions of size {part_size}")
    print(f"Total memory: {mem_size}")
    print(f"Usable memory: {num_partitions * part_size}")
    print(f"Memory lost to internal fragmentation: {mem_size - (num_partitions * part_size)}")
    
    n = int(input("\nEnter number of processes: "))
    
    print("\nProcess Allocation")
    print("-" * 35)
    
    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))
        
        if psize <= part_size and allocated < num_partitions:
            print(f"  Process {i+1} (size {psize}) → Allocated")
            internal_fragmentation += (part_size - psize)
            allocated += 1
        elif allocated >= num_partitions:
            print(f"  Process {i+1} (size {psize}) → No partition available")
        else:
            print(f"  Process {i+1} (size {psize}) → Too large (rejected)")
    
    print("\nSummary")
    print("-" * 35)
    print(f"Total processes: {n}")
    print(f"Allocated: {allocated}")
    print(f"Internal fragmentation: {internal_fragmentation}")
    avg_frag = internal_fragmentation / allocated if allocated > 0 else 0
    print(f"Average fragmentation per partition: {avg_frag:.2f}")


def MVT_simulation():
    print("\n" + "=" * 55)
    print("MVT (VARIABLE PARTITIONING) SIMULATION")
    print("=" * 55)
    
    mem_size = int(input("Enter total memory size: "))
    available_memory = mem_size
    allocated = 0
    
    print(f"\nInitial available memory: {available_memory}")
    n = int(input("\nEnter number of processes: "))
    
    print("\nProcess Allocation")
    print("-" * 35)
    
    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))
        
        if psize <= available_memory:
            print(f"  Process {i+1} (size {psize}) → Allocated")
            available_memory -= psize
            allocated += 1
            print(f"    Remaining memory: {available_memory}")
        else:
            print(f"  Process {i+1} (size {psize}) → Insufficient memory (rejected)")
    
    print("\nSummary")
    print("-" * 35)
    print(f"Total processes: {n}")
    print(f"Allocated: {allocated}")
    print(f"Remaining memory (external fragmentation): {available_memory}")
    utilization = ((mem_size - available_memory) / mem_size) * 100
    print(f"Memory utilization: {utilization:.2f}%")


def main():
    print("MEMORY MANAGEMENT TECHNIQUES SIMULATION")
    print("1. MFT (Fixed Partitioning)")
    print("2. MVT (Variable Partitioning)")
    print("3. Both Techniques")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == '1':
        MFT_simulation()
    elif choice == '2':
        MVT_simulation()
    elif choice == '3':
        MFT_simulation()
        MVT_simulation()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
