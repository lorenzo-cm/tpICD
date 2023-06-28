import threading
import time

def func():
    time.sleep(5)


t= threading.Thread(target=func)
t1= threading.Thread(target=func)

start = time.perf_counter()

t.start()
t1.start()
print('Startei')
t.join()
t1.join()
print('depois do join')

finish = time.perf_counter()
print(f'Time taken: {finish - start} ')