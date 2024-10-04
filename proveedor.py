from KioscoDB import conn
from KioscoDB import cursor

class Proveedor:

    def AgregarProveedor(self, empresa, nombreProd, contacto):
        cursor.execute("INSERT INTO proveedores(empresa, nombreProd, contacto) VALUES(?, ?, ?)", (empresa, nombreProd, contacto))
        conn.commit()

    def MostrarProveedores(self):
        cursor.execute("SELECT * FROM proveedores")
        return cursor.fetchall()
    
    def EliminarProveedor(self, id_proveedor):
        cursor.execute("DELETE FROM proveedores WHERE id_proveedor ="+id_proveedor)
        conn.commit()

    def ModificarProveedor(self,id_proveedor, empresa, nombreProd, contacto):
        cursor.execute("UPDATE proveedores SET empresa = ?, nombreProd = ?, contacto = ? WHERE id_proveedor="+id_proveedor,(empresa, nombreProd, contacto))
        conn.commit()
        