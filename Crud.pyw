from tkinter import *
from tkinter import messagebox
import sqlite3

# ------------------------------ Funciones-------------------------
def conectar():
    
    miConection=sqlite3.connect("Usuarios")
    miCursor=miConection.cursor()
 
    try:
        miCursor.execute('''CREATE TABLE DATOSUSUARIOS (
		ID INTEGER PRIMARY KEY,
		NOMBRE_USUARIO VARCHAR(50),
        PASSWORD VARCHAR(50), 
        APELLIDO VARCHAR(10), 
        DIRECCION VARCHAR(50),
        COMENTARIOS VARCHAR (100))
        ''')

        messagebox.showinfo("BASE","Tabla creada con exito")
        miConection.close()

    except:
        pass
        # messagebox.showwarning("!Atención¡", "La BBDD ya existe")

def salirAplicacion():
    valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")

    if valor == True:
        root.destroy()

def borrarCampos():
    
    strId.set("")
    strNombre.set("")
    strPassword.set("")
    strApellido.set("")
    strDireccion.set("")
    textoComentario.delete(1.0, END)

def infoAdicional():
    messagebox.showinfo("Procesador de gabriel", "Procesador de textos version 2018")

def avisoLicencia():
    messagebox.showwarning("Licencia","producto bajo licencia GNU")


def CRUD(opcion):

    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    
    if strNombre!="" and strPassword!="" and strApellido!="" and strDireccion!="":
        if opcion=="CREAR":
            conectar()
            datos=strNombre.get(), strPassword.get(), strApellido.get(), strDireccion.get(), textoComentario.get("1.0",END)
            miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (datos))
            # miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + strNombre.get() +
            #     "','" + strPassword.get() +
            #     "','" + strApellido.get() +
            #     "','" + strDireccion.get() +
            #     "','" + textoComentario.get ("1.0", END) + "')")
            miConexion.commit()
            borrarCampos()

            messagebox.showinfo("BBDD", "Registro creado con exito")
        elif opcion=="LEER":
            miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + strId.get())

            elUsuario=miCursor.fetchall()

            for usuario in elUsuario:
                
                strId.set(usuario[0])
                strNombre.set(usuario[1])
                strPassword.set(usuario[2])
                strApellido.set(usuario[3])
                strDireccion.set(usuario[4])
                textoComentario.insert(1.0, usuario[5])
            
            miConexion.commit()

        elif opcion=="ACTUALIZAR":
            datos=strNombre.get(), strPassword.get(), strApellido.get(), strDireccion.get(), textoComentario.get("1.0",END)
            
            # ------------ FORMA PARA EVITAR INYECCIÓN SQL ------------------
            miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? " +
            "WHERE ID=" + strId.get(), (datos))
            
            # --------------- FORMA ANIDADA FALLA POR INYECCIÓN SQL-----------------
            # miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + strNombre.get() +
            # "', PASSWORD='" + strPassword.get() +
            # "', APELLIDO='" + strApellido.get() +
            # "', DIRECCION='" + strDireccion.get() +
            # "', COMENTARIOS='" + textoComentario.get("1.0", END) +
            # "' WHERE ID=" + strId.get())
            
            miConexion.commit()

            messagebox.showinfo("BBDD", "Registro actualizado con exito")

        elif opcion=="BORRAR":
            miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + strId.get())

            miConexion.commit()

            messagebox.showinfo("BBDD", "Registro borrado con exito")
            borrarCampos()

    else:
        messagebox.showwarning("Error", "Hay campos vacios en el formulario")
        
# ------------------------------ Barra Menu --------------------------

root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoBBDD=Menu(barraMenu, tearoff=0)
archivoBBDD.add_command(label="Conectar", command=conectar)
archivoBBDD.add_command(label="Salir", command=salirAplicacion)

archivoBorrar=Menu(barraMenu, tearoff=0)
archivoBorrar.add_command(label="Borrar Campos", command=borrarCampos)

archivoCrear=Menu(barraMenu, tearoff=0)
archivoCrear.add_command(label="Crear", command=lambda:CRUD("CREAR"))
archivoCrear.add_command(label="Leer", command=lambda:CRUD("LEER"))
archivoCrear.add_command(label="Actualizar", command=lambda:CRUD("ACTUALIZAR"))
archivoCrear.add_command(label="Borrar", command=lambda:CRUD("BORRAR"))

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="BBDD", menu=archivoBBDD)
barraMenu.add_cascade(label="Borrar", menu=archivoBorrar)
barraMenu.add_cascade(label="CRUD", menu=archivoCrear)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

# ----------------------------- Labels -------------------------------

miFrame=Frame(root, width=600, height=600)
miFrame.pack()  

strId=StringVar()
strNombre=StringVar()
strPassword=StringVar()
strApellido=StringVar()
strDireccion=StringVar()

cuadroId=Entry(miFrame, textvariable=strId)
cuadroId.grid(row=0, column=1, padx=10, pady=10)
cuadroId.config(fg="Black", bg="#9bf6ff")

cuadroNombre=Entry(miFrame, textvariable=strNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="Blue")

cuadroPassword=Entry(miFrame, show="*", textvariable=strPassword)
cuadroPassword.grid(row=2, column=1, padx=10, pady=10)
cuadroPassword.config(fg="Black")

cuadroApellido=Entry(miFrame, textvariable=strApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)
cuadroApellido.config(fg="Blue")

cuadroDirección=Entry(miFrame, textvariable=strDireccion)
cuadroDirección.grid(row=4, column=1, padx=10, pady=10)
cuadroDirección.config(fg="black")

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

IdLabel=Label(miFrame, text="Id:")
IdLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passwordLabel=Label(miFrame, text="Password:")
passwordLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel=Label(miFrame, text="Comentarios:")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# ---------------------- Botones ------------------------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCreate=Button(miFrame2, text="Create", width=5, command=lambda:CRUD("CREAR"))
botonCreate.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonRead=Button(miFrame2, text="Read", width=5, command=lambda:CRUD("LEER"))
botonRead.grid(row=1, column=1, padx=10, pady=10)

botonUpdate=Button(miFrame2, text="Update", width=5, command=lambda:CRUD("ACTUALIZAR"))
botonUpdate.grid(row=1, column=2, padx=10, pady=10)

botonDelete=Button(miFrame2, text="Delete", width=5, command=lambda:CRUD("BORRAR"))
botonDelete.grid(row=1, column=3, padx=10, pady=10)

root.mainloop()