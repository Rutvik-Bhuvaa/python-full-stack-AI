def make_chai():
    return "Here is your masala chai"

print(make_chai())

# another example 
def make_chai_2():
    return "Here is your green chai"

return_value = make_chai_2()
print(return_value)

# another example
def make_chai_3():
    print("Here is your oolong chai")

return_val = make_chai_3()
print(return_val)

# another example - Return early from the function
def chai_status(cups_left):
    if cups_left == 0:
        return "Chai is over"
    return "Chai is ready"
    print("Chai") # return early from the function

print(chai_status(0))
print(chai_status(1))

# another example - returning multiple  values
def chai_report():
    return 100, 20 # sold, remaining

sold, remaining = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)

def chai_reports():
    return 100, 20, 10

one, two, _ = chai_reports()
print("One: ", one)
print("Two: ", two)