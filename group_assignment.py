# Python script that processes a list of users and determines whether 
# they should be added to specific groups based on their job title.

# Sample user data
users = [
    {"username": "john.doe", "job_title": "Database Administrator", "current_groups": ["IT_Staff"]},
    {"username": "jane.smith", "job_title": "Finance Director", "current_groups": ["DBA_Group", "Finance"]},
    {"username": "bob.jones", "job_title": "Senior DBA", "current_groups": ["IT_Staff"]},
    {"username": "sarah.williams", "job_title": "Marketing Manager", "current_groups": ["Marketing"]},
]

# Define which job titles are allowed in the DBA_Group
dba_allowed_titles = ["Database Administrator", "Senior DBA", "DBA Manager"]

def check_group_eligibility(user, target_group, allowed_titles):
    """
    Determine if a user should be added to a group based on job title criteria.
    
    Args:
        user: Dictionary containing username, job_title, and current_groups
        target_group: Name of the group to check eligibility for
        allowed_titles: List of job titles allowed in the target group
    
    Returns:
        String: "Already a member", "Add to group", or "Flag for review"
    """
    if target_group in user["current_groups"]:
        return "Already a member"
    
    # Check if their job title qualifies them
    if user["job_title"] in allowed_titles:
        return "Add to group"
    else:
        return "Flag for review"

# Process each user
for user in users:
    result = check_group_eligibility(user, "DBA_Group", dba_allowed_titles)
    print(f"{user['username']}: {result}")