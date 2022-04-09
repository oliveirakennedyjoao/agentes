from lib.NodeBuscaGulosa import NodeBuscaGulosa
from lib.ParisMetroMap import ParisMetroMap

class BuscaGulosa:
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

        currentNode = NodeBuscaGulosa(originNodeID)
        currentNode.custoHeuristico = 0             #   custo heurístico é o valor retornado pela função h
        currentNode.custoDeChegada = 0              #   custo heurístico é o valor retornado pela função g
        currentNode.custoTotal = 0                  #   custo total é o valor retornado pela função h

        self.listaAberta.append(currentNode)

        while True:

            if currentNode.ID == destinyNodeID:
                return currentNode

            #    1 - Insere o nó inicial na lista aberta;

            if len(self.listaAberta) == 0:                    
                self.listaAberta.append(currentNode)

            #    2 - Insere os vizinhoz na lista aberta;

            for boundaryID in self.PMM.getBoundaries(currentNode.ID):                
                boundaryNode = NodeBuscaGulosa(boundaryID)
                boundaryNode.custoH = self.PMM.getDistanceFromTo(currentNode.ID, boundaryID) 
                boundaryNode.custoTotal = currentNode.custoTotal + boundaryNode.custoHeuristico
                boundaryNode.father = currentNode

                # if (not self.hasNode(boundaryID, self.listaAberta)) and (not self.hasNode(boundaryID, self.listaFechada)):
                if not self.hasNode(boundaryID, self.listaFechada):
                    self.listaAberta.append(boundaryNode)
            
            #   3 - Coloca o nó atual na lista fechada;

            self.listaFechada.append(currentNode)

            #   4 - Retira o nó atual da lista aberta;

            self.listaAberta.remove(currentNode)

            # 5 - Escolhe o nó de menor custo para ser o proximo nó expandido;

            currentNode = self.pickNextNode()
            # print(currentNode)
            
            if not currentNode:
                return "There's no path"

    def originNode(self, nodeId):
        return NodeBuscaGulosa(nodeId)

    def pickNextNode(self):
        
        cheaperChild = self.listaAberta[0]
        
        for node in self.listaAberta:
            if node.custoTotal < cheaperChild.custoTotal:
                cheaperChild = node
        
        return cheaperChild
            
    def hasNode(self, nodeID, list):
        for node in list:
            if node.ID == nodeID:
                return True
        return False