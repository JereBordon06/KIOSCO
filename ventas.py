from KioscoDB import conn
from KioscoDB import cursor

class Venta:

    def AgregarVenta(self, id_producto, id_proveedor, fecha, cantidad, PrecioPorU, valorTotal):
        cursor.execute("INSERT INTO ventas(id_producto, id_proveedor, fecha, cantidad, PrecioPorU, valorTotal) VALUES(?, ?, ?, ?, ?, ?)", (id_producto, id_proveedor, fecha, cantidad, PrecioPorU, valorTotal))
        conn.commit()

    def MostrarVentas(self):
        cursor.execute("SELECT * FROM ventas")
        return cursor.fetchall()
    
    def EliminarVenta(self, id_venta):
        cursor.execute("DELETE FROM ventas WHERE id_ventas ="+id_venta)
        conn.commit()

    def ModificarVenta(self, id_venta, id_producto, id_proveedor, fecha, cantidad, PrecioPorU, valorTotal):
        cursor.execute("UPDATE ventas SET id_producto = ?, id_proveedor = ?, fecha = ?, cantidad = ?, PrecioPorU = ?, valorTotal = ? WHERE id_venta="+id_venta,(id_producto, id_proveedor, fecha, cantidad, PrecioPorU, valorTotal))
        conn.commit()
    
    def Ultimas_5_Ventas(self):
        cursor.execute("SELECT * FROM ventas ORDER BY id_venta DESC LIMIT 5")
        return cursor.fetchall()
    