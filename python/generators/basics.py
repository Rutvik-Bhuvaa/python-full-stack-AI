def serve_chai():
    yield "Cup 1: Masala chai"
    yield "Cup 2: Ginger chai"
    yield "Cup 3: Elaichi chai"

stall = serve_chai()

for cup in stall:
    print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

print(get_chai_list())      # ['Cup 1', 'Cup 2', 'Cup 3']    

# Generator

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()

print(chai) # <generator object get_chai_gen at 0x00000271F2CD4A90>
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai)) # gives error


