from model import Persona

persona = Persona('Luis', 'Perez', 34)

class PersonaController:
    def __init__(self):
        pass

    def ver_personas(self):
        return persona.to_dict()

    # def crear_personas(self, edad):
    #     if type(edad) == 'int':
    #             self.persona = Persona(self.nombre, self.apellido, self.edad)
    # #    else
    # #     return self.persona.to_dict()