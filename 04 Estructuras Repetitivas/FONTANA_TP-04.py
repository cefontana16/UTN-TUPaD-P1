"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""


#Mostrar por pantalla N° de ejercicio 
print("Ejercicio 1")

#Se declara la variable como entero
numero = int()

#Se importa el módulo time para mostrar mas lento el proceso en la terminal.
import time

#Proceso (Para la variable numero de 0 a 101)
for numero in range (101):
    print(numero)#Se muestra resultado por pantalla
    time.sleep(0.5)

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene."""


#Mostrar por pantalla N° de ejercicio 
print("/////////////")
print("Ejercicio 2")

#Ingreso de datos
num = int(input("Ingrese un número entero mayor a 0 y sabremos cuántos dígitos tiene: "))
cont = 0

#Inicio del ciclo mientras el número sea mayor a 0
while num > 0:
    #se actualiza la variable con el resultado entero de dividir al número por 10
    num = (num//10)
    #se suma un dígito al contador
    cont += 1

#Se muestra por pantalla la cantidad de dígitos
print("El número ingresado tiene" ,cont , "dígitos")

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores. """

#Se muestra el N° del ejercicio por pantalla
print("/////////////")
print("Ejercicio 3")

#Solicitamos datos de los números menor y mayor
numero_menor = int(input("Por favor, ingrese en número menor: "))
numero_mayor = int (input("Por favor ingrese el número mayor: "))
suma = 0

#Ciclo for 
for x in range (numero_menor+1, numero_mayor):
    suma = suma + x

#Mostrar respuesta por pantalla    
print("La suma de los números comprendidos entre ",numero_menor, "y ",numero_mayor, "excluyendo esos 2 valores es: ", suma)#Respuesta al usuario"""

    

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0."""


#Mostrar por pantalla N° de ejercicio 
print("/////////////")
print("Ejercicio 4")

#Solicitar ingreso de datos
num_entero = int(input("Ingrese un número entero: "))
suma= 0

#Inicio de ciclo while mientras num_entero sea distinto de 0
while num_entero != 0:
    #Se actualiza la variable sumandole el número entero ingresado
    suma = suma + num_entero
    #Se solicita ingresar otro número en cada iteración y se comunica que el 0 corta el ciclo y devuelve la suma
    num_entero= int(input("Ingrese otro número entero para sumar (muestra el total de la suma al ingresar 0): "))

#Resultado de la suma por pantalla
print("El total acumulado en la suma es: ", suma)

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.""" 


#Mostrar por pantalla N° de ejercicio 
print("/////////////")
print("Ejercicio 5")

#Se importa módulo random
import random

# Se declara la variable donde la función va a elegir aleatoreamente un número.
num_aleatorio = random.randint(0,9)

#Se muestra por pantalla de que trata el juego y se solicita un número
print("Bienvendido al juego: adivine el número escondido del 0 al 9")
num_ingresado = int(input("A probar suerte!!! Ingrese un número del 0 al 9: "))
#Se cuenta el primer ingreso del número solicitado anteriormente
cont = 1

#Proceso con While mientras sea no se adivine el número continúa el ciclo
while num_ingresado  != num_aleatorio:
        #Suma 1 a la variable contador cada vez que se ingresa un número 
        cont = cont + 1
        #Mientras no se adivine el número se pide un número nuevo
        num_ingresado = int(input("A ver esta vez!!! Ingresa otro número: "))

#Resultado por pantalla
print("Felicitaciones!! Acertaste el número en ", cont, "intentos.")
    


"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente."""

#Mostrar por pantalla N° de ejercicio 
print("/////////////")
print("Ejercicio 6")

#Se llama al modulo time
import time
n_par = int()

#Proceso del ciclo muestra numero par desde 100 al 0
for n_par in range (100, -1, -2):
    #Se muestra el resultado por pantalla
    print (n_par)
    #Muestra 1 número par por segundo 
    time.sleep (1)

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario."""

#Muestra por pantalla en N° del ejercicio
print("/////////////")
print("Ejercicio 7")

#Se pide al usuario ingresar número y se declara como entero
num_positivo = int(input("Ingrese un número positivo: "))
#Se declara la variable suma en 0
suma = 0

#Se usa el ciclo for para sumar desde 0 hasta el número ingresado por el usuario
for x in range (0, num_positivo+1):
    #Se suma el valor de x a la variable suma.
    suma = suma + x

#Se muestra el resultado de la suma por pantalla.
print("La suma de los números comprendidos entre 0 y ", num_positivo, "es: ", suma)

"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

#Se muestra el N° del ejercicio por pantalla
print("/////////////")
print("Ejercicio 8")

#Se declaran las variables en 0
cont = 0
num_par = 0
num_impar = 0
num_positivo = 0
num_negativo = 0

#Se comunica cuantos números se van a solicitar por pantalla
print("Debe ingresar 100 números enteros (negativos o positivos). ")
print("Luego se mostrará cuántos de ellos son par, impar, negativos o positivos. Comencemos!")

# ciclo for para contar de 0 a 100
for cont in range (0, 100):
    #Se solicita un número entero y se declara como entero
    num_entero = int(input("Por favor, ingrese un número entero: "))
    cont = cont +1
    #Si el resto del número ingresado es 0 se suma 1 en la variable num_par
    if num_entero % 2 == 0:
        num_par += 1
    #Sino si el resto del número ingresado es distinto de 0 se suma 1 en la variable num_impar
    elif num_entero % 2 != 0:
        num_impar += 1
    #Si el número ingresado es mayor a 0 se suma 1 en la variable num_positivo
    if num_entero > 0:
        num_positivo += 1
     #Sino si el número ingresado es menor a  0  se suma 1 a la variable num_negativo   
    elif num_entero < 0:
        num_negativo += 1

#Se imprimen los resultados por pantalla
print("Números pares ingresados: ", num_par)
print("Números impares ingresados: ", num_impar)       
print("Números positivos ingresados: ", num_positivo)
print("Números negativos ingresados: ", num_negativo) 



"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor)."""

#Se muestra el n° de ejercicio por pantalla
print("/////////////")
print("Ejercicio 9")

#Se declaran las variables suma, cont y num_entero en 0
suma = 0
cont = 0
num_entero = 0

#Se comunica al usuario cuantos números deberá ingresar
print("Debe ingresar 100 números enteros para calcular el promedio de esos valores")

#Declaramos la variable cantidad de números donde podemos modificar el mismo
cant_num = 100

# ciclo for para la variable cont de 0 a 100
for cont in range (0,cant_num):
    #se solicita un número al usuario y se declara como entero
    num_entero = int(input("Ingrese número entero: "))
    #Se suma el número indicado a la variable suma en cada iteración
    suma = suma + num_entero

#Se calcula el promedio y se muestra por pantalla
print("El promedio de los números ingresados es:" , suma/cant_num)




"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. """

#Se muestra el N° de ejercicio por pantalla
print("//////////////")
print("Ejercicio N° 10")

#Se solicita un número al usuario y se declara como entero
numero = int(input("Ingrese un número de 2 o más dígitos: "))

#Se declaran las variables digito y num_invertido en 0
digito= 0
num_invertido = 0

#Se inicia el ciclo while con la condición mientras numero sea mayor a o
while numero > 0:
    #Se carga el resto del numero dividido 10 en la variable
    digito = numero % 10
    # Se actualiza la variable multiplicando la misma por 10 y sumando el digito
    num_invertido = num_invertido * 10 + digito
    #Se actualiza la variable a la parte entera del número divido 10 para seguir iterando
    numero = numero // 10


#Se muestra el resultado del número invertido por pantalla
print("El número invertido es: ", num_invertido)
    