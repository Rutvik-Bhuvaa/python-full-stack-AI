# List
ingradients = ["water", "milk", "black tea"]
ingradients.append("sugar")
print(f"Ingradients: {ingradients}")
ingradients.remove("milk")
print(f"Ingradients: {ingradients}")

spice_options = ["ginger", "cardamom"]
chai_ingradients = ["water", "milk"]
print(f"Chai ingradients: {chai_ingradients}")
chai_ingradients.extend(spice_options)
print(f"Chai ingradients: {chai_ingradients}")

# to add black tea at 2nd position
chai_ingradients.insert(2, "black tea")
print(f"Chai ingradients: {chai_ingradients}")

last_added = chai_ingradients.pop()
print(last_added)
print(f"Chai ingradients: {chai_ingradients}")
chai_ingradients.reverse()
print(f"Chai ingradients: {chai_ingradients}")
chai_ingradients.sort()
print(f"Chai ingradients: {chai_ingradients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Maximum sugar level: {min(sugar_levels)}")

# Operator overloading 
base_liquids = ["water", "milk"]
flavours = ["ginger"]
mix_liquid = base_liquids + flavours
print(f"Mix liquid: {mix_liquid}")

strong_brew = ["black tea"] * 3
print(strong_brew)
# it maintains the order as well
strong_brews = ["black tea", "water"] * 3
print(strong_brews)

# bytearray - It returns a new array of bytes
raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(raw_spice_data)