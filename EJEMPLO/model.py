class Persona:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
    def to_dict(self):
        return self.__dict__
