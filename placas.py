#Programa que genera una placa de carro con el patrón 4letras(mayúsculas) guion 3números

from random import randint, choice

letras = [chr(x) for x in range(65, 91)]
numeros = [numero for numero in range(10)]

def saca_placa(letras:str, numeros:int)-> str:
    """Función que devuelve un string con una placa de auto. Patrón 4letras-3números
    Toma dos listas como argumentos: Una string con todas las letras, una integer con digitos 0-9"""

    placa = ""
    for i in range(8):
        if i < 4:
            placa += choice(letras)
        elif i==4:
            placa += "-"
        else:
            placa += str(choice(numeros))

    return placa

placa = saca_placa(letras, numeros)
print(f"La placa es {placa}")
