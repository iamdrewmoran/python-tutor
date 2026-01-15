def check_admin_access(role, is_active):
    """Check if a user should have admin access"""
    if role == "admin" and is_active:
        return True
    else:
        return False
    
def format_user_info(username, email, role):
    """Format user information as a readable string"""
    return f"User: {username} | Email: {email} | Role: {role}"

# Test the functions
has_access = check_admin_access("admin", True)
print("Admin access granted:", has_access)

user_info = format_user_info("john.doe", "john@company.com", "admin")
print(user_info)

# Test with different values
has_access2 = check_admin_access("employee", True)
print("Employee admin access:", has_access2)