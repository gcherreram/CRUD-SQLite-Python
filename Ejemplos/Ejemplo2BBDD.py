import sqlite3

miConexion=sqlite3.connect("Gestion_Productos")

miCursor=miConexion.cursor()

# ---------------------------- read --------------------------------

# miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'")

# productos=miCursor.fetchall()
# print(productos)        

# --------------------------- update -------------------------------

# miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

# ---------------------------- Delete --------------------------------------------

miCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO='pantalones'")

# --------------------------- Create --------------------------------

# Con primary key permitira dejar un campo clave, esto permitira integridad en la información
# No repetir la información de la llave principal
# miCursor.execute('''
#     CREATE TABLE PRODUCTOS (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#     PRECIO INTEGER,
#     SECCION VARCHAR(20))
#  ''')

# productos=[

#     ("pelota", 20, "Juguetería"),
#     ("pantalón", 15, "confección"),
#     ("destornillador", 25, "ferretería"),
#     ("jarrón", 45, "cerámica"),
#     ("pantalones", 35, "confección")

# ]

# Un interrogante por cada dato en fila, es decir 3 datos por fila/tupla estamos pasando
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miConexion.commit()

miConexion.close()