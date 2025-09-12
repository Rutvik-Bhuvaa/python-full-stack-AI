# zip is used when we want to iterate on two different iterables at the same time

names = ["rutvik", "diya", "meera", "john"]
bills = [500, 230, 240, 400]

for total in zip(names, bills):
    print(total)

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")