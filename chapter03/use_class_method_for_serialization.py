class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def using_string(cls, names_str):
        first, second = map(str, names_str.split(""))
        student = cls(first, second)
        return Student

    @classmethod
    def using_json(cls, obj_json):
        # Parsing json object…
        return Student

    @classmethod
    def using_file_obj(cls, file_obj):
       # Parsing file object…
       return Student


data = User.using_string("Larry Page")
data = User.using_json(json_obj)
data = User.using_file_obj(file_obj)
