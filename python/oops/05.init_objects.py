class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        print(f"{self.size}ml of {self.type} chai")

first_order = ChaiOrder("Masala", 200)
first_order.summary()

second_order = ChaiOrder("Ginger", 220)
second_order.summary()