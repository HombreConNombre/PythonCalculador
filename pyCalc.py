import tkinter as tk
from utils.geometrIrregular import FigurasGeometricas_irregulares

minpady = 10
minpadx = 10

class Root(tk.Tk):
    def __init__( self):
        super().__init__()
        
        # window configuration
        self.title("PyCalc")
        
        # Fullscreen configuration
        self.state('zoomed')

        # Menu Buttons
        Geo_btn = tk.Button( self, text = "Geometria", 
                        command = lambda: self.center_geometry(),
                        width = 10, height = 5)
        Geo_btn.place( relx = .01, rely = .2)
        Calc_btn = tk.Button( self, text = "Calculadora",
                             command = lambda: self.center_calculate(),
                             width = 10, height = 5)
        Calc_btn.place( relx = .01, rely = .4)
        
        # Array to refresh the right part to the screen.
        self.center_screen = []
        self.right_screen = []
        
    def center_geometry( self):
        self.clean_center_screen()
        coord_Label = tk.Label( self, text = "Inserta las coordenadas: ")
        coord_Label.place( relx = .12, rely = .1)
        
        self.entry_text = tk.StringVar()
        self.entry_text.set("Ejemplo: X1,Y1;X2;Y2...")
        
        coord_entry = tk.Entry( self, textvariable = self.entry_text)
        coord_entry.place( relx = .23, rely = .1)
        """ bind options:
            FocusIn, FocusOut, <Button-1>, <KeyPress>... -> some options
        """
        coord_entry.bind('<FocusIn>', self.entry_clean)
        
        coord_Button = tk.Button( self, text = "Crear polinomio", command = lambda: self.calculate_geometr())
        coord_Button.place( relx = .2, rely = .15)
        
        self.center_screen.append( coord_entry)
        self.center_screen.append( coord_Button)
        self.center_screen.append( coord_Label)
        
    def calculate_geometr( self):
        """ We create the labels and calculate perimeter and the area.
        """
        self.clean_right_screen()
        irregular_geo = FigurasGeometricas_irregulares( self.split_lst())
        self.generate_canvas( irregular_geo)
        
        self.right_screen.append( tk.Label( self, text = f"El perimetro de la figura es: {irregular_geo.calcularPerimetro()}"
                 ).place( relx = .2, rely = .2))
        self.right_screen.append( tk.Label( self, text = f"El area de la figura es: {irregular_geo.calcularArea()}"
                 ).place( relx = .2, rely = .25))
        
    def split_lst( self):
        value_lst = []
        for string_x_y in self.entry_text.get().split(";"):
            x_y = string_x_y.split(',')
            value_lst.append(x_y)
        
        print(value_lst)
        return value_lst
            
    def entry_clean( self, _):
        """ Clean the entry when take focus in the Entry

        Args:
            _ (event): We MUST take this variable, but we don't need it.
        """
        print("Focus on")
        self.entry_text.set("")
    
    def generate_canvas( self, irregular_geo):
        """ We are going to create the canvas to draw the geometry object.

        Args:
            irregular_geo (FigurasGeometricas_irregulares): own class.
        """ 
        # Canvas block
        canvas = tk.Canvas( self, width = 500, height = 500, bg = "black")
        
        x_prev = 100
        y_prev = 400
        for x_y in irregular_geo.__str__():
            position_x =  float( x_y[0]) * 100
            position_y =  float( x_y[1]) * 100
            canvas.create_line( x_prev, y_prev, # <- From X, Y
                                position_x + 100, 400 - position_y, # <- To X , Y
                                fill = "white", width = 3)
            
            x_prev = position_x + 100
            y_prev = 400 - position_y
        
        else:
            canvas.create_line( x_prev, y_prev, # <- From X, Y
                                100, 400, # <- To X , Y
                                fill = "white", width = 3)
            
        canvas.place( relx = .6, rely = .1)
        self.right_screen.append( canvas)
        
    def center_calculate( self):
        calculate_history = tk.StringVar()
        value = 0
        
        calculate_entry = tk.Entry( self, 
                                   background = 'white',
                                   textvariable = calculate_history + "")
        
        tk.Button( self, command = lambda: )
        
        
        
        
    def clean_center_screen( self):
        if bool( self.center_screen):
            for screen_obj in self.center_screen:
                screen_obj.destroy()
                
    def clean_right_screen( self):
        if bool( self.right_screen):
            for screen_obj in self.right_screen:
                screen_obj.destroy()
            
if __name__ == "__main__":
    App = Root()
    App.mainloop()