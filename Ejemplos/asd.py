
from BaseDeDatos import *
from tkinter import *
from tkinter import messagebox
import sqlite3


raiz=Tk()
raiz.title("Base de datos")
raiz.geometry("270x355")

miFrame=Frame()
miFrame.pack()

miFrame2=Frame()
miFrame2.pack()

raiz.resizable(0,0)


# ------------------------ RECUADRO DE ESCRITURA ----------------------------

manipulaPantalla1=StringVar()
manipulaPantalla2=StringVar()
manipulaPantalla3=StringVar()
manipulaPantalla4=StringVar()
manipulaPantalla5=StringVar()

ID=Entry(miFrame, textvariable=manipulaPantalla1)
ID.grid(row=0, column=1, padx=0, pady=10)
ID.config(fg="red", justify="center")

nombre=Entry(miFrame, textvariable=manipulaPantalla2)
nombre.grid(row=1, column=1, padx=0, pady=12)

Pass=Entry(miFrame, textvariable=manipulaPantalla3)
Pass.grid(row=2, column=1, padx=0, pady=9)
Pass.config(show="●")

apellido=Entry(miFrame, textvariable=manipulaPantalla4)
apellido.grid(row=3, column=1, padx=0, pady=13)

direccion=Entry(miFrame, textvariable=manipulaPantalla5)
direccion.grid(row=4, column=1, padx=0, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=0, pady=11)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

# -------------------------- NOMBRE DE RECUADRO -------------------------------

idLabel=Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0,  padx=15, pady=5,)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, padx=15, pady=5)

passLabel=Label(miFrame, text="Password: ")
passLabel.grid(row=2, column=0, padx=15, pady=5)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, padx=15, pady=5)

direccionLabel=Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=4, column=0, padx=15, pady=5)

comentarioLabel=Label(miFrame, text="Comentarios: ")
comentarioLabel.grid(row=5, column=0, padx=15, pady=5)


# --------------------------- INTERFAZ INTERACCIÓN ----------------------------


def ingresarInfo(): # Funciona bien

	siempreIntentarCrear() # Intenta crear el archivo de base de datos por si el archivo ha sido borrado mientras el programa estaba abierto y evitar un error

	variosProductos=[(manipulaPantalla2.get(), manipulaPantalla3.get(), manipulaPantalla4.get(), manipulaPantalla5.get(), "Todavía no sé manipular caja comentario")]

	miConexion=sqlite3.connect("DATOS_USUARIO.db")
	miCursor=miConexion.cursor()

	if manipulaPantalla2.get()==("") or manipulaPantalla3.get()==("") or manipulaPantalla4.get()==("") or manipulaPantalla5.get()==(""):
		messagebox.showinfo("Campo Vacío", "Uno o más campos están vacíos")
		return

	miCursor.executemany("INSERT INTO NOMBREUSUARIOS VALUES (NULL,?,?,?,?,?)", variosProductos)

	miConexion.commit()
	miConexion.close()

	messagebox.showinfo("Información", "Datos introducidos correctamente")
	eliminarInfoPantalla()

crearEnvio=Button(miFrame2, text="Create", command=ingresarInfo)
crearEnvio.grid(row=0, column=0, padx=9, pady=10)


def readBoton(): # ¡Funciona Perfecto!, la función que se me hizo más difícil y compleja, ya que quise capturar todos los errores / excepciones


	ExtraidoID=(manipulaPantalla1.get())

	if 	ExtraidoID.isdigit():
		soloComparativaExtraidoID=int(ExtraidoID)

	try:
		negativoExtraidoID=float(manipulaPantalla1.get())
		if negativoExtraidoID <1:
			messagebox.showinfo("ID Negativo", "El ID no puede ser cero o negativo")

			return
	
	except Exception:
		pass

	# miConexion=sqlite3.connect("DATOS_USUARIO.db")
	# miCursor=miConexion.cursor()
	# miCursor.execute ("SELECT count(ID) FROM NOMBREUSUARIOS") # Con count se va todo a la mi*rda, ya que si borras un registro y consultas
	# el último registro te dirá que no existe, ya hay mucho código, así que se queda así, por ahora... No encontré un 
	# sustituto de count para que me devolviese el valor de cada ID... LO SOLUCIONÉ DESPUÉS DE MUUUCHO!! CÓDIGO COMENTADO :D

	# for recorre in miCursor:

	#	convertirRecorre=list(recorre)

	#	cursorIdTotal=convertirRecorre[0] 

	try:

		if ExtraidoID.isalpha():
			print("El ID solo admite números, no letras")
			messagebox.showinfo("Error", "Letras no admitidas, ID solo admite números")
		
		
		# elif cursorIdTotal < soloComparativaExtraidoID: # Intenté agregar también un "or" para saber si el número intruducido era cero o negativo <1:,
		# lo intenté de muchas formas, creando otro elif, un try etc, estuve varios días intentándolo, al final me rendí ya que todo se iba a la mi*rda
		# YA NO NECESARIO, CÓDIGO PERTENECIENTE AL COMENTADO EN LINEA COMENTADA 118

			# print("Consola: No se encuentra en la Base de Datos")
			# messagebox.showinfo("ID no disponible", "ID no se encuentra en la Base de Datos")


		elif ExtraidoID.isdigit():

			miConexion=sqlite3.connect("DATOS_USUARIO.db")
			miCursor=miConexion.cursor()

			miCursor.execute("SELECT * FROM NOMBREUSUARIOS WHERE ID=" + ExtraidoID)
			# Descubrí que "+" le suma o concatena, pero si pongo la "," no funciona Mmmm... estaba poniendo un "?" pero solo aceptaba un dígito
			manipulame=miCursor.fetchall()

    for recorre in manipulame:
    
				ManipulameLista=list(recorre)
				ComparaManipulameID=ManipulameLista[0]


			if soloComparativaExtraidoID == ComparaManipulameID:
				for recorre in manipulame:

					ID, nombre, Pass, apellido, direccion, textoComentario=recorre

					manipulaPantalla1.set(ID)
					manipulaPantalla2.set(nombre)
					manipulaPantalla3.set(Pass)
					manipulaPantalla4.set(apellido)
					manipulaPantalla5.set(direccion)
					miConexion.close()


		else:
			print("Ha ocurrido un Error ")
			messagebox.showinfo("Error Desconocido", """● Posibles errores ●

        - Campo ID vacio
        - Espacios en blanco
        - Símbolos !@#$%&*
        - Alfanuméricos

        ID solo admite números positivos""")

        except Exception:
            messagebox.showinfo("NO ID", "ID no se encuentra en la Base de Datos")

readEnvio=Button(miFrame2, text="Read", command=readBoton)
readEnvio.grid(row=0, column=1, padx=9, pady=10)


def updateBoton(): # funciona bien

	siempreIntentarCrear()

	dameInfoID=manipulaPantalla1.get()
	variosProductos=manipulaPantalla2.get(), manipulaPantalla3.get(), manipulaPantalla4.get(), manipulaPantalla5.get()

	miConexion=sqlite3.connect("DATOS_USUARIO.db")
	miCursor=miConexion.cursor()

	miCursor.execute("UPDATE NOMBREUSUARIOS SET NOMBRE_USUARIO='" + variosProductos[0] + "' , PASSWORD='" + variosProductos[1] + "', APELLIDO='" + variosProductos[2] + "', DIRECCION='" + variosProductos[3] + "' WHERE ID=" + dameInfoID)
	
	messagebox.showinfo("BBDD Update", "Base de Datos actualizada con éxito")


	miConexion.commit()
	miConexion.close()

updateEnvio=Button(miFrame2, text="Update", command=updateBoton)
updateEnvio.grid(row=0, column=2, padx=9, pady=10)


def deleteBoton(): # Funciona bien

	siempreIntentarCrear()

	valor=messagebox.askquestion("Borrar", """¿Desea continuar con la eliminación?""")

	if valor=="yes":

		variosProductos=[(manipulaPantalla1.get())]

		miConexion=sqlite3.connect("DATOS_USUARIO.db")
		miCursor=miConexion.cursor()

		miCursor.execute("DELETE FROM NOMBREUSUARIOS WHERE ID=?", variosProductos)

		miConexion.commit()
		miConexion.close()

		messagebox.showinfo("Borrar", "Si introdujo bien el ID ¡El registro ha sido borrado!")

		eliminarInfoPantalla()

borrarEnvio=Button(miFrame2, text="Delete", command=deleteBoton)
borrarEnvio.grid(row=0, column=3, padx=9, pady=10)



def salirAplicacion():
	valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
	# valor=messagebox.askokcancel("Salir", "Deseas salir de la aplicación")

	if valor=="yes":
		raiz.destroy()



def eliminarInfoPantalla():

	manipulaPantalla1.set("")
	manipulaPantalla2.set("")
	manipulaPantalla3.set("")
	manipulaPantalla4.set("")
	manipulaPantalla5.set("")

def licencia():
	messagebox.showinfo("¡Licencia!", """Gracias por confiar en nosotros

     Licencia para: misterioszg
Serial: BD-S4PRN-81FNG-NE3QG""")

def acercaDe():
	messagebox.showinfo("Sobre el programa", """Programa creado por misterioszg 
      Para PíldorasInformáticas
  Gracias por este regalo/curso""")



# ---------------------------- MENÚ SUPERIOR ------------------------------------


barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

MenuBBDD=Menu(barraMenu, tearoff=0)
MenuBBDD.add_command(label="Conectar", command=coneCrear)
MenuBBDD.add_command(label="Salir", command=salirAplicacion)

# ==========================================================

MenuBorrar=Menu(barraMenu, tearoff=0)
MenuBorrar.add_command(label="Borrar campos", command=eliminarInfoPantalla)

# ==========================================================

MenuCRUD=Menu(barraMenu, tearoff=0)
MenuCRUD.add_command(label="Crear", command=ingresarInfo)
MenuCRUD.add_command(label="Leer", command=readBoton)
MenuCRUD.add_command(label="Actualizar", command=updateBoton)
MenuCRUD.add_command(label="Borrar", command=deleteBoton)

# ==========================================================

MenuAyuda=Menu(barraMenu, tearoff=0)
MenuAyuda.add_command(label="Licencia", command=licencia)
MenuAyuda.add_command(label="Acerca de...", command=acercaDe)
MenuAyuda.add_separator()


barraMenu.add_cascade(label="BBDD", menu=MenuBBDD)
barraMenu.add_cascade(label="Borrar", menu=MenuBorrar)
barraMenu.add_cascade(label="CRUD", menu=MenuCRUD)
barraMenu.add_cascade(label="Ayuda", menu=MenuAyuda)


raiz.mainloop()