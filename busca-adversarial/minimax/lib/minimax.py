from lib.matriz import *
from lib.tabuleiro import *

def avaliacao(tabuleiro: list):

    matrizAvaliar = gerarSubMatriz(tabuleiro, 3, 3)

    res = verificaLinha(matrizAvaliar)
    res2 = verificaColuna(matrizAvaliar)
    res3 = verificaDiagonal(matrizAvaliar)
    
    resMovimentosPossiveis = movimentosPossiveis(tabuleiro, 1)
    print(resMovimentosPossiveis)
    
