import time
import concurrent.futures
# Thread pull executor, it's best to use with context manager.

start = time.perf_counter()

def do_something(seconds : int) -> str:
    print(f"Sleep for {seconds} second(s)")
    time.sleep(seconds)
    return f"Done sleeping...{seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

    #  results = [executor.submit(do_something, sec) for sec in secs]
    
    #  for f in concurrent.futures.as_completed(results):
        #  print(f.result())
    #  f1 = executor.submit(do_something, 2) # function, parameter
    #  f2 = executor.submit(do_something, 2) # function, parameter
    
    #  print(f1.result())
    #  print(f2.result())

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')


