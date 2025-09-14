from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"End of {name} chai brewing")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai maker #{i+1}", ))
        for i in range(3)
    ]

    for p in chai_makers:
        p.start()

    # join each process immediately after starting
    for p in chai_makers:
        p.join()
        print(f"{p.name} has finished brewing")   # <-- prints as soon as one ends

    print("All chai served")
