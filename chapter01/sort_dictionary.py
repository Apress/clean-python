users = [
    {"first_name": "Helen", "age": 39},
    {"first_name": "Buck", "age": 10},
    {"name": "anni", "age": 9}
    ]


def get_user_name(users):
    """Get name of the user in lower case"""
    return users["first_name"].lower()

def get_sorted_dictionary(users):
    """Sort the nested dictionary"""
    if not isinstance(users, dict):
        raise ValueError("Not a correct dictionary")
    if not len(users):
        raise ValueError("Empty dictionary")

    users_by_name = sorted(users, key=get_user_name)
    return users_by_name
