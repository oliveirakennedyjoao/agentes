from lib.NodeEstrela import NodeEstrela
from lib.ParisMetroMap import ParisMetroMap

class Aestrela:
    def __init__(self):
        self.fronteiras = []
        self.PMM = ParisMetroMap()

    def findPath(self, originNodeID, destinyNodeID):

        if not(self.PMM.checkIfNodeExist(originNodeID) and self.PMM.checkIfNodeExist(destinyNodeID)):
            return "uma ou mais estações (nós) é inválida!"

        primeiroNo = self.gerarPrimeiroNo(originNodeID, destinyNodeID)
        self.fronteiras.append(primeiroNo)

        passoAtual = 1

        while True:
            print('''\n###############################\n\tPasso %s:\n###############################\n''' % passoAtual)
            
            noAtual = self.obterProximoNoExpandir()
            
            print("Nó Atual: \n\n\t%s" % noAtual)

            if noAtual.estadoAtual == destinyNodeID:
                print("\nDestino alcançado ''\o/'' !\n")
                return noAtual


            print("\nVizinhos inseridos:\n")

            for vizinhoID in self.PMM.getBoundaries(noAtual.estadoAtual):
                vizinho = self.gerarNoFronteira(noAtual, vizinhoID, destinyNodeID)
                
                # Validação para evitar que um passo já realizado seja repetido

                if(noAtual.acao['acao'][0] != vizinhoID):
                    self.fronteiras.append(vizinho)
                    print("\t%s" % vizinho)                

            self.fronteiras.remove(noAtual)

            print("\nFronteiras:\n")
            
            for fronteira in self.fronteiras:
                print("\t%s" % fronteira)

            passoAtual += 1


    def obterProximoNoExpandir(self) -> NodeEstrela:
        noExpandir = self.fronteiras[0]

        for noFronteira in self.fronteiras:
            if noFronteira.custoTotal < noExpandir.custoTotal:
                noExpandir = noFronteira
        
        return noExpandir

    def gerarPrimeiroNo(self, estadoAtual, estadoDestino) -> NodeEstrela:
        primeiroNo = NodeEstrela(estadoAtual)
        primeiroNo.acao = { 'acao': ('origem', estadoAtual), 'custo': 0 }
        primeiroNo.caminhoPercorrido = [primeiroNo.acao]
        primeiroNo.custoTotal = self.avaliarCusto(primeiroNo, estadoDestino)
        
        return primeiroNo
    
    def gerarNoFronteira(self, noOrigem, fronteiraID, estadoDestino):
        
        noFronteira = NodeEstrela(fronteiraID)
        noFronteira.acao = { 'acao': (noOrigem.estadoAtual, fronteiraID), 'custo': self.PMM.getRealDistanceFromTo(noOrigem.estadoAtual, fronteiraID) }
        
        noFronteira.caminhoPercorrido = noOrigem.caminhoPercorrido.copy()
        noFronteira.caminhoPercorrido.append(noFronteira.acao)

        noFronteira.custoTotal = self.avaliarCusto(noFronteira, estadoDestino)

        return noFronteira

    def avaliarCusto(self, no, estadoDestino):
        
        custoAteDestino = self.PMM.getDirectDistanceFromTo(no.estadoAtual, estadoDestino)
        custoRealAteOrigem = 0
        
        for acao in no.caminhoPercorrido:
            custoRealAteOrigem += acao['custo']
        
        return custoRealAteOrigem + custoAteDestino
