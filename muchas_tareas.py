#Archivo con diversas funciones para practicar varios temas que se toman del libro de 
#Computer Science with Python - Zelle cápitulo 4

def numeros_notas():
    #notas convertidas de numeros a letras
    notas = ['F', 'F', 'D', 'C', 'B', 'A']
    while True:
        quiz_nota = input("Ingrese la nota del quiz (1-5): ")
        try:
            quiz_nota = int(quiz_nota)
        except:
            print("El valor de la nota es invalido!")
        else:
            if quiz_nota < 0 or quiz_nota > 5:
                print("Nota fuera del rango 1 - 5!")
            else:
                break
    print(f"La nota general es {notas[quiz_nota]}")

def acronimo():
    #Toma una frase y muestra las letras inciales de cada palabra en mayúsculas
    frase = input("Ingrese la frase a acronimizar: ")
    frase = frase.lower()

    for letra in range(len(frase)):
        if letra == 0:
            print(frase[letra].upper(), end="")
        if frase[letra] == " " and letra != len(frase) - 1:
            print(frase[letra + 1].upper(), end="")
    print()  

def nombres_numerologicos():
    #Pide un nombre y se devuelve un valor entero. Teniendo en cuenta a=1, b=2 .. z=26

    while True:
        valor_nombre = 0
        nombre = input("Ingrese su nombre para darle su valor: ")
        nombre = nombre.lower()
        try:
            suma = 0
            for letra in nombre:
                if (ord(letra) >= 97 and ord(letra) <= 122) or letra == " ":
                    suma += 1
        except:
            print("Error")
        else:
            if suma == len(nombre):
                break
            else:
                print("Se necesitan solo letras!")

    for letra in nombre:
        if letra != " ":
            valor_nombre += ord(letra) - 96

    print(f"El valor numerologico de tu nombre es {valor_nombre}")    
        
def cifra_cesar():
    #Codifica un texto moviendose determinadas pociones (llave) en el alfabeto. LLave 2 a = c

    frase = input("Ingrese la frase a codificar: ")

    while True:
        llave = input("Ingrese el valor de la llave(1-26): ")
        try:
            llave = int(llave)
        except ValueError:
            print("El dato debe ser un numero de 1 a 26!")
        else:
            if llave < 1 or llave > 26:
                print("El dato debe ser un numero de 1 a 26!")
            else:
                break

    for letra in frase:
        print(chr(ord(letra) + llave), end="")

    print()

def menu():
    print("*** TAREAS VARIAS ***")
    print()
    print("1. Convertir Notas - Numeros a Letras")
    print("2. Acronimo")
    print("3. Nombres Numerologicos")
    print("4. Cifra Cesar")
    print("5. Cuenta Palabras")
    print("6. Promedio Tamano Palabraas")
    print()

def eleccion():
    seleccion = input("Escriba el numero de su seleccion: ")
    if seleccion == '1':
        numeros_notas()
    elif seleccion == '2':
        acronimo()
    elif seleccion == '3':
        nombres_numerologicos()
    elif seleccion == '4':
        cifra_cesar()
    elif seleccion == '5':
        cuenta_palabras()
    elif seleccion == '6':
        promedio_largo_palabra()

def cuenta_palabras():
    #cuenta el numero de palabras de una oracion

    frase = input("Ingrese una oracion: ").split(" ")
    print(f"Su oracion tiene {len(frase)} palabras!")

def promedio_largo_palabra():
    #Devuleve el promedio del tamano de las palabras en una oracion

    frase = input("Escriba una frase: ").split(" ")
    suma = 0

    for palabra in frase:
        suma += len(palabra)

    print(f"El promedio del tamano por palabras de su frase es {suma / len(frase)}")

menu()
eleccion()

