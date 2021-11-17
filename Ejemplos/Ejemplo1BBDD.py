# ---------------- Pasos a seguir para conectar con BBDD --------------

# 1. Abrir - crear conexión
# 2. Crear Puntero
# 3. Ejecutar query(consulta) SQL
# 4. Manejar los resultados de la query
#     4.1 Insertar, leer, actualizar, borrar (CRUD, create, read, update, delete)
# 5. Cerrar puntero
# 6. Cerrar conexión

import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

# ---------------- --Para crear la tabla:--------------------
# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# --------------Insertar un solo registro----------------------
# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

# -------------Esto para insertar varios productos----------------
# variosProductos=[

#     ("Camiseta", 10, "Deportes"),
#     ("Jarrón", 90, "Cerámica"),
#     ("Camión", 20, "Juguetería")

# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

# ------------------ obtener información de la tabla -------------------

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall()

for producto in variosProductos:

    print("Nombre Articulo: ", producto[0], " Sección: ", producto[2])

miConexion.commit()

miConexion.close()