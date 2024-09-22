
# Calculadora Compra y venta jugadores FC Mobile (coinfcm) por Luis Flow - https://github.com/luisflow/Calculadora-FC-Mobile

preciocompra= int(input("¿cual es el valor de compra? "))
numjugadorescompra= int(input("¿cuantos jugadores compras? "))
precioventa= int(input("¿cual es el valor de venta? "))
porcventa=  ((10)/100)
ganancia=((precioventa-(precioventa*(porcventa)))-(preciocompra*numjugadorescompra))
print("--------------------------------------------------------")
#print('Precio total de compra: ' + str((preciocompra * numjugadorescompra)))
print("Precio total de compra: {:,.0f}".format((preciocompra * numjugadorescompra)))
print(f'menos {(porcventa*100):.0f}% de venta')
print(f'Precio total de venta: {(precioventa-(precioventa*(porcventa))):,.0f}')
#print('Ganancia Ocasional: '
if ganancia <  0 :
   print(f'Compra negativa  {round(ganancia):.0f}  \u2639')
else:
   #print('Compralo, es ganancia de : ' + str(round(ganancia,0)))
   print("========================================================")
   print(f"!!! COMPRALO, es ganancia de ${round(ganancia):.0f} !!!    OK: \u263A ")
   #print('GANANCIA: '+ str(ganancia))
   print("========================================================")