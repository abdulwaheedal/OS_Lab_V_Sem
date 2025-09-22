import multiprocessing

if __name__ == '__main__':
    print("System Starting...")

    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))

    p1.start()
    p2.start()
