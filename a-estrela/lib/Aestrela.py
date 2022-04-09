from lib.NodeEstrela import NodeEstrela
from lib.ParisMetroMap import ParisMetroMap

class Aestrela:
    def __init__(self):
        self.listaAberta = []
        self.listaFechada = []
        self.PMM = ParisMetroMap()

    def findPath(self, originNodeID, destinyNodeID):
        
        ## Check if Nodes Exist

        if not(self.PMM.checkIfNodeExist(originNodeID) and self.PMM.checkIfNodeExist(destinyNodeID)):
            return "One or more Nodes are not valid!"

        ## Check if 
        
        if originNodeID == destinyNodeID:
            return "Origem igual ao Destino"
        
        ## Cria um noEstrela a partir do ID do no de origem

        originNode = NodeEstrela(originNodeID)
        originNode.distanciaDestino = self.PMM.getDirectDistanceFromTo(originNodeID, destinyNodeID)       #   custo heurístico é o valor retornado pela função h
        originNode.distanciaPercorrida = 0                                                          #   custo heurístico é o valor retornado pela função g
        originNode.f = 0                                                                          #   custo total é o valor retornado pela função g + h

        self.listaAberta.append(originNode)

        while True:

            currentNode = self.pickNextNode()

            if not currentNode:
                return "There's no path"

            print(f"\nNó Atual:  %s" % currentNode)

            if currentNode.ID == destinyNodeID:
                print("\nResultado encontrado!")
                return currentNode

            #    1 - Insere o nó inicial na lista aberta;

            print("\nVizinhos inseridos:\n")

            for boundaryID in self.PMM.getBoundaries(currentNode.ID):                
                boundaryNode = NodeEstrela(boundaryID)
                boundaryNode.distanciaDestino = self.PMM.getDirectDistanceFromTo(boundaryID, destinyNodeID) 
                boundaryNode.distanciaPercorrida = currentNode.distanciaPercorrida + self.PMM.getRealDistanceFromTo(currentNode.ID, boundaryID)
                boundaryNode.f = boundaryNode.distanciaPercorrida + boundaryNode.distanciaDestino
                boundaryNode.father = currentNode

                if currentNode.father and boundaryNode.ID != currentNode.father.ID:
                    self.listaAberta.append(boundaryNode)
                    print(boundaryNode)
                elif currentNode.ID == originNode.ID:
                    self.listaAberta.append(boundaryNode)
                    print(boundaryNode)

            self.listaAberta.remove(currentNode)


    def pickNextNode(self):
        
        cheaperChild = NodeEstrela("0")
        cheaperChild = self.listaAberta[0]
        
        for node in self.listaAberta:
            if node.f < cheaperChild.f:
                cheaperChild = node
        
        return cheaperChild
            
    def hasNode(self, nodeID, list):
        for node in list:
            if node.ID == nodeID:
                return True
        return False