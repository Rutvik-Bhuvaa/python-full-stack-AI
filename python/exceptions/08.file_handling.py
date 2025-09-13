file = open("order.txt", "w")
try:
    file.write("Masala chai 2 cups")
finally:
    file.close()

# Modern way

with open("orders.txt", "w") as file:
    file.write("Ginger tea 2 cups")