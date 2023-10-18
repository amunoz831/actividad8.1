from libro import Libro

class ItemCompra:

    def __init__(self,libro:Libro, cantidad:int):
        self.libro:Libro=libro
        self.cantidad:int=cantidad

    def calcular_subtotal(self):
        return self.cantidad*Libro.precio

