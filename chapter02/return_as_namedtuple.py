
def get_user_info(user_obj):
    user = get_data_from_db(user_obj)
    UserInfo = namedtuple(“UserInfo”, [“first_name”, “last_name”, “age”])
    
    user_info = UserInfo(first_name=user[“first_name”],
                         last_name=user[“last_name”],
                         age=user[“age”])
    
    return user_info

def get_full_name(user_info):
    return user_info.first_name + user_info.last_name

user_info = get_user_info(user_obj)
full_name = get_full_name(user_info)
