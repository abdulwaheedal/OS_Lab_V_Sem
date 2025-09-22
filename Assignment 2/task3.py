import multiprocessing

if __name__ == '__main__':
    print("System Starting...")

    # Create two processes
    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))

    # Start both processes
    p1.start()
    p2.start()
