def get_user_info(user_obj):
    user = get_data_from_db(user_obj)
    first_name = user["first_name"]
    last_name = user["last_name"]
    age = user["age"]
    return (first_name, last_name, age)


def get_full_name(first_name, last_name):
    return first_name + last_name

first_name, last_name, age = get_user_info(user_obj)
full_name = get_full_name(first_name, last_name)
