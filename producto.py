from KioscoDB import conn
from KioscoDB import cursor

class Producto:

    def AgregarProducto(self, nombre, marca, precio, stock, id_proveedor):
        cursor.execute("INSERT INTO producto(nombre, marca, precio, stock, id_proveedor) VALUES(?, ?, ?, ?, ?)", (nombre, marca, precio, stock, id_proveedor))
        conn.commit()


    def MostrarProducto(self):
        cursor.execute("SELECT * FROM producto")
        return cursor.fetchall()
        
    
    def EliminarProducto(self, id_porducto):
        cursor.execute("DELETE FROM producto WHERE id_producto ="+id_porducto)
        conn.commit()

    def ModificarProducto(self, id_producto, nombre, marca, precio, stock, id_proveedor):
        cursor.execute("UPDATE producto SET nombre = ?, marca = ?, precio = ?, stock= ?, id_proveedor= ? WHERE id_producto="+id_producto,(nombre, marca, precio, stock, id_proveedor))
        conn.commit()
    
    def Productos_bajo_stock(self):
        cursor.execute("SELECT * FROM producto WHERE stock < 10")
        return cursor.fetchall()
    
    
    def ValorTotal_delInventario(self):
        resultado = cursor.execute("SELECT (precio * stock) FROM producto")
        return resultado
    
    
