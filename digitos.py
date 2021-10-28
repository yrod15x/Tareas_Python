
num = 4567
digitos = []

while num > 0:
    digitos.append(int(num % 10))
    num = int(num /10)

digitos.reverse()

print(digitos)
