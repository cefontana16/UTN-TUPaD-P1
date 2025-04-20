#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.


#Solicitar datos al usuario
edad = (int(input("Ingrese su edad: ")))

#verificar si es mayor de edad
if edad > 18:
    print ("Es mayor de edad")
else:
    print("Es menor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”. 

#Solicitar nota al usuario y convertir a float
nota = (float(input("Ingrese su nota: ")))

#Verificar si la nota es suficiente para aprobar (mayor o igual a 6)
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar.

#Solicitar dato al usuario
numero = int(input("Ingrese un número par: "))

#Comprobar si el número es par
if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor: ingrese un número par")

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años. """

#Solicitar ingreso de datos.
edad = int(input("Ingrese su edad: "))

#Comprobar la categoría según la edad ingresada
if edad > 0 and edad < 12:
    print (" Categoría: Niño/a.")
elif edad >= 12 and edad < 18:
    print (" Categoría Adolescente.")
elif edad >=18 and edad < 30:
    print ("Categoría Adulto/a joven. ")
else:
    print ("Categoría Adulto/a. ")

"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
como una lista o un string. """

#Solicitar datos
contraseña = str(input("Ingrese una contraseña de entre 8 y 14 caracteres: "))

#Comprobando contraseña
if len(contraseña) >=8 and len(contraseña) <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")




"""6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
siguiente: 
from statistics import mode, median, mean 
mi_lista = [1,2,5,5,3] 
mean(mi_lista) 
En la documentación oficial se puede encontrar más información sobre este paquete: 
https://docs.python.org/es/3.8/library/statistics.html.  
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
mediana es mayor que la moda. 
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
la mediana es menor que la moda. 
● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
Definir la lista numeros_aleatorios de la siguiente forma: 
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
forma aleatoria. """


#importar modulo 
import random 

#definir la lista de numeros aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(10)]
print ("Los números son: ", numeros_aleatorios)

#Ordenar la lista anterior
numeros_aleatorios.sort()
print ("Los números ordenados son: ", numeros_aleatorios)

#calcular media, mediana y moda.
from statistics import mean, median, mode 
media = mean(numeros_aleatorios)
print (f"la media es:  {media}")
mediana = median(numeros_aleatorios)
print (f"la mediana es: {mediana}")
moda = mode(numeros_aleatorios)
print (f"la moda es:  {moda}")

#Determinar el sesgo 
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print ("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    pass







"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla. """

#Solicitar frase
frase = input("Ingrese una frase o palabra: ")

#Determinar si termina en vocal
if frase [-1] in "aeiouAEIOU":
    print (f"{frase}!")
else:
    print (frase)

"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
lower() y title() de Python para convertir entre mayúsculas y minúsculas. """

#Solicitar datos.
nombre = input("Ingrese su nombre: ")
print ("Seleccione una opción: ")
print ("1. Si quiere su nombre en mayúsculas.")
print ("2. Si quiere su nombre en minúsculas.")
print ("3. Si quiere su nombre con la primera letra mayúscula.")
opcion = int(input ("Ingrese el número de opción seleccionada (1, 2 o 3): "))

#Transformar datos según la opción elegida
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print (nombre.lower())
elif opcion == 3:
    print (nombre.title())
else:
    print ("Debe elegir la opcion 1, 2 ó 3")


"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla: 
● Menor que 3: "Muy leve" (imperceptible). 
● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
generalmente no causa daños). 
● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
débiles). 
● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). """

#Solicitar dato
terremoto = int(input("Ingrese la magnitud del terremoto: "))

#Determinar la magnitud
if terremoto < 3:
    print ("La magnitud es: Muy leve (imperceptible).")
elif terremoto >= 3 and terremoto < 4:
    print ("La magnitud es: Leve (ligeramente perceptible). ")
elif terremoto >= 4 and terremoto < 5:
    print ("La magnitud es: Moderado (sentido por personas, pero generalmente no causa daños).")
elif terremoto >= 5 and terremoto <6:
    print ("La magnitud es: Fuerte (puede causar daños en estructuras débiles). ")
elif terremoto >= 6 and terremoto < 7:
    print ("La magnitud es: Muy Fuerte (puede causar daños significativos). ")
elif terremoto >= 7:
    print ("La magnitud es: Extremo (puede causar graves daños a gran escala).")

    


"""10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
Periodo del año /Estación en el hemisferio norte /Estación en el hemisferio sur 
Desde el 21 de diciembre hasta el 20 de marzo (incluidos)/ Invierno / Verano 
Desde el 21 de marzo hasta el 20 de junio (incluidos)/  Primavera / Otoño 
Desde el 21 de junio hasta el 20 de septiembre (incluidos) / Verano / Invierno
Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) / Otoño / Primavera 
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano. """

#Mostrar opciones al usuario
print("Seleccione el hemisferio donde se encuentra")
print("1) Hemisferio Norte.")
print("2) Hemisferio Sur.")

#Ingreso de datos
hemisferio = int(input("Ingrese el hemisferio seleccionado: (1 o 2)"))
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el día: "))

#Calcular la estación del año.
if (hemisferio == 1) and ((mes == 12 and dia >= 21) or ( mes == 1 ) or (mes == 2) or (mes == 3 and dia <= 20)):
    print("Usted se encuentra en invierno")
elif (hemisferio == 1) and ((mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20)):
    print("Usted se encuentra en primavera")
elif (hemisferio == 1) and ((mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20)):
    print("Usted se encuentra en verano")
elif (hemisferio == 1) and ((mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20)):
    print("Usted se encuentra en otoño") 

elif (hemisferio == 2) and ((mes == 12 and dia >= 21) or ( mes == 1 ) or (mes == 2) or (mes == 3 and dia <= 20)):
    print("Usted se encuentra en verano")
elif (hemisferio == 2) and ((mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20)):
    print("Usted se encuentra en otoño")
elif (hemisferio == 2) and ((mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20)):
    print("Usted se encuentra en invierno")
elif (hemisferio == 2) and ((mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20)):
    print("Usted se encuentra en primavera")  
else:
    print("Se ingresó un hemisferio o fecha incorrecta")