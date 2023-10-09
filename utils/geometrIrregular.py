from .intGeometric import polinomios
import math

class FigurasGeometricas_irregulares( polinomios):
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
        x_previo = float( self.pos_lados[0][0])
        y_previo = float( self.pos_lados[0][1])
        for i in range( len(self.pos_lados)):
            x = float( self.pos_lados[i][0])
            y = float( self.pos_lados[i][1])
            
            if x != x_previo and y != y_previo:
                base = abs( x - x_previo)
                altura = abs( y - y_previo)
                hipotenusa = math.sqrt( math.pow( base, 2) + math.pow( altura, 2))
                perimetro += hipotenusa
                       
            elif x == x_previo or y == y_previo:
                perimetro += abs( x - x_previo + y - y_previo)    
                
        else:
            x = float( self.pos_lados[0][0])
            y = float( self.pos_lados[0][1])
            
            if x != x_previo and y != y_previo:
                base = abs( x - x_previo)
                altura = abs( y - y_previo)
                hipotenusa = math.sqrt( math.pow( base, 2) + math.pow( altura, 2))
                perimetro += hipotenusa
                       
            elif x == x_previo or y == y_previo:
                perimetro += abs( x - x_previo + y - y_previo)
                
        return perimetro

    def calcularArea( self):
        """ Calculate the area 

        Returns:
            area(float): the calculated area
        """
        x_acum = [ 0, 0] # [x0, x1]
        y_acum = [0,0] # [y0, y1]
        
        for i in range( len( self.pos_lados)):
            xy_2sum = self.pos_lados[i]
            
            if i == 0:
                x_acum[0] += float( xy_2sum[0])
                y_acum[0] += float( xy_2sum[1])
            elif i == len(self.pos_lados)-1:
                x_acum[1] += float( xy_2sum[0])
                y_acum[1] += float( xy_2sum[1])
            else:
                x_acum[0] += float( xy_2sum[0])
                y_acum[0] += float( xy_2sum[1])
                x_acum[1] += float( xy_2sum[0])
                y_acum[1] += float( xy_2sum[1])
            
        x_acum[0] /= 2
        y_acum[1] /= 2
        
        area = float( x_acum[0]) * float( y_acum[1]) 
        return area
    
    def __str__(self) -> str:
        print( self.pos_lados)
        return self.pos_lados