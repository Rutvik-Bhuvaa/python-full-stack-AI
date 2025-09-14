import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing")
    count = 0
    for _ in range(100_000_000):
        count +=1
    print(f"{threading.current_thread().name} finished brewing")


first_thread = threading.Thread(target=brew_chai)
second_thread = threading.Thread(target=brew_chai)

start = time.time()
first_thread.start()
second_thread.start()

first_thread.join()
second_thread.join()
end = time.time()

print(f"total time taken {end - start:.2f} seconds")