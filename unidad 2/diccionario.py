#Poner todas las variables con mayusculas
Edades = {
    "Brayan": 25,#borrar pabellon de arteaga 
    "Luis": 30,
    "José": 22
}
print("Edad de Luis:", Edades["Luis"])  
#cambiar edades a luisn
Edades["Brayan"] = 28
print("\nDespués de añadir a Brayan:")
print(Edades)                               
#cambiar edades a luisn
Edades["Luis"] = 26
print("\nDespués de actualizar la edad de Luis:")
print(Edades)                              
#cambiar edades a luisn
del Edades["José"]
print("\nDespués de eliminar a José:")
print(Edades)                               
#cambiar edades a Jose para elimiarlo
print("\nRecorriendo el diccionario:")
for Nombre, Edad in Edades.items():         
    print( f"{Nombre} Tiene {Edad} Años")
    #Recorrer el print un espacio acia tras 