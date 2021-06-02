import funcionesCalculadora


opcion=1
while opcion>0 and opcion<6 :
    print("Menu inicial: ")
    print("1 - Calcular Area")
    print("2 - Calcular Perímetro")
    print("3 - Calcular Hipotenusa")
    print("4 - Calcular punto Intermedio")
    print("5 - Calcular ")
    print("Pulsa cualquier otro número para salir.")
    opcion=int(input())
    #Comienza la elección
    if opcion == 1:
        funcionesCalculadora.calcularArea()
    elif opcion == 2:
        funcionesCalculadora.calcularPerimetro()
    elif opcion == 3:
        funcionesCalculadora.calcularHipotenusa()
    elif opcion == 4:
        funcionesCalculadora.CalcularPuntoMedio()
    elif opcion == 5:
        #No sé qué hacer aún. Admito ideas.
        print("Elegido X")
