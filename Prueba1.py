import funcionesCalculadora
import math
import objGeometric

figura = 0

opcion=1
while opcion>0 and opcion<6 :
    nLados=int(input("Antes de empezar necesito que me digas cuántos lados tiene la figura geométrica: "))
    if nLados==3:
        base=float(input("Introduce la base: "))
        altura=float(input("Introduce ahora la altura: "))
        #Colocar en el futuro una opción de si está correcto los datos.
        figura = objGeometric.Triangulo(nLados,base,altura)
        print(figura)
        
    elif nLados==4:
         base=float(input("Introduce la base: "))
        altura=float(input("Introduce ahora la altura: "))
        #Colocar en el futuro una opción de si está correcto los datos.
        figura = objGeometric.Rectangulos(nLados,base,altura)
        
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
        funcionesCalculadora.calcularArea(figura)
    elif opcion == 2:
        funcionesCalculadora.calcularPerimetro(figura)
    elif opcion == 3:
        break
    elif opcion == 4:
        funcionesCalculadora.CalcularPuntoMedio()
    elif opcion == 5:
        #No sé qué hacer aún. Admito ideas.
        print("Elegido X")
