
import math
import copy
from lib.tabuleiro import *

def minimax(tabuleiro, player) -> int:

    estado = testeTerminal(tabuleiro)

    if estado == 'E':
        return 0
    
    if estado == 'P':
        return 1
    
    if estado == 'V':
        return -1
    
    if estado == None:
        utilidade = -1000
        
        for jogada in movimentosPossiveis(tabuleiro):
            tabuleiroProjetado = copy.deepcopy(tabuleiro)
            tabuleiroProjetado[jogada[0]][jogada[1]] = player
            resultadoMinMax = minimax(tabuleiroProjetado, 'V' if player == 'V' else 'P')

            if(player == 'V'):
                if(resultadoMinMax < utilidade):
                    utilidade = resultadoMinMax

            if(player == 'P'):
                if(resultadoMinMax > utilidade):
                    utilidade = resultadoMinMax
        
        return utilidade


