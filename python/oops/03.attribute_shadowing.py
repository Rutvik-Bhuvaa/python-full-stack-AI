class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)
print(cutting.strength)

cutting.temperature = "mild"
cutting.cup = "small"
print(f"After change: {cutting.temperature}")
print(f"Cup size is {cutting.cup}")
print(f"Direct look up for class: {Chai.temperature}")

# Attribute shadowing => If you delete any property of object and then you try to print then it fallback to the class from which the object is created and inherit that property
del cutting.temperature
print(cutting.temperature)
del cutting.cup
print(cutting.cup)  # Error because there is no fallback