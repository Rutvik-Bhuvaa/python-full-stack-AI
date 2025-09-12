# why to use enumerate?
menu = ["green", "lemon", "spiced", "mint"]

for chai in menu:
    print(f"Menu item is {chai}")

for idx, chai in enumerate(menu, start=1):
    print(f"{idx}: {chai} chai")