#se crea una lista llamada lista de compras
lista_compras =[]

print("lista de compras")
#agregan los producto

producto1 = input("Agragar un producto: ")
#se da de lata producto1

lista_compras.append(producto1)
#se mada a guasrdar produco en la lesita 

producto2 = input("Agragar un producto:")
#se da de lata producto2

lista_compras.append(producto2)
#se mada a guasrdar produco en la lesita 

producto3 = input("Agragar un producto")
#se da de lata produL3

lista_compras.append(producto3)
#se mada a guasrdar produco en la lesita 

print("\n📌 Tu lista de compras es:")

for producto in lista_compras:
	  print(f"- {producto}")
	  
print("\n✅ ¡Lista creada con éxito!")
#https://www.webfx.com/tools/emoji-cheat-sheet/