value = 13
rem = value % 5

if rem:
    print(f"Not divisible, remainder is {rem}")

# using walrus operator
value = 13

if (rem := (value % 5)):
    print(f"Not divisible, remainder is {rem}")

# another example

available_cups_size = ["small", "medium", "large"]

if (available := input("Enter the serving size (small/medium/large): ").lower()) in available_cups_size:
    print(f"Serving {available} chai")
else:
    print(f"{available} size is not available currently")


flavours = ["masala", "ginger", "green", "mint"]

print("Available flavours: ", flavours)

while (flavour := input("Choose any flavour from above list: ").lower()) not in flavours:
    print(f"{flavour} chai is not available")

print(f"You will get the {flavour} chai in some minutes")