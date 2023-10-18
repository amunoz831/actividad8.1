from carro_compra import CarroCompras
from libro import Libro
from libro_existente_error import LibroExistenteError
from libro_agotado_error import LibroAgotadoError
from existencias_insuficientes_error import ExistenciasInsuficientesError
class TiendaLibros:
    def __init__(self):
        self.catalogo:dict[str:Libro] = {}
        self.carrito: CarroCompras=CarroCompras()

    def adicionar_libro_a_catalogo(self,isbn:str,titulo:str,precio:float,existancias:int):
        if isbn in self.catalogo:
            raise LibroExistenteError
        else:
            libro=Libro(isbn,titulo,precio,existancias)
            self.catalogo[isbn]=libro
            return libro

    def agregar_libro_a_carrito(self,libro:Libro,cantidad_a_agregar:int):
        if libro.existencias == 0:
            raise LibroAgotadoError
        elif libro.existencias < cantidad_a_agregar:
            raise ExistenciasInsuficientesError
        else:
            CarroCompras.agregar_item(libro,cantidad_a_agregar)

    def retirar_item_de_carrito(self,isbn:str):
        CarroCompras.quitar_item(isbn)
