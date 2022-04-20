def imprimirTabuleiro(tabuleiro):
    print('[')
    
    for linha in tabuleiro:
        print('\t', linha)
    
    print(']')

def movimentosPossiveis(tabuleiro: list, player):
    movimentosPossiveis = []

    avaliarProximaLinha = False

    index = 3

    while index >= 0:
        for posicao in range(4):
            if index == 3:
                if tabuleiro[index][posicao] == 0:
                    movimentosPossiveis.append({ 'posicao': (index, posicao) })
            if index < 3:
                if tabuleiro[index + 1][posicao] != 0:
                    movimentosPossiveis.append({ 'posicao': (index, posicao) })
        index -= 1

    return movimentosPossiveis
