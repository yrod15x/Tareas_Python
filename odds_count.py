def find_it(seq):
    
    contadores = []
    
    for i in range(len(seq)):
        cont = 0
        for j in range(len(seq)):
            if seq[i] == seq[j]:
                cont +=1
        contadores.append(cont)

    for num in range(len(contadores)):
        if contadores[num] % 2 != 0:
            return seq[num]
    
    return contadores

seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

print(find_it(seq), end=" ")