class NodeEstrela:
    def __init__(self, ID):
        self.ID = ID
        self.distanciaDestino = None
        self.distanciaPercorrida = None
        self.f = None
        self.father = None
    
    def __str__(self):
        return "{ ID: %s distanciaAteDestino: %s distanciaPercorrida: %s custoTotal: %s }" % \
                    (self.ID, self.distanciaDestino, self.distanciaPercorrida, self.f) 