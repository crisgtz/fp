class Auto:
    def __init__(self, marca, velocidad_maxima):
        self.__marca = marca           # atributo privado
        self.__velocidad_maxima = velocidad_maxima
        self.__velocidad_actual = 0

    # obtiene velocidad
    def get_velocidad_actual(self):
        return self.__velocidad_actual

#Crea un auto con una velocidad maxima y mustra su velocidad actual
    

    # método para acelerar
    def acelerar(self, aumento):
        if self.__velocidad_actual + aumento > self.__velocidad_maxima:
            self.__velocidad_actual = self.__velocidad_maxima
        else:
            self.__velocidad_actual += aumento

#muestra como el auto aumenta la velocidad 
    
    # método para frenar
    def frenar(self, reduccion):
        if self.__velocidad_actual - reduccion < 0:
            self.__velocidad_actual = 0
        else:
            self.__velocidad_actual -= reduccion


auto1 = Auto("Toyota", 180)

auto1.acelerar(50)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto1.acelerar(200)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto1.frenar(100)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto2 = Auto("Nissan", 200)

auto2.acelerar(50)
print("Velocidad actual:", auto2.get_velocidad_actual(), "km/h")

auto2.acelerar(200)
print("Velocidad actual:", auto2.get_velocidad_actual(), "km/h")

auto2.frenar(100)
print("Velocidad actual:", auto2.get_velocidad_actual(), "km/h")



#__Marca = Variables privadas
#_Marca = Variables que se pueden mandar llamar llamando primero a la clase 
#Marca = variables publicas 