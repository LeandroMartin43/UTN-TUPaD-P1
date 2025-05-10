# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("Actividad 1: Números del 0 al 100 en orden creciente")
for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
print("\nActividad 2: Contar la cantidad de dígitos de un número")
numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(abs(numero)))  # Usamos abs para evitar contar el signo negativo
print(f"El número tiene {cantidad_digitos} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
print("\nActividad 3: Sumar los números entre dos valores")
inicio = int(input("Ingrese el primer valor: "))
fin = int(input("Ingrese el segundo valor: "))
suma = sum(range(inicio + 1, fin))  # Excluimos los valores de inicio y fin
print(f"La suma de los números entre {inicio} y {fin} (excluyéndolos) es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
print("\nActividad 4: Sumar números hasta ingresar 0")
total = 0
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    total += num
print(f"El total acumulado es: {total}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
print("\nActividad 5: Juego de adivinar el número")
numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
        break

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
print("\nActividad 6: Números pares entre 0 y 100 en orden decreciente")
for i in range(100, -1, -2):  # Empieza en 100 y baja de 2 en 2
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
print("\nActividad 7: Sumar números hasta un número indicado por el usuario")
limite = int(input("Ingrese un número entero positivo: "))
if limite >= 0:
    suma = sum(range(limite + 1))  # Suma de todos los números desde 0 hasta el límite
    print(f"La suma de los números desde 0 hasta {limite} es: {suma}")
else:
    print("Por favor, ingrese un número positivo.")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos.
print("\nActividad 8: Contar números pares, impares, negativos y positivos")
pares = impares = negativos = positivos = 0
for _ in range(100):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1
print(f"Pares: {pares}, Impares: {impares}, Negativos: {negativos}, Positivos: {positivos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
print("\nActividad 9: Calcular la media de 100 números enteros")
suma = 0
for _ in range(100):
    numero = int(input("Ingrese un número entero: "))
    suma += numero
media = suma / 100
print(f"La media de los números ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
print("\nActividad 10: Invertir el orden de los dígitos de un número")
numero = input("Ingrese un número: ")
numero_invertido = numero[::-1]
print(f"El número invertido es: {numero_invertido}")
