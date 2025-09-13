class InvalidChaiError(Exception): pass

def bill(flavour, cups):
    try:
        menu = {"masala": 20, "ginger": 30}
        if flavour not in menu:
            raise InvalidChaiError(f"{flavour} chai is not in our menu")
        if not isinstance(cups, int):
            raise TypeError("Provide number of cups in INTEGER")
        cost = cups * menu[flavour]
        print(f"You ordered {cups} cups of {flavour} chai so cost is: {cost}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting...")

bill("mint", 2)
bill("masala", "two")
bill("ginger", 3)