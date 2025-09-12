staff = [("Amit", 15), ("Raj", 16), ("Zara", 17)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
# fallback logic
else:
    print("No one is eligible to manage the staff")