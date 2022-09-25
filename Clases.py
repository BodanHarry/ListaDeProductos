#Harry
class Producto:

    def __init__(self, cod, nom, des, pre, exi, exiMin):
        self.Codigo = cod
        self.Nombre = nom
        self.Descripcion = des
        self.Precio = pre
        self.Existencia = exi
        self.ExistenciaMinima = exiMin
    
    def __str__(self):
        return f"""Codigo: {self.Codigo}
Nombre: {self.Nombre}
Descripcion: {self.Descripcion}
Precio: {self.Precio}
Existencia: {self.Existencia}
Existencia Minina: {self.ExistenciaMinima}
"""

class ListaProd:

    def __init__(self):
        self.lista =[]
    
    def agregarProducto(self, producto):
        try:
            self.lista.append(producto)
        except Exception as ex:
            print("Error al agregar el producto: ", str(ex))
        
    def editarProducto(self, producto, posicion):
        try:
            self.lista[posicion] = producto
        except Exception as ex:
             print("Error al agregar el producto: ", str(ex))
    
    def eliminarProducto(self, producto):
        try:
            self.lista.remove(producto)
        except Exception as ex:
            print("Error al eliminar el producto: ", str(ex))
    
    def buscarPorCodigo(self, codigo):
        try:
            pos = 0
            for prod in self.lista:
                if prod.Codigo == codigo:
                    print("Producto encontrado...")
                    return prod, pos
                pos+=1
            else:
                print("No se encontró el producto...")        
        except Exception as ex:
            print("Error al buscar elemento:", str(ex))

    def buscarPorNombre(self, nombre):
        try:
            pos = 0
            for prod in self.lista:
                if prod.Nombre == nombre:
                    print("Producto encontrado...")
                    return prod, pos
                pos+=1
            else:
                print("No se encontró el producto...")          
        except Exception as ex:
            print("Error al buscar elemento: ", str(ex))

    def buscarPorPrecio(self, precio):
        try:
            pos = 0
            for prod in self.lista:
                if prod.Precio == precio:
                    print("Producto encontrado...")
                    return prod, pos
                pos+=1
            else:
                print("No se encontró el producto...")        
        except Exception as ex:
            print("Error al buscar elemento: ", str(ex))

    def mostrarExistenciaMenorAMinimo(self):
        try:
            for prod in self.lista:
                if prod.Existencia < prod.ExistenciaMinima:
                    print(prod)       
        except Exception as ex:
            print("Error al mostrar productos con menos existencia: ", str(ex))