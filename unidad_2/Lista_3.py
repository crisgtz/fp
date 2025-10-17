#nombre, preparatoria, lugar de residencia, edad, carrera
mis_datos = []

print("Lista_mis_datos")

nombre = input("ingresar nombre: ")

mis_datos.append(nombre)

preparartoria = input("ingresar preparartoria: ")

mis_datos.append(preparartoria)

lugar_de_residencia =("ingresasr lugar_de_residencia : ")

mis_datos.append(lugar_de_residencia)

print("\n Tu lista de mis datos es: ")
for nombre in mis_datos:
    print(f"- {nombre}")


print("\n Tu lista de mis datos es: ")
for preparartoria in mis_datos:
    print(f"- {preparartoria}")


print("\n Tu lista de mis datos es: ")
for lugar_de_residencia in mis_datos:
    print(f"- {lugar_de_residencia}")
    
print("\n✅ ¡Lista creada con éxito!")

#https://www.webfx.com/tools/emoji-cheat-sheet/
