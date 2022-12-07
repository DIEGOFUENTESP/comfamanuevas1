opcion=100

print("EMPANADAS: ")
print("*****************\n")

print("1.RESGISTRAR")
print("2.ver")
print("0.SALIR\n")


empanadas=None
while opcion != 0:
    opcion=int(input("DIGITA UNA OPCION: "))
    if opcion==1:
        empanada=input("Digite el nombre de la empanada a registrar: ")
        empanada.append(empanada)
    elif opcion==2:
        
        for empanada in empanadas:
            print(empanada)

    elif opcion==0:
        break
    else:
        print("INVALIDA")