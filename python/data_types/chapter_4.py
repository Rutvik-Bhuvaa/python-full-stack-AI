# Boolean
is_boiling = True;
stir_count = 5;
total_actions = stir_count+is_boiling #upcastng
print(f"Total actions {total_actions}");

milk_present = 0;
print(f"is there milk present? {bool(milk_present)}")

water_hot = True;
tea_added = False;
can_serve = water_hot and tea_added;
print(f"Can we serve? {can_serve}")