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
                    movimentosPossiveis.append({ 'posicao': (index, posicao) })
            if index < 3:
                if tabuleiro[index + 1][posicao] != '-':
                    movimentosPossiveis.append({ 'posicao': (index, posicao) })
        index -= 1

    return movimentosPossiveis

def testeTerminal(tabuleiro):
    for i in range(2):
        for j in range(2):
            matrizAvaliar = gerarSubMatriz(tabuleiro, i, i + 3, j, j + 3)
            print(matrizAvaliar)