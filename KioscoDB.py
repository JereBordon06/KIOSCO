import _sqlite3
conn = _sqlite3.connect("Kiosco.db")
cursor = conn.cursor()


cursor.execute('CREATE TABLE IF NOT EXISTS producto(id_producto INTEGER PRIMARY KEY, nombre TEXT, marca TEXT, precio INTEGER NUMBER, stock INTEGER NUMBER, id_proveedor, FOREIGN KEY (id_proveedor)REFERENCES proveedores(id_proveedor))')
cursor.execute('CREATE TABLE IF NOT EXISTS proveedores(id_proveedor INTEGER PRIMARY KEY, empresa TEXT, nombreProd TEXT, contacto INTEGER NUMBER)')
cursor.execute('CREATE TABLE IF NOT EXISTS ventas(id_venta INTEGER PRIMARY KEY, id_producto INTEGER NUMBER, id_proveedor INTEGER NUMBER, fecha TEXT, cantidad INTEGER NUMBER, precioPorU INTEGER NUMBER, valorTotal INTEGER NUMBER, FOREIGN KEY (id_producto) REFERENCES producto(id_producto), FOREIGN KEY (id_proveedor)REFERENCES proveedores(id_proveedor))')
conn.commit()
def cerrar():
    conn.close()
    