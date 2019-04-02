def get_all_users_age():
    all_users = 1000000000
    for id in all_users:
        user_obj = access_db_to_get_users_by_id(id)
        yield user.name, user.age

for user_name, user_age in get_all_users_age():
    print(user_name, user_age)
