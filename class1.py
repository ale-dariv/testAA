#class + nombre de la clase + :

class nombres:

#cuerpo de la clase: funciones,variables
#__init__ (double underscore): python crea una instancia
#self-instancia de clases

    def __init__ (self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
      
    def integrantes (self):
        miembros = ("Nombre de integrante de los particuleros: \n {} {}")
        print(miembros.format(self.nombre, self.apellido))

    def asesorado1 (self):
        alum = ("El alumno oficial de {} es {}")
        print(alum.format(asesor2.nombre, alumno1.nombre))

    def asesorado2 (self):
        alum = ("El alumno oficial de {} es {}")
        print(alum.format(asesor1.nombre, alumno2.nombre))

asesor1 = nombres("Andrés","Ramírez")
asesor2 = nombres("Tzihue", "Cisneros")
alumno1 = nombres("Alexis","Guerreo")
alumno2 = nombres("Alejandra", "Dávila")

#print(type(asesor1))
#print(type(asesor2))
#print(type(alumno1))

asesor1.integrantes()
asesor2.integrantes()
alumno1.integrantes()
alumno2.integrantes()

asesor2.asesorado1()
alumno1.asesorado2()  

