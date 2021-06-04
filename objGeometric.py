import math

class FigurasGeometricas:

    def __init__(self, nLados):
        self.nLados=nLados

class Triangulo(FigurasGeometricas):

    def __init__(self,nLados,base,altura):
        FigurasGeometricas(nLados)
        self.base=base
        self.altura=altura
        self.hipotenusa=self.calcularHipotenusa()

    def calcularArea(self):
        area=self.base*self.altura/2
        return area

    def calcularPerimetro(self):
        perimetro=self.altura+self.base+self.hipotenusa
        return perimetro

    def calcularHipotenusa(self):
        bCuadrado=math.pow(self.base,2)
        aCuadrado=math.pow(self.altura,2)
        hipotenusa=math.sqrt(bCuadrado+aCuadrado)
        return hipotenusa

class Rectangulo(FigurasGeometricas):

    def _init_(self, base, altura):
        self.base=base
        self.altura=altura

    
   