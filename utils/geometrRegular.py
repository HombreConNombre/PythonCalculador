from intGeometric import polinomios
import math

class FigurasGeometricas_regulares(polinomios):
    """ Regular figures, all sides are similar
    """
    def __init__( self, n_lados: int, long_lados: float, apotema: float):
        self.__n_lados= n_lados
        self.__long_lados = long_lados
        self.__apotema = apotema
        
    # GET and SET BLOCK
    def get_n_lados( self) -> int:
        return self.__n_lados
    
    def set_n_lados( self, new_n_lados: int) -> None:
        self.__n_lados = new_n_lados
        
    def get_long_lados( self) -> int:
        return self.__long_lados
    
    def set_long_lados( self, new_long_lados: float) -> None:
        self.__long_lados = new_long_lados
        
    def get_apotema( self) -> int:
        return self.__apotema
    
    def set_apotema( self, new_apotema: float) -> None:
        self.__apotema = new_apotema

    # FUNCTIONS BLOCK
    def calcularArea( self) -> float:
        area = self.calcularPerimetro() * self.__apotema / 2
        return area

    def calcularPerimetro( self) -> float:
        perimetro = self.__n_lados * self.__long_lados
        return perimetro

class Rectangulo( polinomios):
    """ Rectangule figures
    """
    def __init__( self, long_lados: float, altura: float):
        self.__n_lados = 4
        self.__long_lados = long_lados
        self.__altura = altura
    
    # GET and SET BLOCK
    def get_n_lados( self) -> int:
        return self.__n_lados
    
    def set_n_lados( self, new_n_lados: int) -> None:
        self.__n_lados = new_n_lados
        
    def get_long_lados( self) -> int:
        return self.__long_lados
    
    def set_long_lados( self, new_long_lados: float) -> None:
        self.__long_lados = new_long_lados
        
    def get_altura( self) -> int:
        return self.__altura
    
    def set_altura( self, new_altura: float) -> None:
        self.__altura = new_altura
    
    # FUCTIONS BLOCK    
    def calcularArea( self) -> float:
        area = self.__altura * self.__long_lados
        return area

    def calcularPerimetro( self) -> float:
        perimetro = (self.__altura + self.__long_lados) * 2
        return perimetro

        
class Triangulo( polinomios):
    """ Triangules
    """        
    def __init__( self, base: float = 1, altura: float = 2):
        self.__n_lados = 3
        self.__base = base
        self.__altura = altura
        self.__hipotenusa = self.calcularHipotenusa()
        
     # GET and SET BLOCK
    def get_n_lados( self) -> int:
        return self.__n_lados
    
    def set_n_lados( self, new_n_lados: int) -> None:
        self.__n_lados = new_n_lados
        
    def get_base( self) -> int:
        return self.__long_lados
    
    def set_base( self, new_long_lados: float) -> None:
        self.__long_lados = new_long_lados
        
    def get_altura( self) -> int:
        return self.__altura
    
    def set_altura( self, new_altura: float) -> None:
        self.__altura = new_altura
        
    def get_hipotenusa( self) -> int:
        return self.__hipotenusa
    
    def set_hipotenusa( self, new_hipotenusa: float) -> None:
        self.__hipotenusa = new_hipotenusa
        
    # FUCTIONS BLOCK
    def calcularArea( self) -> float:
        area = self.__base * self.__altura/2
        return area

    def calcularPerimetro( self) -> float:
        perimetro = self.__altura + self.__base + self.hipotenusa
        return perimetro

    def calcularHipotenusa( self) -> float:
        bCuadrado = math.pow( self.__base, 2)
        aCuadrado = math.pow( self.__altura, 2)
        hipotenusa = math.sqrt( bCuadrado + aCuadrado)
        return hipotenusa

class circunferencia( polinomios):
    """ Circle
    """
    def __init__( self, radio):
        self.__radio = radio
        
    # GET and SET BLOCK
    def get_radio( self) -> float:
        return self.__radio
    
    def set_radio( self, new_radio: float) -> None:
        self.__radio = new_radio
        
    # FUCTIONS BLOCK
    def calcularPerimetro( self) -> float:
        perimetro = 2 * self.radio * math.pi
        return perimetro

    def calcularArea( self) -> float:
        area = 2 * math.pi * math.pow( self.radio, 2)
        return area