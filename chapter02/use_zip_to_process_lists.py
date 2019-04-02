def get_user_salary_info():
    users = get_users_name_from_db()
    # ["Abe", "Larry", "Adams", "John", "Sumit", "Adward"]
    
    users_salary = get_users_salary_from_db()
    #  ["2M", "1M", "60K", "30K", "80K", "100K"]

    users_salary = []
    for usr, slr in zip(users, users_salary):
        users_salary.append(usr, slr)

    return users_salary
