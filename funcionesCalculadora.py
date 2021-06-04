import math
import objGeometric

#Funcion calcular area
def calcularArea(FigurasGeometricas):
    area=FigurasGeometricas.calcularArea()

    return area

#Función Calcular Perímetro - 2
def calcularPerimetro(figura):
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

#Función para calcular la hipotenusa (Completar con objetos)
def calcularHipotenusa(Triangulo):
    hipotenusa=Triangulo.calcularHipotenusa()

    return hipotenusa

#Función para calcular puntos medios en el plano Cartesiano (Futuro: Cambiar los Arrays por Objetos)
def CalcularPuntoMedio():
    X1=float(input("Introduce la coordenada del eje X del primer punto: "))
    Y1=float(input("Introduce la coordenada del eje Y del primer punto: "))
    X2=float(input("Introduce la coordenada del eje X del segundo punto: "))
    Y2=float(input("Introduce la coordenada del eje Y del segundo punto: "))
    P1=[X1,Y1]
    P2=[X2,Y2]
    PmX=(P1[0]+P2[0])/2
    PmY=(P1[1]+P2[1])/2
    Pm=[PmX,PmY]
    print("El punto medio es X: "+str(Pm[0])+" Y: "+str(Pm[1]))

    return None