"""1. Crear una función llamada imprimir_hola_mundo que imprima por
 pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
 programa principal."""

#Función 
def imprimir_hola_mundo():
    print ("Hola Mundo")

#Programa principal
print("\nImprimir Hola Mundo\n")
imprimir_hola_mundo()


"""2. Crear una función llamada saludar_usuario(nombre) que reciba
 como parámetro un nombre y devuelva un saludo personalizado.
 Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
volver: “Hola Marcos!”. Llamar a esta función desde el programa
 principal solicitando el nombre al usuario."""

#Se crea la funcion saludar_usuario(nombre)
def saludar_usuario(nombre):
    return f"¡Hola {nombre}!"

#programa principal
print("\nSaludar al usuario\n")
nombre = input("Por favor ingrese su nombre: ")
print (saludar_usuario(nombre))



"""3. Crear una función llamada informacion_personal(nombre, apellido,
 edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
dir los datos al usuario y llamar a esta función con los valores in
gresados."""

#Función
def información_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

#programa principal
print("\nPresentación con información personal\n")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad:")
residencia = input("Ingresa tu residencia: ")
print (información_personal(nombre, apellido, edad, residencia))



 
"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
dio como parámetro y devuelva el área del círculo. calcular_peri
metro_circulo(radio) que reciba el radio como parámetro y devuel
va el perímetro del círculo. Solicitar el radio al usuario y llamar am
bas funciones para mostrar los resultados."""


import math
#función area
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

#función perímetro
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#programa principal
print("\nCalcular área y perímetro del circulo\n")
radio = float(input("Ingrese el radio del círculo: "))
print ("El área del círculo es: ", round(calcular_area_circulo(radio), 2))
print ("El perímetro del círculo es: ", round(calcular_perimetro_circulo(radio),2))


"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
 una cantidad de segundos como parámetro y devuelva la cantidad
 de horas correspondientes. Solicitar al usuario los segundos y mos
trar el resultado usando esta función."""

#función
def segundos_a_horas(segundos):
    return segundos / 3600

#programa principal
print("\nPasar de horas a segundos\n")
segundos = int(input("Por favor ingrese la cantidad de segundos: "))
print ("Los", segundos ," segundos son: ", round(segundos_a_horas(segundos), 2),"horas")




"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
 número como parámetro y imprima la tabla de multiplicar de ese
 número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción."""

#función
def tabla_multiplicar(numero):
    print (f"Tabla de multiplicar de: {numero}")
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")

#programa principal
print("\nTabla de multiplicar del número ingresado\n")
numero = int(input("Ingresa un número del 1 a 10:"))
tabla_multiplicar(numero)



"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
 dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara."""

#funcion
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 
    return (suma, resta, multiplicacion, division)

#programa principal
print("\nOperaciones básicas\n")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
resultados = operaciones_basicas(a, b)
print("Suma, resta, multiplicación y división = ", resultados)




"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
 peso en kilogramos y la altura en metros, y devuelva el índice de
 masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales."""

#función 
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc 
#programa principal
print("\nIngresa tus datos para calcluar el índice de masa corporal\n")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print("Su imc es: ",round(calcular_imc(peso, altura), 2))



"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 una temperatura en grados Celsius y devuelva su equivalente en
 Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 resultado usando la función."""

#crear función
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit
#programa principal
print("\nPasar de grados celsius a fahrenheit\n")
celsius = float(input("Ingrese la temperatura en grados celsius: "))
print(celsius, "grados celsius son: ", round(celsius_a_fahrenheit(celsius), 2), "grados fahrenheit.")


"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
 tres números como parámetros y devuelva el promedio de ellos.
 Solicitar los números al usuario y mostrar el resultado usando esta
 función."""

#Crear función
def calcular_promedio(a, b, c):
    promedio = (a + b + c ) / 3
    return promedio

#programa principal
print("\nCalcula el promedio de los números ingresados\n")
a = float(input("Ingrese el primer número:" ))
b = float(input("Ingrese el segundo número:" ))
c = float(input("Ingrese el tercer número:" ))
print ("El promedio es: ", round(calcular_promedio(a, b, c), 2))
                  