import threading
import asyncio

def turn_async(function):
    def run_as_async():
        asyncio.run(function())
    return run_as_async

@turn_async
async def worker_1():
    try:
        print('Thread 1 worker function start')
        print('Thread 1 worker awaiting 3 seg...')
        await asyncio.sleep(3)
        print('Thread 1 worker function finish')
    except Exception as error:
        print(f">>> ERROR IN THREAD 1: \n{error}")

@turn_async
async def worker_2():
    try:
        print('Thread 2 worker function start')
        print('Thread 2 worker awaiting 6 seg...')
        await asyncio.sleep(6)
        print('Thread 2 worker function finish')
    except Exception as error:
        print(f">>> ERROR IN THREAD 1: \n{error}")

@turn_async
async def worker_3():
    try:
        print('Thread 3 worker function start')
        print('Thread 3 worker awaiting 9 seg...')
        await asyncio.sleep(9)
        print('Thread 3 worker function finish')
    except Exception as error:
        print(f">>> ERROR IN THREAD 1: \n{error}")

def main():
    try:
        thread_1 = threading.Thread(target = worker_1)
        thread_2 = threading.Thread(target = worker_2)
        thread_3 = threading.Thread(target = worker_3)
        thread_1.start()
        thread_2.start()
        thread_3.start()
    except Exception as error:
        print(f"ERROR: At main \n{error}")

if __name__ == '__main__':
    main()
