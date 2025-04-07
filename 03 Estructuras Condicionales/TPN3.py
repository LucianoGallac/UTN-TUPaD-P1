#Ejercicio N1
EdadMinima = 18
edad = int(input("Ingrese su edad "))
if edad >= EdadMinima:
    print ("Eres mayor de edad")
else:
    print ("Eres menor de edad")


#Ejercicio N2
NotaMinima = 6
nota = int(input("Ingrese su calificacion"))
if nota >= NotaMinima:
    print ("Aprobado")
else:
    print ("Desaprobado")


#Ejercicio N3
numero = int(input("Ingrese un numero"))
if numero %2 == 0:
    print ("Numero par")
else:
    print("Por favor ingrese un numero par")


#Ejercicio N4
edad = int(input("Ingrese su edad"))

if edad > 0 and edad < 12:
    print ("Niño/a")
elif edad >= 12 and edad < 18:
    print ("Adolescente")
elif edad >= 18 and edad < 30:
    print ("Adulto/a joven")
else:
    print ("Adulto")


#Ejercicio N5
contraseña = input("Ingrese una contraseña")
if 8 <= len(contraseña)<=14:
    print ("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña valida")


#Ejercicio N6
from statistics import mode, median, mean 
import random

numeros_aleatorios =  [random.randint(1, 100) for i in range(50)] 

Lamoda = mode(numeros_aleatorios)
Lamediana = median(numeros_aleatorios)
LaMedia = mean(numeros_aleatorios)

print (f"La moda {Lamoda}, La mediana {Lamediana}, La media {LaMedia}")

if LaMedia > Lamediana and Lamediana > Lamoda:
    print ("Sesgo positivo")
elif LaMedia < Lamediana and Lamediana < Lamoda:
    print("Sesgo negativo")
else:
    print ("sin sesgo")


#Ejercicio N7
palabra = input("Ingrese una palabra")

if palabra[len(palabra) - 1] in "aeiouAEIOU":
        print (palabra + "!")
else:print (palabra)


#Ejercicio N8
Nombre = input("Ingrese su nombre: ")
Numero = input("Ingrese un numero del 1 al 3: ")

if Numero == "1":
    print (Nombre.upper())
elif Numero == "2":
    print (Nombre.lower())
elif Numero == "3":
    print (Nombre.title())
else:
    print ("No ha ingresado el numero correcto")


#Ejercicio N9
Magnitud = float(input("Ingrese la magnitud del terremoto"))

if Magnitud < 3:
    print ("muy leve")
elif Magnitud >= 3 and Magnitud < 4:
    print ("leve")
elif Magnitud >= 4 and Magnitud < 5:
    print ("Moderado")
elif Magnitud >=5 and Magnitud < 6:
    print ("fuerte")
elif Magnitud >= 6 and Magnitud < 7:
    print ("Muy fuerte")
else:
    print ("extremo")


#Ejercicio N10