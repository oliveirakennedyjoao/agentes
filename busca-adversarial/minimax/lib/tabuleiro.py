from lib.matriz import *

def imprimirTabuleiro(tabuleiro):
    print('[')
    
    for linha in tabuleiro:
        print('\t', linha)
    
    print(']')

def movimentosPossiveis(tabuleiro: list):
    movimentosPossiveis = []

    index = 3

    while index >= 0:
        for posicao in range(4):
            if index == 3:
                if tabuleiro[index][posicao] == '-':
                    movimentosPossiveis.append([index, posicao])
            if index < 3:
                if tabuleiro[index][posicao] == '-':
                    if tabuleiro[index + 1][posicao] != '-':
                        movimentosPossiveis.append([index, posicao])
        index -= 1

    return movimentosPossiveis

def testeTerminal(tabuleiro):
    for i in range(2):
        for j in range(2):
            matrizAvaliar = gerarSubMatriz(tabuleiro, i, i + 3, j, j + 3)

            linhas = verificaLinha(matrizAvaliar)
            if linhas != 0:
                return linhas
            
            colunas = verificaColuna(matrizAvaliar)
            if colunas != 0:
                return colunas
            
            diagonais = verificaDiagonal(matrizAvaliar)
            if diagonais != 0:
                return diagonais
    
    if gameOver(tabuleiro):
        return 'E'
    
    return None

def gameOver(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula == '-':
                return False
    return True