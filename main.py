from producto import Producto
from proveedor import Proveedor
from ventas import Venta
from KioscoDB import cerrar
def main():
    while True:
        print("- - - - > Menu Principal < - - - -")
        print("[1].Gestionar tabla productos.")
        print("[2].Gestionar tabla proveedores.")
        print("[3].Gestionar tabla ventas.")
        print("[4].Salir.")
        seleccion = int(input("Seleccione una opcion: "))
        if seleccion == 1:
            MenuProductos()
        elif seleccion == 2:
            MenuProveedores()
        elif seleccion == 3:
            MenuVentas()
        elif seleccion == 4:
            print("Guardando cambios...")
            print("Cerrando Sitema...")
            cerrar()
            break
            
        else:
            print("Opcion invalida, vuelve a intentar de nuevo.")


def MenuProductos():
    producto = Producto()
        
    while True:
        print("- - - - > Gestion de Productos < - - - -")
        print("[1].Agregar Producto.")
        print("[2].Ver todos los Productos.")
        print("[3].Eliminar un Producto.")
        print("[4].Modificar un Producto.")
        print("[5].Ver los Productos con bajo stock.")
        print("[6].Ver el valor total del Inventario.")
        print("[7].Volver al Menu Principal.")
        operacion = int(input("Seleccione una Operacion: "))

        if operacion == 1:
            print("- - - - > Agregar Producto < - - - -")
            nombre = str(input("-Introduzca el nombre del Producto: "))
            marca = str(input("-Introduzca la marca del Producto: "))
            precio = float(input("-Introduzca el precio del Producto: "))
            stock = int(input("-Introduzca la cantidad de unidades del Producto: "))
            id_proveedor = int(input("-Introduzca la id del Proveedor: "))
            producto.AgregarProducto(nombre, marca, precio, stock, id_proveedor)
            print(">>> Producto agregado correctamente <<<")
            
        elif operacion == 2:
            print("- - - - > tabla Producto < - - - -")
            productos = Producto()
            for producto in productos.MostrarProducto():
                print(producto)
            print("- - - - - - - -")

        elif operacion == 3:
            print("- - - - > Eliminar Producto < - - - -")
            id_producto = input("-Inserte la ID del Producto que desea Eliminar:  ")
            producto.EliminarProducto(id_producto)
            print(">>> Producto eliminado con exito <<<")
            
        elif operacion == 4:
            print("- - - - > Modificar Producto < - - - -")
            id_producto = str(input("-Inserte la ID del Producto a modificar: "))
            nombreModificado = str(input("-Modificacion del nombre del Producto: "))
            marcaModificado = str(input("-Modificacion de la marca del Producto: "))
            precioModificado = float(input("-Modificacion del precio del Producto: "))
            stockModificado = int(input("-Modificacion de la cantidad de unidades del Producto: "))
            idProveedorModificado = int(input("-Modificacion de la ID del Proveedor: "))
            producto.ModificarProducto(id_producto, nombreModificado, marcaModificado, precioModificado, stockModificado, idProveedorModificado)
            print(">>> Producto modificado con exito <<<")
            
        elif operacion == 5:
            print("- - - - > Productos con bajo stock < - - - -")
            bajoStock = producto.Productos_bajo_stock()
            for i in bajoStock:
                print(i)
            print("- - - - - - - -")
            
        elif operacion == 6:
            print("- - - - > Valor Total del Inventario < - - - -")
            valorTotal = producto.ValorTotal_delInventario()
            print(f"El valor total del inventario es de: {valorTotal} ARS")
            print("- - - - - - - -")

        elif operacion == 7:
            print("Volviendo...")
            break
            
        else:
            print("Opcion invalida, vuelve a intentar de nuevo")

def MenuProveedores():
        proveedor = Proveedor()
        while True:
            print("- - - - > Gestion de Proveedores < - - - -")
            print("[1].Agregar Proveedor.")
            print("[2].Ver todos los Proveedores.")
            print("[3].Eliminar un Proveedor.")
            print("[4].Modificar un Proveedor.")
            print("[5].Volver al Menu Principal.")
            operacion = int(input("Seleccione una Operacion: "))

            if operacion == 1:
                print("- - - - > Agregar Proveedor < - - - -")
                nombreEmpresa = str(input("-Introduzca el nombre de la empresa: "))
                nombreProducto = str(input("-Introduzca la el nombre del producto que Provee: "))
                contacto = str(input("-Introduzca el contacto del Proveedor(10 Digitos): "))
                proveedor.AgregarProveedor(nombreEmpresa, nombreProducto, contacto)
                print(">>> Proveedor agregado correctamente <<<")
            
            elif operacion == 2:
                print("- - - - > tabla Proveedor < - - - -")
                infoProveedor = proveedor.MostrarProveedores()
                for i in infoProveedor:
                    print(i)
                print("- - - - - - - -")

            elif operacion == 3:
                print("- - - - > Eliminar Proveedor < - - - -")
                id_proveedor = str(input("-Inserte la ID del Proveedor que desea Eliminar:  "))
                proveedor.EliminarProveedor(id_proveedor)
                print(">>> Proveedor eliminado con exito <<<")
            
            elif operacion == 4:
                print("- - - - > Modificar Proveedor < - - - -")
                id_proveedor = str(input("-Inserte la ID del Proveedor a modificar: "))
                nombreEmpresaModificado = str(input("-Modificacion del nombre de la empresa: "))
                nombreProductoModificado = str(input("-Modificacion del Producto que provee: "))
                contacto = str(input("-Modificacion del contacto(10 Digitos): "))
                proveedor.ModificarProveedor(id_proveedor, nombreEmpresaModificado, nombreProductoModificado, contacto)
                print(">>> Proveedor modificado con exito <<<")

            elif operacion == 5:
                print("Volviendo...")
                break
            
            else:
                print("Opcion invalida, vuelve a intentar de nuevo.")

def MenuVentas():
    venta = Venta()
    while True:
            print("- - - - > Gestion de Ventas < - - - -")
            print("[1].Agregar Venta.")
            print("[2].Ver todas las Ventas.")
            print("[3].Eliminar una Venta.")
            print("[4].Modificar una Venta.")
            print("[5].Ver ultimas 5 ventas.")            
            print("[6].Volver al Menu Principal.")
            operacion = int(input("Seleccione una Operacion: "))

            if operacion == 1:
                print("- - - - > Agregar venta < - - - -")
                id_productoV = int(input("-Introduzca la ID del producto: "))
                id_proveedorV = int(input("-Introduzca la ID del Proveedor: "))
                fecha = str(input("-Introduzca la fecha de la Venta(DD-MM-AAAA): "))
                cantidad = int(input("-Introduzca la cantidad de unidades vendidas: "))
                precioPU = float(input("-Introduzca el precio p/u del Producto: "))
                valorTotal_deLaVenta = float(input("-Introduzca el valor total de la Venta: "))
                venta.AgregarVenta(id_productoV, id_proveedorV, fecha, cantidad, precioPU, valorTotal_deLaVenta)
                print(">>> Venta agregada correctamente <<<")
            
            elif operacion == 2:
                print("- - - - > tabla Venta < - - - -")
                infoVentas = venta.MostrarVentas()
                for i in infoVentas:
                    print(i)
                print("- - - - - - - -")

            elif operacion == 3:
                print("- - - - > Eliminar Venta < - - - -")
                id_venta = str(input("-Inserte la ID de la Venta que desea Eliminar:  "))
                venta.EliminarVenta(id_venta)
                print(">>> Venta eliminada con exito <<<")
            
            elif operacion == 4:
                print("- - - - > Modificar Venta < - - - -")
                id_venta = str(input("-Introduzca la ID de la venta a Modificar: "))
                id_productoVModificado = int(input("-Modificacion de la nueva ID del producto: "))
                id_proveedorVModificado = int(input("-Modificacion de la nueva ID del Proveedor: "))
                fechaModificado = str(input("-Modificacion de la fecha de la Venta: "))
                cantidadModificado = int(input("-Modificacion de la cantidad de unidades vendidas: "))
                precioPUModificado = float(input("-Modificacion del precio p/u del Producto: "))
                valorTotal_deLaVentaModificado = float(input("-Modificacion del valor total de la Venta: "))
                venta.ModificarVenta(id_venta, id_productoVModificado, id_proveedorVModificado, fechaModificado, cantidadModificado, precioPUModificado, valorTotal_deLaVentaModificado)
                print(">>> Venta modificada con exito <<<")

            elif operacion == 5:
                print("- - - - > Ultimas 5 Ventas < - - - -")
                ultimasVentas = venta.Ultimas_5_Ventas()
                for i in ultimasVentas:
                    print(i)
                print("- - - - - - - -")
            elif operacion == 6:
                print("Volviendo...")
                print("- - - - - - - -")
                break
            
            else:
                print("Opcion invalida, vuelve a intentar de nuevo.")
                print("- - - - - - - -")
        

if __name__ == "__main__":
     main()
            
            
