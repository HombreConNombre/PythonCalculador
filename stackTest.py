import tkinter as tk
from utils.geometrIrregular import FigurasGeometricas_irregulares

minpady = 10
minpadx = 10

class Root(tk.Tk):
    def __init__( self):
        super().__init__()
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
        tk.Label( self, text = "Inserta las coordenadas: "
                               ).place( relx = .12, rely = .1)
        
        tk.Entry( self,
                 ).place( relx = .23, rely = .1)
        """ bind options:
            FocusIn, FocusOut, <Button-1>, <KeyPress>... -> some options
        """        
        tk.Button( self, text = "Crear polinomio"
                  ).place( relx = .2, rely = .15)        
             
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
        tk.Button( self, text = " + "
                  ).place( relx = .25, rely = .25)
        tk.Button( self, text = " - "
                  ).place( relx = .27, rely = .25)
        tk.Button( self, text = " / "
                  ).place( relx = .29, rely = .25)
        tk.Button( self, text = " * "
                  ).place( relx = .31, rely = .25)
        
        # Second buttons row
        tk.Button( self, text = 'M+'
                            ).place( relx = .25, rely = .28)
        tk.Button( self, text = 'M'
                            ).place( relx = .27, rely = .28)
        tk.Button( self, text = 'M-'
                            ).place( relx = .29, rely = .28)
        tk.Button( self, text = ' ^ '
                            ).place( relx = .31, rely = .28)
        
        # Thrid buttons row
        tk.Button( self, text = ' √ '
                            ).place( relx = .25, rely = .31)
        # Memory Lst_Box
        self.memory_lstbox = tk.Listbox( self, background = 'white', listvariable = self.memory,
                              width = 50, height = 50, selectmode = tk.SINGLE
                              ).place( relx = .6, rely = .1)
    # CLEAN BLOCK
    def clean_frame( self):
        print(len(self.winfo_children()))
        for widget in self.winfo_children():
            print( widget.winfo_id)
            if not ('geometria' in str(widget) or 'calculadora' in str(widget)):
                widget.destroy()
                
            
if __name__ == "__main__":
    App = Root()
    App.mainloop()