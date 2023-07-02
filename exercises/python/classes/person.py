class Person:
    def get_gender(self):
        return 'Unknown'


class Male(Person):
    def get_gender(self):
        return "Male"


class Female(Person):
    def get_gender(self):
        return "Female"
