from regra import Regra


class BaseConhecimento:
    def __init__(self):
        self.regras = []

    def adicionar_regra(self, regra: Regra):
        self.regras.append(regra)
