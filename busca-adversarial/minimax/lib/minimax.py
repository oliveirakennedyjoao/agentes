
import math
from lib.tabuleiro import *

def hold():
    math.inf

def utilidade(tabuleiro: list):
    estado = testeTerminal(tabuleiro)
    
    if estado == None:
        return 0
    
    if estado == 'P':
        return 1
    
    if estado == 'V':
        return -1
    

def minimax(tabuleiro, player) -> int:

    for jogada in movimentosPossiveis():
        tabuleiroResultadoJogada = tabuleiro.copy()
        tabuleiroResultadoJogada[jogada[0]][jogada[1]] = player

        estado = testeTerminal(tabuleiro)
    
        if estado == None:
            minimax(tabuleiroResultadoJogada, 'V' if player == 'P' else 'V')
        
        if estado == 'E':
            return 0
        
        if estado == 'P':
            return 1
        
        if estado == 'V':
            return -1

def realizarMovimento(tabuleiro):
    melhorJogada = None
    valor = math.inf

    for jogada in movimentosPossiveis():
        tabuleiroResultadoJogada = tabuleiro.copy()
        tabuleiroResultadoJogada[jogada[0]][jogada[1]] = 'P'

        resultadoMinMax = minimax(tabuleiro, 'P')

        if(valor < resultadoMinMax):
            melhorJogada = tabuleiroResultadoJogada.copy()
            valor = resultadoMinMax

    return melhorJogada
        


