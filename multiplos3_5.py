number = 10

def solution(number):
    suma = 0
    if number < 0:
        return suma
    else:
        multiplos = [x for x in range(1, number) if x % 3 == 0 or x % 5 == 0]

    for num in multiplos:
        suma += num

    return suma

print(solution(number))

