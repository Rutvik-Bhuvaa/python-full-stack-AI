# Set
essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"clove", "ginger", "black pepper"}

# union
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# intersection
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

# difference
# left difference
only_essential_spices = essential_spices - optional_spices
print(f"Only in essential spices: {only_essential_spices}")

# right difference
only_optional_spices = optional_spices - essential_spices
print(f"Only in optional spices: {only_optional_spices}")

# membership
print(f"Is clove in essential spices? {'clove' in essential_spices}")
print(f"Is clove in optional spices? {'clove' in optional_spices}")
