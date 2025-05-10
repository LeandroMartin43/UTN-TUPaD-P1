import random
from statistics import mode, median, mean

# 1. Programa que solicita la edad del usuario
edad = int(input("Introduce tu edad: "))
if edad > 18:
    print("Es mayor de edad")

# 2. Programa que solicita la nota al usuario
nota = float(input("Introduce tu nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3. Programa que permite ingresar solo números pares
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4. Programa que clasifica la edad en categorías
edad = int(input("Introduce tu edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5. Programa que valida la longitud de la contraseña
contrasena = input("Introduce una contraseña (8-14 caracteres): ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6. Programa que calcula moda, mediana y media y determina el sesgo
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]  # Lista con 50 números aleatorios
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

# Determinar el sesgo
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo")

# 7. Programa que agrega un signo de exclamación si la palabra termina en vocal
frase = input("Introduce una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    print(f"{frase}!")
else:
    print(frase)

# 8. Programa que permite transformar el nombre en mayúsculas, minúsculas o con la primera letra mayúscula
nombre = input("Introduce tu nombre: ")
opcion = int(input("Elige una opción: 1. Mayúsculas, 2. Minúsculas, 3. Primera letra mayúscula: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")

# 9. Programa que clasifica la magnitud de un terremoto según la escala de Richter
magnitud = float(input("Introduce la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# 10. Programa que determina la estación del año según el hemisferio, mes y día
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("Introduce el número de mes (1-12): "))
dia = int(input("Introduce el día del mes: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        print("Verano")
    else:
        print("Otoño")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        print("Invierno")
    else:
        print("Primavera")
else:
    print("Hemisferio no válido")
