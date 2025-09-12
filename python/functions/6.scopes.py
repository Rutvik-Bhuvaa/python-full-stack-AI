def serve_chai():
    chai_type = "masala" # local scope
    print(f"Inside function {chai_type}")


chai_type = "lemon"
serve_chai()
print(f"Outside function {chai_type}")

def chai_counter():
    chai_order = "Lemon" # Enclosing scope
    def print_order():
        chai_order = "Green" # local scope
        print("Inner ", chai_order)
    print_order()
    print("Outer ", chai_order)

chai_order = "Oolong" # Global scope
chai_counter()
print("Global ", chai_order)