def process_order(item, quantity):
    try:
        price = {"Masala": 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print(f"Sorry we don't have {item} chai in our menu")
    except TypeError:
        print("Quantity must be in number")


process_order("Ginger", 2)
process_order("Masala", "two")