class Person:

    def __init__(self, first_name, last_name):
        self._full_name = f"${first_name} ${last_name}"

    def get_name(self):
        return self._full_name

per = Person("Larry", "Page")
assert per.get_name() == "Larry Page"
