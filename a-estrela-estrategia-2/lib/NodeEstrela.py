class NodeEstrela:
    def __init__(self, estadoAtual):
        self.estadoAtual = estadoAtual
        self.acao = None                #   Tupla (NoAtual, NoVizinho)
        self.caminhoPercorrido = None   #   Lista contendo todas as ações até o presente nó
        self.custoTotal = None          #   Resultado da função de Avaliação
    
    def __str__(self):
        return "{ EstadoAtual: %s, acao: %s, custoTotal: %s }" % \
                    (self.estadoAtual, self.acao, self.custoTotal) 
    
    def printCaminhoPercorrido(self):
        for i in self.caminhoPercorrido:
            print(i)