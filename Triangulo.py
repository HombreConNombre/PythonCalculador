import math

class Triangulo(FigurasGeometricas):

    def _init_(self,nLados,base,altura):
        FigurasGeometricas._init_(self, nLados)
        self.base=base
        self.altura=altura
        self.hipotenusa=calcularHipotenusa(self)

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