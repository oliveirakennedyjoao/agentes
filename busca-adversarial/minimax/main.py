import os
from lib.minimax import *
from lib.tabuleiro import *

tabuleiroInicial = [
    ['-', '-', '-', '-'],
    ['-', '-', '-', '-'],
    ['-', '-', '-', '-'],
    ['-', 'V', '-', 'P']
]

def playerJoga(tabuleiro):
    
    imprimirTabuleiro(tabuleiro)
    
    colunaJogar = input("'V' joga: escolha uma coluna: ")
    jogadasPossiveis = movimentosPossiveis(tabuleiro)
    
    novoTabuleiro = tabuleiro.copy()

    for jogada in jogadasPossiveis:
        if jogada[1] == int(colunaJogar):        
            novoTabuleiro[jogada[0]][jogada[1]] = 'V'
    
    os.system('cls')
    imprimirTabuleiro(novoTabuleiro)
    return novoTabuleiro

def iaJoga(tabuleiro):
    print('iaJogou')
    os.system('cls')
    imprimirTabuleiro(tabuleiro)
    return tabuleiro

tabuleiro = tabuleiroInicial

while not gameOver(tabuleiro):
    tabuleiro = playerJoga(tabuleiro)

    if gameOver(tabuleiro):
        print ('Você venceu!')
    else:
        tabuleiro = iaJoga(tabuleiro)