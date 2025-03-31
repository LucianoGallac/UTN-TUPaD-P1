#Ejercicio N1

print ("Hola mundo")

#Ejercicio N2

Nombre = input("Ingrese su nombre")
print (f"Hola{Nombre}! ")

#Ejercicio N3

Nombre = input ("Ingrese su nombre")
Apellido = input ("Ingrese su apellido")
LugarDeResidencia = input ("Ingrese su lugar de residencia")
Edad = int(input("Ingrese su Edad"))
print (f"Soy {Nombre} {Apellido}, tengo {Edad} años y vivo en {LugarDeResidencia}")

#Ejercicio N4

Radio = input("Ingrese el radio de un cirulo")
Radio = float(Radio)
pi = 3.14159
area = pi * Radio * Radio
Perimetro = 2 * pi * Radio
print (f"El area del circulo es {area} y su perimetro es {Perimetro}")

#Ejercicio N5

segundos = input("Ingrese los segundos")
segundos = int (segundos)
horas = segundos // 3600
print ("El resultado es ",horas, "Hora/horas")

#Ejercicio N6

numero = input("Ingrese un numero")
numero = int(numero)

print (f"{numero}, {numero * 2}, {numero * 3}, {numero * 4}, {numero * 5}, {numero * 6}, {numero * 7}, {numero * 8}, {numero * 9}, {numero * 10}")

#Ejercicio N7

numero1 = input("Ingrese un numero entero")
numero1 =int(numero1)
numero2 = input("Ingrese el segundo numero entero")
numero2 =int(numero2)

if numero1 > 0 and numero2 > 0:
    
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2 

    print(f"La suma de los números es: {suma}")
    print(f"La resta de los números es: {resta}")
    print(f"La multiplicación de los números es: {multiplicacion}")
    print(f"La división de los números es: {division}")
else:
    print("Error: Los números deben ser mayor a 0.")

#Ejercicio N8

Altura = input("Ingrese su altura")
Altura = float(Altura)

Peso = input("Ingrese su peso")
Peso = int(Peso)

Imc = Peso / (Altura**2)

print ("Su Indice de masa corporal es de ", Imc)

#Ejercicio N9

GradosCelcius = input("Ingrese la T°")
GradosCelcius = int (GradosCelcius)

Fahrenheit = 9/5 * GradosCelcius + 32

print ("La temperatura ingresada equivalente a fahrenheit es: ", Fahrenheit)

#Ejercicio N10

Numero1 = int(input("Ingrese el primer numero"))
Numero2 = int(input("Ingrese el segundo numero"))
Numero3 = int(input("Ingrese el tercer numero"))

Promedio = (Numero1 + Numero2 + Numero3) / 3

print("El promedio de estos tres numeros es de: ", Promedio)