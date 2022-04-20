def gerarSubMatriz(matriz, i1, i2, j1, j2) -> list:
    submatriz = []
    for i in range(i2 - i1):
        submatriz.append([])
        for j in range(j2 - j1):
            submatriz[i].append(matriz[i + i1][j + j1])
    return submatriz

def verificaLinha(subMatriz) -> int:
    for i in subMatriz:
        if i[0] == '-':
            continue
        if i[0] == i[1] and i[0] == i[2]:
            return i[0]
    
    return 0

def verificaColuna(subMatriz) -> int:
    for j in range(3):
        if subMatriz[0][j] == '-':
            continue
        if subMatriz[0][j] == subMatriz[1][j] and subMatriz[0][j] == subMatriz[2][j]:
            return subMatriz[0][j]
    
    return 0

def verificaDiagonal(subMatriz) -> int:
    if subMatriz[0][0] == '-' and subMatriz[0][2] == '-':
        return 0
    if subMatriz[0][0] == subMatriz[1][1] and subMatriz[0][0] == subMatriz[2][2]:
        return subMatriz[0][0]

    if subMatriz[0][2] == subMatriz[1][1] and subMatriz[0][2] == subMatriz[2][0]:
        return subMatriz[0][2]
    
    return 0