import math

class FigurasGeometricas_regulares:
    """ Regular figures, all sides are similar
    """
    def __init__( self, nLados, long_lados, apotema):
        self.nLados=nLados
        self.long_lados = long_lados
        self.apotema = apotema
        
    def calcularArea( self):
        area = self.calcularPerimetro() * self.apotema / 2
        return area

    def calcularPerimetro( self):
        perimetro = self.nLados * self.long_lados
        return perimetro
    
class FigurasGeometricas_irregulares:
    """ Irregulars figures, not all sides are similar
    """
    def __init__( self, pos_lados = []) -> None:
        """constructor

        Args:
            long_lados (bidimensional array): Array with the polynomial on the 
            cardinal axes
        """
        self.pos_lados = pos_lados
    
    def calcularPerimetro( self):
        perimetro = 0
        x_previo = self.pos_lados[0][0]
        y_previo = self.pos_lados[0][1]
        for i in range( self.pos_lados):
            x = self.pos_lados[i][0]
            y = self.pos_lados[i][1]
            
            if x != x_previo and y != y_previo:
                base = abs( x - x_previo)
                altura = abs( y - y_previo)
                hipotenusa = math.sqrt( math.pow( base, 2) + math.pow( altura, 2))
                perimetro += hipotenusa
                       
            elif x == x_previo or y == y_previo:
                perimetro += abs( x - x_previo + y - y_previo)    
                
        
        else:
            x = self.pos_lados[0][0]
            y = self.pos_lados[0][1]
            
            if x != x_previo and y != y_previo:
                base = abs( x - x_previo)
                altura = abs( y - y_previo)
                hipotenusa = math.sqrt( math.pow( base, 2) + math.pow( altura, 2))
                perimetro += hipotenusa
                       
            elif x == x_previo or y == y_previo:
                perimetro += abs( x - x_previo + y - y_previo)
                
        return perimetro

    def calcularArea( self):
        area = 0
        x_previo = self.pos_lados[0][0]
        y_previo = self.pos_lados[0][1]
        
        for i in range(self.pos_lados):
            x = self.pos_lados[i][0]
            y = self.pos_lados[i][1]
            x_acum = [[]]
            y_acum = [[]]

        
        return area
        
        
class Triangulo():
    """ Triangules
    """        
    def __init__( self, base = 1, altura = 2):
        self.base = base
        self.altura = altura
        self.hipotenusa = self.calcularHipotenusa()
        
    def calcularArea( self):
        area = self.base * self.altura/2
        return area

    def calcularPerimetro( self):
        perimetro = self.altura + self.base + self.hipotenusa
        return perimetro

    def calcularHipotenusa( self):
        bCuadrado = math.pow( self.base, 2)
        aCuadrado = math.pow( self.altura, 2)
        hipotenusa = math.sqrt( bCuadrado + aCuadrado)
        return hipotenusa

class circunferencia():
    """ Circle
    """
    def __init__( self, radio):
        self.radio = radio
        
    def calcularPerimetro( self):
        perimetro = 2 * self.radio * math.pi
        return perimetro

    def calcularArea( self):
        area = 2 * math.pi * math.pow( self.radio, 2)
        return area