class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

# Creating object from class chai

masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")

masala.is_hot = False
print(f"Class: {Chai.is_hot}")
print(f"Object : {masala.is_hot}")

masala.flavour = "Masala"
print(masala.flavour)