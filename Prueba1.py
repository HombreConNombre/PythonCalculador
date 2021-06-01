import math

#Función Calcular Area - 1
def calcularArea():
    print("¿Qué figura geométrica es:")
    print("1 - Triangulo")
    print("2 - Rectángulo")
    print("3 - Figuras de +4 lados regulares")
    print("4 - Círculo")
    opcion=input()
    opcion=float(opcion)
    if opcion==1:
        base=input("Introduce la base: ")
        altura=input("Introduce la altura: ")
        base=float(base)
        altura=float(altura)
        area=base*altura/2
        print("El AREA del triángulo es: "+str(area))
    elif opcion==2:
        base=input("Introduce la base: ")
        altura=input("Introduce la altura: ")
        base=float(base)
        altura=float(altura)
        area=base*altura
        print("El AREA de la figura es: "+str(area))
    elif opcion==3:
        nlados=input("Introduce el número de lados: ")
        lado=input("Introduce la longitud de un lado: ")
        apotema=input("Introduce la longitud del apotema: ")
        nlados=int(nlados)
        lado=float(lado)
        apotema=float(apotema)
        perimetro=lado*nlados
        area=perimetro*apotema/2
        print("El AREA del pentágono es: "+str(area))
    elif opcion==4:
        radio=input("Introduce radio: ")
        radio=float(radio)
        area=float(math.pi*math.pow(radio,2))
        print("El AREA del círculo es: "+str(area))
            
    return None

#Función Calcular Perímetro - 2
def calcularPerimetro():
    print("¿Qué figura geométrica es:")
    print("1 - Triangulo")
    print("2 - Rectángulo")
    print("3 - Figuras de +4 lados regulares")
    print("4 - Círculo")
    opcion=input()
    opcion=float(opcion)
    if opcion==1:
        lado1=input("¿Cuánto mide el primer lado?")
        lado2=input("¿Cuánto mide el segundo lado?")
        lado3=input("¿Cuánto mide el tercer lado?")
        perimetro=float(lado1+lado2+lado3)
        print("El PERÍMETRO del triángulo es: "+str(perimetro))
    elif opcion==2:
        base=input("Introduce la base: ")
        altura=input("Introduce la altura: ")
        perimetro=float((base+altura)*2)
        print("El PERÍMETRO de la figura es: "+str(perimetro))
    elif opcion==3:
        nlados=input("Introduce el número de lados: ")
        lado=input("Introduce la longitud de un lado: ")
        nlados=int(nlados)
        lado=float(lado)
        perimetro=lado*nlados
        print("El PERÍMETRO del pentágono es: "+str(perimetro))
    elif opcion==4:
        radio=input("Introduce radio: ")
        radio=float(radio)
        area=float(2*math.pi*radio)
        print("El PERÍMETRO del círculo es: "+str(area))
            
    return None

#Función para calcular la hipotenusa
def calcularHipotenusa():
    base=float(input("Introduce la base del triángulo: "))
    altura=float(input("Introduce la altura del triángulo: "))
    bCuadrado=math.pow(base,2)
    aCuadrado=math.pow(altura,2)
    hipotenusa=math.sqrt(bCuadrado+aCuadrado)
    print("La HIPOTENUSA es: "+str(hipotenusa))

    return None

#Función para calcular puntos medios en el plano Cartesiano
def CalcularPuntoMedio():
    X1=float(input("Introduce la coordenada del eje X del primer punto: "))
    Y1=float(input("Introduce la coordenada del eje Y del primer punto: "))
    X2=float(input("Introduce la coordenada del eje X del segundo punto: "))
    Y2=float(input("Introduce la coordenada del eje Y del segundo punto: "))
    P1=[X1,Y1]
    P2=[X2,Y2]

    return None

print("Menu inicial: ")
print("1 - Calcular Area")
print("2 - Calcular Perímetro")
print("3 - Calcular Hipotenusa")
print("4 - Calcular punto Intermedio")
print("5 - Calcular ")
opcion=input()
opcion=int(opcion)
#Comienza la elección
if opcion == 1:
    calcularArea()
elif opcion == 2:
    calcularPerimetro()
elif opcion == 3:
    calcularHipotenusa()
elif opcion == 4:
    print("Elegido punto Intermedio")
elif opcion == 5:
    print("Elegido X")
