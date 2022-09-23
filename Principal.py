from Clases import Producto as prod, ListaProd as lst

listaProd = lst()

def menu():
    print("1. Agregar Producto")
    print("2. Editar Producto")
    print("3. Eliminar Producto")
    print("4. Buscar por código")
    print("5. Buscar por Nombre")
    print("6. Buscar por precio")
    print("7. Mostrar Productos con poca existencia")
    print("8. Mostrar todos los productos")
    print("9. Salir")
    op = int(input("Escriba su opción: "))
    return op

def agregarProducto():
    print("Agregar Producto")
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    precio = input("Precio: ")
    existencia = input("Existencia: ")
    existenciaMinima = input("Existencia mínima: ")
    producto = prod(codigo, nombre, descripcion, precio, existencia, existenciaMinima)
    print(producto)
    listaProd.agregarProducto(producto)

def modificarProducto():
    print("Editar Producto")
    cod = input("Código: ")
    prodV, posV = listaProd.buscarPorCodigo(cod)
    print(f"""Producto seleccionado {prodV}""")
    print(prodV)
    print("Nuevos Datos del producto")
    nuevoNombre = input("Nombre: ")
    nuevaDescripcion = input("Descripcion: ")
    nuevoPrecio = input("Precio: ")
    nuevaExistencia = input("Existencia: ")
    nuevaExistenciaMinima = input("Existencia Mínima: ")
    nuevoProducto = prod(cod, nuevoNombre, nuevaDescripcion, nuevoPrecio, nuevaExistencia, nuevaExistenciaMinima)
    listaProd.editarProducto(nuevoProducto, posV)

def eliminarProducto():
    print("Eliminar Producto")
    cod = input("Código: ")
    prodV1, pos = listaProd.buscarPorCodigo(cod)
    print(f"""Realmente desea eliminar el registro {prodV1}""")
    resp = input("SI - NO")
    if resp.upper()=="SI":
        listaProd.eliminarProducto(prodV1)
    else:
        print("Operación cancelada")

def buscarPorCodigo():
    print("Buscar Producto")
    cod = input("Código: ")
    try:
        producto, pos = listaProd.buscarPorCodigo(cod)
 
        if producto.Codigo != None:
            print(producto)
    except Exception as ex:
        print("Error al buscar código", str(ex))

def buscarPorNombre():
    print("Buscar Producto por Nombre")
    nombre = input("Nombre: ")
    try:
        producto, pos = listaProd.buscarPorNombre(nombre)
 
        if producto.Codigo != None:
            print(producto)
    except Exception as ex:
        print("Error al buscar código", str(ex))

def buscarPorPrecio():
    print("Buscar Producto por Precio")
    precio = input("Precio: ")
    try:
        producto, pos = listaProd.buscarPorPrecio(precio)
 
        if producto.Codigo != None:
            print(producto)
    except Exception as ex:
        print("Error al buscar código", str(ex))


def  mostrarExistenciaMenorAMinimo():
    listaProd.mostrarExistenciaMenorAMinimo();
        
def mostrarProductos():
    for producto in listaProd.lista:
        print(producto)
        print("="*25)


def main():
    op = 0
    while(op!=10):
        op = menu()
        if op == 1: agregarProducto()
        elif op == 2: modificarProducto()
        elif op == 3: eliminarProducto()
        elif op == 4: buscarPorCodigo()
        elif op == 5: buscarPorNombre()
        elif op == 6: buscarPorPrecio()
        elif op == 7: mostrarExistenciaMenorAMinimo()
        elif op == 8: mostrarProductos()
        elif op == 9: print("Adios...")
        else: print("Opción no válida")

main()