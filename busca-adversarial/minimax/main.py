import os
import copy
from lib.minimax import *
from lib.tabuleiro import *

tabuleiro = [
    ['-', '-', '-', '-'],
    ['-', '-', '-', '-'],
    ['-', '-', '-', '-'],
    ['-', 'V', '-', 'P']
]

def playerJoga(tabuleiro):

    colunaJogar = input("'V' joga: escolha uma coluna: ")
    jogadasPossiveis = movimentosPossiveis(tabuleiro)

    for jogada in jogadasPossiveis:
        if jogada[1] == int(colunaJogar):        
            tabuleiro[jogada[0]][jogada[1]] = 'V'
    
    os.system('cls')
    print('YOU:')
    imprimirTabuleiro(tabuleiro)

def iaJoga(tabuleiro):
    #os.system('cls')

    melhorJogada = None
    utilidade = -1000

    for jogada in movimentosPossiveis(tabuleiro):
        tabuleiroResultadoJogada = copy.deepcopy(tabuleiro)
        tabuleiroResultadoJogada[jogada[0]][jogada[1]] = 'P'

        resultadoMinMax = minimax(tabuleiroResultadoJogada, 'V')
        
        # print(resultadoMinMax)

        if(resultadoMinMax >= utilidade):
            utilidade = resultadoMinMax
            melhorJogada = jogada

    tabuleiro[melhorJogada[0]][melhorJogada[1]] = 'P'
    
    print('IA:')
    imprimirTabuleiro(tabuleiro)

def start():
    imprimirTabuleiro(tabuleiro)
    
    while not gameOver(tabuleiro):
    
        playerJoga(tabuleiro)

        if gameOver(tabuleiro):
            print ('Você venceu!')
        else:
            iaJoga(tabuleiro)

        estadoDoJogo = testeTerminal(tabuleiro)
        if estadoDoJogo != None:
            print(estadoDoJogo, 'Venceu!')
            break

start()