#Aqui defino la clase Persona (padre) en la cual estan los valores nombre y edad 
class Persona:
    pass
    def __init__(self,nombre,edad):
      self.n = nombre
      self.e = edad
    def __str__(self):
        #y aqui los retorno
        return f"Nonbre de la persona {self.n} y la edad es {self.e}"

#Aqui le digo al usuario que introdusca los valores y creo el objeto
X = Persona(input("diga el nombre de la persona: "), int(input("Diga la edad: "))) 
#Aqui imprimo el objeto
print(X) 

#Aqui creamos la clase empledo (hijo)
class Empleado(Persona):
    pass
    #Aqui le defino los valores sueldo y impuestos 
    def __init__(self,sueldo):
        self.s = sueldo        

    #Aqui defino el valor "total" el cual no es masuna resta entre el suldo y los impuestos 
    def __str__(self):       
        
        if self.s <= 3000:
            #Aqui sigo si la persona en custion no tiene que pagar impuestos            
            return f"Para el sueldo de {self.s}, No hay impuestos que pagar" 
        else:
            return f"Para el sueldo de {self.s}, Si debe pagar impuestos"

#Aqui le digo al usuario que ingrese el valor del sueldo y defino el objeto 
Y = Empleado(float(input("Ingrese el sueldo: ")))

#aqui llamo al objeto con un prin
print(Y)