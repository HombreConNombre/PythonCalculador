from utils.funcionesCalculadora import *
from utils.geometrRegular import *
from utils.geometrIrregular import *

figura = Triangulo()


def introduccion():
    regular_irregular = input("Por favor, dime si la figura geométrica es regular, irregular o circular: ")
    
    if regular_irregular.upper() == "REGULAR":
        consulta_regular()
            
    elif regular_irregular.upper() == "CIRCULAR":
        consulta_circunferencia()
    
    elif regular_irregular.upper() == "IRREGULAR":
        consulta_irregular()    

def consulta_regular():
    global figura
    
    n_lados = int(input("¿Cuántos lados tiene esa figura?"))
    if n_lados == 3:
        altura = float(input( "Inserta la altura del triángulo: "))
        base = float(input( "Introduce la longitud de la base: ")) 
        figura = Triangulo( base, altura)  
    
    elif n_lados == 4:
        long_lados = float(input( "Inserte la longitud de los lados: "))
        altura = float(input( "Introdúceme la altura: "))
        figura = Rectangulo( n_lados, long_lados, altura)
    
    else:
        long_lados = float(input( "Inserte la longitud de los lados: "))
        apotema = float(input( "Introdúceme la apotema: "))
        figura = FigurasGeometricas_regulares( n_lados, long_lados, apotema)
        
def consulta_circunferencia():
    global figura
    radio = float(input( "Introduce el radio del círculo: "))
    figura = circunferencia( radio)
    
def consulta_irregular():
    global figura
    n_lados = int(input( "¿Cuántos lados tiene tu polinomio?: "))
    pos_cards = []
    
    for _ in range(n_lados):
        x = float( input( " Introduce la coordenada X: "))
        y = float( input( "Introduce la coodernada Y: "))
        
        pos_cards.append([ x, y])
        print(pos_cards)
        
    figura = FigurasGeometricas_irregulares(pos_cards)
        
if __name__ == '__main__':
    opcion = 1
    introduccion()
    while int(opcion) > 0 and int(opcion) < 6 :
        print("""Menu inicial: 
            1 - Calcular Area
            2 - Calcular Perímetro
            3 - Calcular Hipotenusa
            4 - Calcular punto Intermedio
            5 - Coger otra figura
            Pulsa cualquier otro número para salir.""")
        opcion = input()
        #Comienza la elección
        match opcion:
            case '1':
                print( "El area es: "+ str(figura.calcularArea()))
            case '2':
                print( "El perímetro es: "+ str(figura.calcularPerimetro()))
            case '3':
                print( "El hipotenusa es: "+ str(figura.calcularHipotenusa()))
            case '4':
                CalcularPuntoMedio()
            case '5':
                introduccion()    
