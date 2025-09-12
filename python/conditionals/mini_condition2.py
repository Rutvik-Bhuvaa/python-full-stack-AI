snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great choice! We will serve you {snack}")
else:
    print(f"{snack} is unavailable currently")
