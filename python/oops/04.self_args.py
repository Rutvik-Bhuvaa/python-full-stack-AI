class Chaicup:
    size = 150 # ml

    def describe(self):
        print(f"A {self.size}ml chai cup")


cup = Chaicup()
cup.describe()  # it has reference
# Chaicup.describe() # It doesn't have reference so it gives error
Chaicup.describe(cup) # now it has reference

cup_two = Chaicup()
cup_two.size = 100
Chaicup.describe(cup_two)
cup_two.describe()

