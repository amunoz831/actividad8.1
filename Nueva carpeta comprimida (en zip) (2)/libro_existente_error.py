from libro_error import LibroError
from libro import Libro


class LibroExistenteError(LibroError):

    def __init__(self,libro:Libro):
        super().__init__(libro)
    
    def __str__(self):
        return f"El libro con titulo {Libro.titulo} y isbn: {Libro.isbn} ya existe en el catalogo"
        
    
    # Defina metodo inicializador

    # Defina metodo especial
