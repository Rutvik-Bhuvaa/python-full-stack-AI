# Dictionary

chai_order = dict(type="ginger tea", sugar=2, size="medium")
print(chai_order)

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"Recipe base: {chai_recipe["base"]}")
print(f"Recipe: {chai_recipe}")
# to delete from dictionary
del(chai_recipe["liquid"])
del chai_recipe["base"]
print(f"Recipe: {chai_recipe}")

# membership
print(f"Is sugar added in chai order? {'sugar' in chai_order}")

chai_order = {"type":"oolong tea", "sugar":2, "size":"large"}
print(f"Chai order details (keys): {chai_order.keys()}")
print(f"Chai order details (values): {chai_order.values()}")
print(f"Chai order details (items): {chai_order.items()}")


last_item = chai_order.popitem();
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

chai_type = chai_order["type"]
print(f"Chai size is {chai_type}")

# if key is not present inside dictionary
customer_note = chai_order.get("note", "No note")
print(f"Customer note is: {customer_note}")

sugar_quantity = chai_order.get("sugar", "No sugar")
print(f"Sugar quantity is: {sugar_quantity}")