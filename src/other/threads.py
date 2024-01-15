import threading
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

def t1():
    print(threading.current_thread().getName())

def t2():
    print(threading.current_thread().getName())

if __name__ == '__main__':
    task1 = Thread(target=t1)
    task2 = Thread(target=t2)

    task1.start()
    task2.start()

    task1.join()
    task2.join()

    pool = ThreadPoolExecutor(max_workers=2)
    pool.submit(t1)
    pool.submit(t2)

    pool.shutdown(wait=True)
