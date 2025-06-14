"""1)Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario"""

#Función que calcula el factorial
def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num-1) * num

print("\n---Calcula el factorial desde 1 hasta el número que ingresas---\n")  
#Programa principal
#Se solicita al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

#Se llama a la función factorial con el número ingresado como parámetro
print (factorial(numero))



"""2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique."""

#Se crea la función fibonacci
def fibonacci_rec(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_rec(pos-1) + fibonacci_rec(pos-2)
    
#Programa principal    
#Se solicita al usuario hsta que posición quiere llegar
n = int(input("\nIngresa la posición de la serie Fibonacci hasta la cual quieres ver: "))

#Se muestra por pantalla la serie fibonacci
print(f"\nSerie de Fibonacci hasta la posición: {n}.")
for i in range(n + 1): 
    print(f"\nLa posición {i} = {fibonacci_rec(i)} en fibonacci")  


"""3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1)
. Prueba esta función en un
algoritmo general."""

#Definir función recursiva
def potencia(n, m):
    if m == 0:
        return 1
    else: 
        return n * potencia(n, m-1)

#Programa principal  
print("\n---Calcula la potencia de un número:---\n")  
#Se solicitan la base y potencia al usuario
n = int(input("Ingresa la base: "))
m = int(input("ingrese la potencia: "))
#Se realiza el calculo de potencia
res_potencia = potencia (n, m)
#Se muestra el resultado por pantalla
print (f"\nLa potencia de {n} elevado a {m} es: {res_potencia}")



"""4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

Ejemplo: 
Convertir el número 10 a binario: 
10 ÷ 2 = 5     resto: 0   
 5 ÷ 2 = 2     resto: 1   
 2 ÷ 2 = 1     resto: 0   
 1 ÷ 2 = 0     resto: 1   
Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010". """

#Se define la función recursiva
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

#Programa principal   
print("\n---Pasar un número decimal a binario---")
#Se solicitan los datos al usuario y se imprime por pantalla el resultado
numero = int(input("\nIngresa un número entero positivo: "))
if numero == 0:
    print("\nEl número binario es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"\nEl número binario es: {binario}")

"""5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
lo es. 
     Requisitos: 
La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed(). """

#Función recursiva
def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    # Comparar la primera y la última letra
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con la palabra sin la primera y la última letra
    return es_palindromo(palabra[1:-1])

#Programa principal
print("\n---Veamos si una palabra es palindromo---")
#Se solicitan ingreso de datos y se imprime por pantalla
palabra_ingresada = input("\nIngresa una cadena de texto sin expacios ni tilde: ").lower()
if es_palindromo(palabra_ingresada):
    print("\nEs palindromo")
else:
    print("\nNo es palindromo")



"""6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos. 
     Restricciones: 
No se puede convertir el número a string. 
Usá operaciones matemáticas (%, //) y recursión. 
Ejemplos: 
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
suma_digitos(9)      → 9 
suma_digitos(305)    → 8   (3 + 0 + 5) """

#Se define la función recursiva
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n //10)
    
#Programa principal
print("\n---Suma de dígitos---")
#Se solicitan datos al usuario y se muestra resultado por pantalla
numero = int(input("\nPor favor ingrese un número positivo para sumar sus dígitos : "))
if numero >= 0:
    print(f"\nLa suma de los dígitos es {suma_digitos(numero)}")
else:
    print("\nIngrese un número positivo")



"""7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
último nivel con un solo bloque. 
 
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
pirámide. 
 
      Ejemplos: 
contar_bloques(1)   → 1         (1) 
contar_bloques(2)   → 3         (2 + 1) 
contar_bloques(4)   → 10        (4 + 3 + 2 + 1) """

#Definir función recursiva
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return contar_bloques(n -1) + n
    
#Programa principal
print("\n---Contar bloques de una pirámide---")
#Se solicitan datos al cliente y se muestra resultados por pantalla
nivel = (int(input("Ingrese la cantidad de niveles o pisos de la pirámide: ")))
print (f"La pirámide con {nivel} niveles tiene {contar_bloques(nivel)} bloques")
    

"""8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número. 
Ejemplos: 
contar_digito(12233421, 2)   → 3  
contar_digito(5555, 5)       → 4   
contar_digito(123456, 7)     → 0  """

#Función recursiva
def contar_digito(numero, digito):
        if numero == 0:
            return 0
        else:
           ultimo_num = numero % 10
           if ultimo_num == digito:
            return 1 + contar_digito (numero // 10, digito) 
           else:
            return contar_digito (numero // 10, digito)

#Programa principal
print("\n---Contar cuantas veces se repite un dígito dentro de un número---")
#Ingreso de datos y se muestra resultado por pantalla
numero = int(input("\nIngrese un número positivo: "))
digito = int(input("Ingrese el dígito para ver cuantas veces aparece en el número ingresado: "))
print(f"\nEl número ingresado tiene {contar_digito(numero, digito)} veces el número {digito}") 
