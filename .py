
class Usuario:   #Persona que solicita libros.
   
    def __init__(self, nombre, pertenece_universidad, es_activo, carnet, tiene_devoluciones_pendientes):
        self.nombre = nombre
        self.pertenece_universidad = pertenece_universidad
        self.es_activo = es_activo
        self.carnet = carnet
        self.tiene_devoluciones_pendientes = tiene_devoluciones_pendientes

    # Acciones que puede realizar
    def recibir_prestamo(self, libro):
        print(f"{self.nombre} ha recibido el libro {libro.titulo} en préstamo.")
        
    def devolver_libro(self, libro):
        print(f"{self.nombre} ha devuelto el libro {libro.titulo}.")
        
    def pagar_multa(self, monto):
        print(f"{self.nombre} ha pagado una multa de {monto}.")
        
    def entregar_carnet(self):
        print("Carnet entregado.")


class Libro: 
    
    def __init__(self, titulo, autor,isbn, estado, disponibilidad, cantidad_copias):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.estado = estado #Bueno-Deteriorado-Perdido
        self.disponibilidad = disponibilidad
        self.cantidad_copias = cantidad_copias

    # Acciones que puede realizar
    def prestar(self):
        if self.cantidad_copias > 0:
            self.cantidad_copias -= 1
            return True
        return False
        
    def regresar(self):
        self.cantidad_copias += 1
        
    def reservar(self):
        print("Libro reservado.")
        
    def buscar(self):
        print("Buscando libro...")
        
    def reportar_perdido(self):
        self.estado = "Perdido"
        self.cantidad_copias = 0
        
    def renovar(self):
        print("Préstamo renovado.")


libro_1 = Libro("Fluent Python", "Luciano Ramalho", "978-1492056355", 3)
libro_2 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", 5)
libro_3 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0156012195", 2)
libro_4 = Libro("Clean Code", "Robert C. Martin", "978-0132350884", 4)
libro_5 = Libro("Dune", "Frank Herbert", "978-0441172719", 1)

print(libro_1.titulo)
print(libro_2.titulo)
print(libro_3.titulo)
print(libro_4.titulo)
print(libro_5.titulo)



class Prestamo:  #Relaciona un Libro con un Estudiante en un momento dado, gestionado por un Bibliotecario.
    
    def __init__(self, libro, estudiante, bibliotecario, fecha_prestamo, fecha_devolucion):
        self.libro = libro                 # Objeto Libro
        self.estudiante = estudiante       # Objeto Estudiante
        self.bibliotecario = bibliotecario # Objeto Bibliotecario 
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado = "Activo"             # Podría ser "Activo", "Devuelto", "Retrasado"





