import time
import threading

start = time.perf_counter()

'''
def do_something():
    print("Sleep for 1 second...")
    time.sleep(1)
    print("Done sleeping...")


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

# When we run this script, it will output Finished in 0 second(s), 
# because the thread will execute, and the remaining lines will execute too.
# Essentially it means that, before do_something function is executed, 
# print finish and print are executed.
# If we want to run these statements after the thread execution is finished, 
# we need join, sth like pthread_join in C.
'''

# The same function, but we loop over 100 times.
# If running synchronously, it will take 100 seconds.
# Using threading, it takes ~1s only. (1.05 in my machine).
# Now, adding arguments..

def do_something(seconds: int) -> None:
    print(f'Sleep for {seconds} second(s)...')
    time.sleep(seconds)
    print("Done sleeping...")

threads = []

for _ in range(100):
    t = threading.Thread(target=do_something, args = [2])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')


