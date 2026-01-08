user_role = "admin"
is_active = False

if user_role == "admin" and is_active:
    print("Access granted: Full admin privileges")
elif user_role == "manager" and is_active:
    print("Access granted: Manager privileges")
elif user_role == "employee" and is_active:
    print("Access granted: Standard user")
else:
    print("Access denied: Account is not active")