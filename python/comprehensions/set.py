favourite_chais = [
    "Masala chai", "Green Tea", "Masala chai",
    "Lemon tea", "Green Tea", "Elaichi chai"
]

# I want to find unique chais

unique_chai = {chai for chai in favourite_chais}
print(unique_chai)

unique_chai = {chai for chai in favourite_chais if len(chai) > 8}
print(unique_chai)

unique_chai = {chai for chai in favourite_chais if len(chai) < 8}
print(unique_chai)

recipes = {
    "Masala chai": ["ginger", "cardemom", "clove"],
    "Elaichi chai": ["milk", "cardemom"],
    "Spicy chai": ["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)