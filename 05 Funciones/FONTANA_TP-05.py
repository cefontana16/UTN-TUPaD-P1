#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range

print("Ejercicio 1")
lista_multiplos_de4 = list(range(4, 101, 4))
print(lista_multiplos_de4)

"""2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
indexing con números negativos! """

print("Ejercicio 2")
lista_indexing = ["rojo", "azul", "verde", "blanco", "gris"]
print(lista_indexing[-2])

"""3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
ejemplo: 
lista_vacia = [] """

print("Ejercicio 3")
lista_vacia = []
lista_vacia.append("Hola")
lista_vacia.append("buenos")
lista_vacia.append("dias")
print(lista_vacia)


"""4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
en los videos o bien investigar cómo funciona el indexing con números negativos! 
animales = ["perro", "gato", "conejo", "pez"] """

print("Ejercicio 4")
animales = ["perro", "gato", "conejo", "pez"]
animales[-1] = "oso"
animales[-3] = "loro"
print(animales)


#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 

print("Ejercicio 5")
numeros = [8, 15, 3, 22, 7]#lista numeros con 5 elementos
numeros.remove(max(numeros))#Remueve el numero máximo de la lista números, en este caso se removería el numero 22.
print(numeros)#se imprime la lista nueva numeros sin el numero mayor que fue removido anteriormente

"""6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
pantalla los dos primeros. """

print("Ejercicio 6")
lista = list(range(10, 31, 5))
print(lista[0:2])

"""7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
cualesquiera. """

print("Ejercicio 7")
autos = ["sedan", "polo", "suran", "gol"] 
autos[1] = "palio"
autos[2] = "corolla"
print(autos)

"""8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
directamente. Imprimir la lista resultante por pantalla. """

print("Ejercicio 8")
dobles = []
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)
print(dobles)


"""9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
diferentes clientes: 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
["agua"]] 
a) Agregar "jugo" a la lista del tercer cliente usando append. 
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
c) Eliminar "pan" de la lista del primer cliente.  
d) Imprimir la lista resultante por pantalla """

print("Ejercicio 9")
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
["agua"]] 

compras[2].append("jugo")
lista_2_fideos = compras[1]
lista_2_fideos[1]= "tallarines"
compras[0].remove("pan")
print(compras)


"""10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
● Posición lista_anidada[0]: 15 
● Posición lista_anidada[1]: True 
● Posición lista_anidada[2][0]: 25.5 
● Posición lista_anidada[2][1]: 57.9 
● Posición lista_anidada[2][2]: 30.6 
● Posición lista_anidada[3]: False 
Imprimir la lista resultante por pantalla."""

print("Ejercicio 10")
lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]
print(lista_anidada)

