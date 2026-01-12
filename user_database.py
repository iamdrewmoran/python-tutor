# A list of group names
groups = ["Engineering", "Sales", "Marketing"]

# A dictionary representing one user
user1 = {
    "username": "john.doe",
    "email": "john.doe@company.com",
    "role": "admin",
    "active": True,
    "groups": ["Marketing", "Sales"]
}

# Access dictionary values
print("Username:", user1["username"])
print("Role:", user1["role"])
print("User groups:", user1["groups"])

# Check if user is in a specific group
if "Engineering" in user1["groups"]:
    print(user1["username"], "is in Engineering group")

# A list of user dictionaries - a mini database!
all_users = [
    {"username": "john.doe", "role": "admin", "active": True},
    {"username": "jane.smith", "role": "manager", "active": True},
    {"username": "bob.jones", "role": "employee", "active": False}
]

# Loop through all users
for user in all_users:
    print("Processing", user["username"])
    if user["active"]:
        print(" -> Account is active")
    else:
        print(" -> Accout is suspended")