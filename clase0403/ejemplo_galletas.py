class Galletas:
    def __init__ (self, sabor, tiene_chispas):
        self.sabor = sabor
        self.tiene_chispas = tiene_chispas
        print(f"Se ha creado una galleta de sabor {self.sabor}. ¿Con chispas? {self.tiene_chispas}.")
        
mi_galleta = Galletas("Vainilla", True)
mi_galleta2 = Galletas("Chocolate", False)