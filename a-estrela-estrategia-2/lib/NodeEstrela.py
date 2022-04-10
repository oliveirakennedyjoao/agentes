class NodeEstrela:
    def __init__(self, estadoAtual):
        self.estadoAtual = estadoAtual
        self.acao = None                #   Tupla (NoAtual, NoVizinho)
        self.caminhoPercorrido = None   #   Lista Contendo todas as ações até o presente nó, ou seja, caminho da origem até o nó atual
        self.custoTotal = None          #   Resultado da função de Avaliação
    
    def __str__(self):
        return "{ EstadoAtual: %s, acao: %s, custoTotal: %s }" % \
                    (self.estadoAtual, self.acao, self.custoTotal) 
    
    def printCaminhoPercorrido(self):
        custoRealTotal = 0
        for i in self.caminhoPercorrido:
            custoRealTotal += i['custo']
            print(i)

        print("-------------------------------")
        print("Custo total do caminho: ", custoRealTotal, "\n")