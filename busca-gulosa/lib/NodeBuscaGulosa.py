class NodeBuscaGulosa:
    def __init__(self, ID):
        self.ID = ID
        self.father = None
        self.custoHeuristico = None
        self.custoDeChegada = None
        self.custoTotal = None
    
    def __str__(self):
        return "{ ID: %s fatherID: %s custoHeuristico: %s custoDeChegada: %s custoTotal: %s }" % \
                    (self.ID, self.father.ID, self.custoHeuristico, self.custoDeChegada, self.custoTotal) 