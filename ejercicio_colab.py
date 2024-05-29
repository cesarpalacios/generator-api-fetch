# Problema: calcular el descuento de una compra:
# Instrucciones:
# El usuario realiza 4 compras.	Ejecutar el proceso hasta un  máximo de 4 compras
# Porel nombre del producto, precio y  cantidad cada compra, ingresar
# Calcular el total de la compra y aplicar un descuento del  10% si es total de la compra es igual o superior a $100
# Finalmente, se debe mostrar el total de la compra con o sin  descuento

#https://colab.research.google.com/
#https://www.freecodecamp.org/espanol/learn/


def calculo_descuento(tabla, cantidad_productos):
  suma_compra = 0
  for i in range(0, cantidad_productos):
    suma_compra += tabla[i][1] * tabla[i][2] 
  if suma_compra >= 100:
    valor_descuento = suma_compra * 0.1
    return suma_compra - valor_descuento
  else:
    return suma_compra

def matriz_datos(cantidad_compra, matriz):
  for i in range(0, cantidad_compra):
    nombre_producto = input("ingrese el nombre del producto: ")
    precio = int(input("ingrese el precio sin puntos ni comas: "))
    cantidad = int(input("ingrese las unidades del producto: "))
    matriz.append([nombre_producto, precio, cantidad])
  return matriz

cantidad_compra = int(input('ingrese la cantidad de productos a comprar: ')) #Pidiendo cantidad de productos al usuario y la guardo en variable cantidad de compra
matriz=[] #Lista
if cantidad_compra > 4:
  print ('el valor ingresado supera la cantidad permitida de compra que es 4')
elif cantidad_compra < 1: 
  print ('el valor ingresado tiene que ser como minimo 1')
else:
  matriz = matriz_datos(cantidad_compra, matriz)
  
  numero_productos = len(matriz)
  total_compra = calculo_descuento(matriz, numero_productos)
  print ('El valor total a pagar es: ', int(total_compra))