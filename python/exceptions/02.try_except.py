chai_menu = {"Masala": 30, "Ginger": 40}

try:
    chai_menu["Elaichi"]
except KeyError:
    print("The key you are trying to access is does not exist")

print("Hi there")