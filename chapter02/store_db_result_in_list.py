def get_all_users_age(total_users=1000):
    age = []
    for id in total_users:
        user_obj = access_db_to_get_users_by_id(id)
        age.append([user.name, user.age])
    return age

total_users = 1000000000
for user_info in range(total_users):
    info = get_all_users_age()
    for user in info:
        print(user)
