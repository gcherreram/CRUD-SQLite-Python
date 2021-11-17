# Para generar ejecutables abrimos la consola del sistema operativo
# usaremos la instrucción pyinstaller en el path donde me encuentre, seguido
# un espacio y el nombre del archivo que quiero convertir: 

# C:\Users\Gabo0\Desktop\Python\graficas>pyinstaller calculadora.py

# Esto me genera varias carpetas, me centrare en la carpeta dist ya que 
# allí esta el aplicativo (Me abrira el programa con una ventana de consola)

# Para que la ventana de consola no aparezca, si no que se abra solo
# el programa, debere añadirle a la instrucción un comando más
# C:\Users\Gabo0\Desktop\Python\graficas>pyinstaller --windowed calculadora.py

# Para comprimir más el archivo y que no me aparezcan tantos archivos adicionales
# debo ingresar otro comando más en la instrucción
# C:\Users\Gabo0\Desktop\Python\graficas>pyinstaller --windowed --onefile practicaCalculadora.py