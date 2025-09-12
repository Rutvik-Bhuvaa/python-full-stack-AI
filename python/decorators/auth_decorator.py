from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "Admin":
            print(f"Access Denied because you are {user_role}")
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_tea_inventory(user_role):
    print(f"Access granted to inventory because you are {user_role}")

access_tea_inventory("User")
access_tea_inventory("Admin")
