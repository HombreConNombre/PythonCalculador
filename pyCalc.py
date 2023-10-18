import tkinter as tk
import time
from utils.geometrIrregular import FigurasGeometricas_irregulares
from utils.geometrRegular import *

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
        tk.Button( self, text = "Geometria",
                        command = lambda: self.center_geometry(),
                        width = 10, height = 5, name = 'geometria'
                        ).place( relx = .01, rely = .2)
        tk.Button( self, text = "Calculadora",
                             command = lambda: self.center_calculate(),
                             width = 10, height = 5, name = 'calculadora'
                             ).place( relx = .01, rely = .4)      
        
    def center_geometry( self) -> None:
        self.clean_frame()
        tk.Button( self, text = "Crear un rectángulo/cuadrado",
                  command = lambda: self.create_rectangle()
                  ).place( relx = .12, rely = .1)
        tk.Button( self, text = "Crear un triángulo",
                  command = lambda: self.create_triangle()
                  ).place( relx = .12, rely = .15)
        tk.Button( self, text = "Crear un círculo",
                  command = lambda: self.create_circle()
                  ).place( relx = .12, rely = .2)
        tk.Button( self, text = "Crear un círculo",
                  command = lambda: self.create_irregular()
                  ).place( relx = .12, rely = .25)        
        
    def create_triangle( self) -> None:
        """ we are going to create all necesary widgets to calculate
            triangle area and perimeter.
        """
        self.clean_frame()
        time.sleep(10)
        tk.Label( self, text = "Si te falta algún dato, no hay problema. "
                    ).place( relx = self.winfo_width()/2, rely = 0)
        
        tk.Label( self, text = "Inserta la base: "
                    ).place( relx = .1, rely = .15) 
        self.base = tk.StringVar()
        self.base.set("3.45")
        base_entry = tk.Entry( self, 
                 textvariable = self.base
                 ).place( relx = .1, rely = .15)
        
        tk.Label( self, text = "Inserta la altura: "
                    ).place( relx = .12, rely = .25)
        
        self.height = tk.StringVar()
        self.height.set("3.45")
        height_entry = tk.Entry( self, 
                 textvariable = self.height
                 ).place( relx = .23, rely = .25)
        tk.Label( self, text = "La hipotenusa: "
                    ).place( relx = .12, rely = .25)
        
        self.hypotenuse = tk.StringVar()
        self.hypotenuse.set("3.45")
        hypotenuse_entry = tk.Entry( self, 
                 textvariable = self.hypotenuse
                 ).place( relx = .23, rely = .25)
        """ bind options:
            FocusIn, FocusOut, <Button-1>, <KeyPress>... -> some options
        """
        base_entry.bind('<FocusIn>', self.entry_clean)
        height_entry.bind('<FocusIn>', self.entry_clean)
        hypotenuse_entry.bind('<FocusIn>', self.entry_clean)
        
        tk.Button( self, text = "Calcular",
                  command = lambda: self.calculate_geometr()
                  ).place( relx = .2, rely = .15)
        
    def create_circle( self) -> None:
        self.clean_frame()
        tk.Label( self, text = "Inserta el radio: "
                    ).place( relx = .12, rely = .25)
        
        self.entry_text = tk.StringVar()
        self.entry_text.set("1.5")
        coord_entry = tk.Entry( self, 
                 textvariable = self.entry_text
                 )
        coord_entry.place( relx = .23, rely = .25)
        """ bind options:
            FocusIn, FocusOut, <Button-1>, <KeyPress>... -> some options
        """
        coord_entry.bind('<FocusIn>', self.entry_clean)
        
        tk.Button( self, text = "Calcular",
                  command = lambda: self.calculate_geometr()
                  ).place( relx = .2, rely = .15)
        
    def create_irregular( self) -> None:
        self.clean_frame()
        tk.Label( self, text = "Inserta las coordenadas: "
                    ).place( relx = .12, rely = .25)
        
        self.entry_text = tk.StringVar()
        self.entry_text.set("Ejemplo: X1,Y1;X2;Y2...")
        coord_entry = tk.Entry( self, 
                 textvariable = self.entry_text
                 )
        coord_entry.place( relx = .23, rely = .25)
        """ bind options:
            FocusIn, FocusOut, <Button-1>, <KeyPress>... -> some options
        """
        coord_entry.bind('<FocusIn>', self.entry_clean)
        
        tk.Button( self, text = "Crear polinomio",
                  command = lambda: self.calculate_geometr()
                  ).place( relx = .2, rely = .15)
        
    def calculate_geometr( self, shape: str, values: list) -> None:
        """ We create the labels and calculate perimeter and the area.
        """
        geometry = 0
        match shape:
            case 'square':
                geometry = Rectangulo( values[0])
            case 'rectangle':
                geometry = Rectangulo( values[0], values[1])
            case 'triangle':
                geometry = Triangulo( values[0], values[1])
            case 'circle':
                geometry = circunferencia()
            case 'irregular':
                geometry = FigurasGeometricas_irregulares( self.split_lst())
        
        self.generate_canvas( geometry)
        tk.Label( self,
                    text = f"El perimetro de la figura es: {geometry.calcularPerimetro()}"
                ).place( relx = .2, rely = .2)
        tk.Label( self,
                    text = f"El area de la figura es: {geometry.calcularArea()}"
                ).place( relx = .2, rely = .25)
        
    def split_lst( self) -> list:
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
        self.entry_text.set("")
    
    def generate_canvas( self, irregular_geo) -> None:
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
        
    def center_calculate( self) -> None:
        """ we are going to create the tk.widgets in the central part
        """
        self.clean_frame()
        self.memory_lst = []
        self.calculate_history = tk.StringVar()
        self.value = tk.StringVar()
        self.result = tk.StringVar()
        self.memory = tk.StringVar()
        
        tk.Label( self,
                 text = 'Last operation:'
                 ).place( relx = .2, rely = .1)
        tk.Entry( self,
                background = 'light grey',
                textvariable = self.calculate_history
                ).place( relx = .25, rely = .1)
        
        tk.Label( self,
                 text = 'Result:'
                ).place( relx = .2, rely = .15)
        tk.Label( self,
                 background = 'snow',
                 textvariable = self.result
                ).place( relx = .25, rely = .15)
        
        tk.Label( self,
                 text = 'Operation:'
                ).place( relx = .20, rely = .2)
        tk.Entry( self,
                 background = 'white',
                 textvariable = self.value
                ).place( relx = .25, rely = .2)
        
        # First buttons row
        tk.Button( self, command = lambda: self.basic_calculate('+'), text = " + "
                  ).place( relx = .25, rely = .25)
        tk.Button( self, command = lambda: self.basic_calculate('-'), text = " - "
                  ).place( relx = .27, rely = .25)
        tk.Button( self, command = lambda: self.basic_calculate('/'), text = " / "
                  ).place( relx = .29, rely = .25)
        tk.Button( self, command = lambda: self.basic_calculate('*'), text = " * "
                  ).place( relx = .31, rely = .25)
        
        # Second buttons row
        tk.Button( self, command = lambda: self.add_memory(), text = 'M+'
                            ).place( relx = .25, rely = .28)
        tk.Button( self, command = lambda: self.select_memory(), text = 'M'
                            ).place( relx = .27, rely = .28)
        tk.Button( self, command = lambda: self.delete_memory(), text = 'M-'
                            ).place( relx = .29, rely = .28)
        tk.Button( self, command = lambda: self.advance_calculate('^'), text = ' ^ '
                            ).place( relx = .31, rely = .28)
        
        # Thrid buttons row
        tk.Button( self, command = lambda: self.advance_calculate('√'), text = ' √ '
                            ).place( relx = .25, rely = .31)
        # Memory Lst_Box
        self.memory_lstbox = tk.Listbox( self, background = 'white', listvariable = self.memory,
                              width = 50, height = 50, selectmode = tk.SINGLE
                              ).place( relx = .6, rely = .1)
        
        
    # BASIC MATHS BLOCK
    def basic_calculate( self, operation: str) -> None:
        """ when you push "+, -, * or /" buttons, you call this fuction

        Args:
            operation (str): only +, -, * or /
        """
        if (self.value.get() == '0' or self.result.get() == '') and operation != '/':
            self.calculate_history.set( f"{self.value.get()}")
            self.result.set( self.value.get())
            
        elif operation == '/' and self.value.get() == '0':
            self.result.set( self.value.get())

        else:
            match operation:
                case '+':
                    self.calculate_history.set(f"\n{self.result.get()} + {self.value.get()}")
                    self.result.set( float( self.result.get()) + float( self.value.get()))

                case '-':
                    self.calculate_history.set(f"\n{self.result.get()} - {self.value.get()}")
                    self.result.set( float(self.result.get()) - float( self.value.get()))

                case '/':
                    self.calculate_history.set(f"\n{self.result.get()} / {self.value.get()}")
                    self.result.set( float(self.result.get()) / float( self.value.get()))

                case '*':
                    self.calculate_history.set(f"\n{self.result.get()} * {self.value.get()}")
                    self.result.set( float(self.result.get()) * float( self.value.get()))

    def advance_calculate ( self, operation: str) -> None:
        if not self.value.get() == '0' and ( self.result.get() == '0' or self.result.get() == ''):
            pass
        match operation:
            case '^':
                self.calculate_history.set(f"\n{self.result.get()} ^ {self.value.get()}")
                self.result.set( float(self.result.get()) ** float(self.value.get()))
            case '√':
                self.calculate_history.set(f"\n{self.result.get()} ^ {self.value.get()}")
                self.result.set( float(self.result.get()) ** (1/float(self.value.get())))
                
    # MEMORY BLOCK
    def add_memory( self):
        if not self.value.get() in str( self.memory):
            self.memory_lst.append(self.value.get())
            self.memory.set( self.memory_lst)

    def select_memory( self):
        if self.memory_lstbox.curselection():
            self.value.set( self.memory_lstbox.get( self.memory_lstbox.curselection()))
    
    def delete_memory( self):
        if self.memory_lstbox.curselection():
            self.memory_lst.remove( self.memory_lstbox.get( self.memory_lstbox.curselection()))
            self.memory.set( self.memory_lst)

    # CLEAN BLOCK
    def clean_frame( self):
        for widget in self.winfo_children():
            if not ('geometria' in str(widget) or 'calculadora' in str(widget)):
                widget.destroy()
                
            
if __name__ == "__main__":
    App = Root()
    App.mainloop()