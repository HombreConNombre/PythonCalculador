from intGeometric import polinomios
import math

class FigurasGeometricas_regulares(polinomios):
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

class Rectangulo(polinomios):
    """ Rectangule figures
    """
    def __init__( self, long_lados, altura):
        self.nLados = 4
        self.long_lados = long_lados
        self.altura = altura
        
    def calcularArea( self):
        area = self.calcularPerimetro() * self.altura / 2
        return area

    def calcularPerimetro( self):
        perimetro = (self.altura + self.long_lados) * 2
        return perimetro

        
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