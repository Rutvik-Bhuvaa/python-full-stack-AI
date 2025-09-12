# Integer
black_tea_grams = 17;
ginger_grams = 5;
total = black_tea_grams+ginger_grams;
print(f"Total is {total}");

remaining_tea = black_tea_grams-ginger_grams;
print(f"Remaining tea is {remaining_tea}");

total_milk = 7;
servings = 4;
milk_per_serving = total_milk/servings;
print(f"Total milk per serving is {milk_per_serving}");

total_tea_bags = 7;
pots = 4;
bags_per_pot = total_tea_bags//pots; # // used when i don't care about what comes after decimal
print(f"Whole pots per bag is {bags_per_pot}")

total_cardamom_pods = 10;
pods_per_cup = 3;
leftover_pods = total_cardamom_pods%pods_per_cup;
print(f"Leftover pods is {leftover_pods}");

base_flavour_strength = 2;
scale_factor = 3;
powerful_flavour = base_flavour_strength ** scale_factor;
print(f"Powerful flavour is {powerful_flavour}");

total_tea_leaves_harvested = 1_000_000_000;
print(f"Total tea leaves harvested {total_tea_leaves_harvested}")