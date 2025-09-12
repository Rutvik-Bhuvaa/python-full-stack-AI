def infinite_chai():
    count = 1
    while True:
        yield f"Refill {count}"
        count +=1

refill = infinite_chai()
user = infinite_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user))