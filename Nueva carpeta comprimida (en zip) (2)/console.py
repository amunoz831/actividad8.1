import sys

from tienda_libros import TiendaLibros
from libro_agotado_error import LibroAgotadoError
from existencias_insuficientes_error import ExistenciasInsuficientesError
from libro_existente_error import LibroExistenteError
from libro_error import LibroError

class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def retirar_libro_de_carrito_de_compras(self):
        isbn=str(input("ingrese el isbn del libro que desea retirar del carrito: "))
        TiendaLibros.retirar_item_de_carrito(isbn)
        print("el libro se retiro con exito")

    def agregar_libro_a_carrito_de_compras(self):
            isbn = str(input("Ingrese el ISBN del libro: "))
            cantidad = int(input("Ingrese la cantidad de unidades: "))
            
            try:
                TiendaLibros.agregar_libro_a_carrito(isbn, cantidad)
                print(f"{cantidad} copias del libro con ISBN {isbn} han sido agregadas al carrito.")
            except LibroAgotadoError as e:
                print(f"Error: {e}")
            except ExistenciasInsuficientesError as e:
                print(f"Error: {e}")

    def adicionar_un_libro_a_catalogo(self):
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            precio = float(input("Ingrese el precio del libro: "))
            existencias = int(input("Ingrese la cantidad de existencias: "))
        
            try:
                TiendaLibros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
                print("El libro ha sido agregado al catálogo.")
            except LibroExistenteError as e:
                print(f"Error: {e}")
            except LibroError as e:
                print(f"Error al agregar el libro al catálogo: {e}")
