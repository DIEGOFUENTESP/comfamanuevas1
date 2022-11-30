#ENTRADAS DEL PROBLEMA
nivelDeAgua= int(input("Digita el nivel del agua"))

#EVALUANDO CAMINOS MULTIPLES (MAS DE 2)
if nivelDeAgua<=100:
    print("Bajo")
elif nivelDeAgua>100 and nivelDeAgua<400:
    print("OK")
elif nivelDeAgua>=400:
    print("MUCHA AGUA")
else:
    print("NIVEL DE AGUA NO VALIDO")