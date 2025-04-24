#Ejercicio N1

for cont in range (0,101):
    print (cont)

#Ejercicio N2

Numero_entero = input("Ingrese un numero entero")

cantidad_digitos = len(Numero_entero) 
print(f"El número tiene {cantidad_digitos} dígito/s.")

#Ejercicio N3

Primer_numero = int(input("Ingrese un numero entero "))
Segundo_numero = int(input("Ingrese el segundo numero entero "))
Suma = 0

print (f"La sumatoria de {Primer_numero} y {Segundo_numero} es: ")
for i in range (Primer_numero +1, Segundo_numero):
    Suma = Suma + i
print (Suma)

#Ejercicio N4

suma = 0

while True:

    Numero_entero = int(input("Ingrese un numero entero: "))
    

    if Numero_entero == 0:
        break
    

    suma += Numero_entero
print(f"La suma total de los números ingresados es: {suma}")

#Ejercicio N6

for cont in range (100,-2,-2):
    print (cont)

#Ejercicio N7

numero = int(input("Ingresa un número entero positivo: "))


if numero > 0:
    suma = 0
    for i in range(numero + 1):  
        suma = suma + i 
    print(f"La suma de los números entre 0 y {numero} es: {suma}")
else:
    print("Por favor, ingresa un número entero positivo.")

#Ejercicio N8

def contar_numeros():
    
    pares = 0
    impares = 0
    negativos = 0
    positivos = 0

    
    cantidad_numeros = 50 

    for i in range(cantidad_numeros):
        
        numero = int(input(f"Ingrese el número {i+1} de {cantidad_numeros}: "))


        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

        if numero < 0:
            negativos += 1
        elif numero > 0:
            positivos += 1

    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Números negativos: {negativos}")
    print(f"Números positivos: {positivos}")


contar_numeros()

#Ejercicio N9

suma = 0

cantidad_numeros = 50

for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el número {i+1}: "))  
    suma += numero  

LaMedia = suma / cantidad_numeros
print (f"La media es: {LaMedia}")

#Ejercicio N10

numero = input("Ingrese un número: ")

numero_invertido = numero[::-1]
print(numero_invertido)