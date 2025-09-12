# Tuples
masala_spices = ("Cardamom", "Cloves", "Cinnamon")
(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1 # Behind the scene tuples is responsible for this
print(f"Ratios G: {ginger_ratio}, C: {cardamom_ratio}")
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Now Ratios G: {ginger_ratio}, C: {cardamom_ratio}")

# Membership
print(f"Is ginger present in Masala spices? {'ginger' in masala_spices}")
print(f"Is clove present in Masala spices? {'Cloves' in masala_spices}")
print(f"Is cinnamom present in Masala spices? {'Cinnamon' in masala_spices}")


