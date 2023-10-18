from item_compra import ItemCompra
from libro import Libro
class CarroCompras:
    
    def __init__(self):
        self.items:list[ItemCompra]= []

    def agregar_item(self, libro:Libro, cantidad:int):
        item= ItemCompra(libro,cantidad)
        self.items.append(item)

    def calcular_total(self):
        total=0
        for i in self.items:
            total+=i.calcular_subtotal
        return total

    def quitar_item(self,isbn:str):
         self.items =[item for item in self.items if isbn!=item.libro.isbn]