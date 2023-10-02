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