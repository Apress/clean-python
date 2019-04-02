class Employee(Person):
    POSITIONS = ("Superwiser", "Manager", "CEO", "Founder")

    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department
        self.age = None
        self._age_last_calculated = None
        self._recalculated_age()

    def __str__(self):
        return ("Name: " + self.name + "\nDepartment: "
               + self.department)
        
    @classmethod
    def no_position_allowed(cls, position):
        return [t for t in cls.POSITIONS if t != position]

    

    @staticmethod
    def c_positions(position):
        return [t for t in cls.TITLES if t in position]

    @property
    def id_with_name(self):
        return self.id, self.name

    def age(self):
        if (datetime.date.today() > self._age_last_recalculated):
            self.__recalculated_age()
        return self.age


    def _recalculated_age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year
        if today < datetime.date(
           today.year, self.birthday.month,
           self.birthday.year):
	     age -= 1
        self.age = age
        self._age_last_recalculated = today
