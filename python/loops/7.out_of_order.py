flavours = ["ginger", "out of stock", "tulsi", "discontinued", "lemon"]

for flavour in flavours:
    if flavour == "discontinued":
        break
    if flavour == "out of stock":
        continue
    print(f"{flavour} item found")

print("outside the loop")