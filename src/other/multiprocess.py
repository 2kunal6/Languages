from multiprocessing import Process
import os


# pid (process id is same in multithreading because child threads belong to the same process but different in multiprocessing)
def t1():
    print(os.getpid())

def t2():
    print(os.getpid())

if __name__ == '__main__':
    task1 = Process(target=t1)
    task2 = Process(target=t2)

    task1.start()
    task2.start()

    task1.join()
    task2.join()

    '''pool = ThreadPoolExecutor(max_workers=2)
    pool.submit(t1)
    pool.submit(t2)

    pool.shutdown(wait=True)'''
