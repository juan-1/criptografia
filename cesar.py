#Script para cifrado del Cesar
#===========================Bibliotecas==============================
from colorama import Fore, init, Style, Back, Cursor	#para cambiar de color y formato las impresiones en consola //no es estandar
import subprocess  										#para ejecutar comandos del sistema operativo o lanzar programas
from time import sleep
#==========================VAR Globales==============================
borra = 0
#==========================Funciones=================================
def borra_pantalla(): #función para limpiar la consola
	subprocess.run("cls", shell=True)

def cifrar():
	cadena = input("por favor ingrese la cadena a cifrar: ")
	lista = list(cadena)
	lista_c = []
	for x in lista:
		lista_c.append(chr(ord(x)+3))
	print("".join(lista_c))
	sleep(4)

def descifrar():
	cadena = input("por favor ingrese la cadena a descifrar: ")
	lista = list(cadena)
	lista_d = []
	for x in lista:
		lista_d.append(chr(ord(x)-3))
	print("".join(lista_d))
	sleep(2)

def ayuda():
	print("Es un tipo de cifrado por sustitución en el que una letra en", 
		"el texto original es reemplazada por otra letra\nque se encuentra",
		"un número fijo de posiciones más adelante en el alfabeto.",
		"Por ejemplo, con un desplazamiento de 3,\nla A sería sustituida por la D",
		"(situada 3 lugares a la derecha de la A ), la B sería reemplazada por la E,",
		"etc.\nEste método debe su nombre, según Suetonio, a Julio César, que lo usaba",
		"para comunicarse con sus generales.")
	sleep(5)

def opcion(opc): #función para seleccionar opciones
	if opc == "1":
		cifrar()
	elif opc == "2":
		descifrar()
	elif opc == "ayuda":
		ayuda()
	else:
		print(Fore.RED+"\topcion invalida...!")
		sleep(1)

def control():
	global borra
	borra_pantalla()
	print(Cursor.DOWN(2)+Cursor.FORWARD(10)+Style.BRIGHT+Fore.YELLOW+">>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>> Algoritmo de cifrado <<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>>>> Cesar <<<<<<<<<<<<<<<<<<")
	while True:
		if(borra != 0):
			borra_pantalla()
		print(Cursor.DOWN(2)+Cursor.FORWARD(10)+Style.BRIGHT+Fore.BLUE+"********************* OPCIONES *******************\n")
		print(" 1 => cifra una cadena")
		print(" 2 => Descifra una cadena")
		print(" ayuda => AYUDA")
		print(" salir => SALIR\n")
		opc=input(Fore.GREEN+" ~ $"+Style.RESET_ALL)
		if opc== "salir":
			break
		opcion(opc)
		borra+=1

control()
