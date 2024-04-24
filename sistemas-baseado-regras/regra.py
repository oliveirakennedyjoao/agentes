import inspect
import typing


class Regra:
    def __init__(self, nome: str, regra: typing.Callable):
        self.nome = nome
        self.funcao = regra
        self.assinatura = inspect.signature(self.funcao)

    # Função para mostrar a regra no log
    def __repr__(self):
        func_name = self.funcao.__name__
        func_params = ", ".join(self.assinatura.parameters.keys())
        return f"{func_name}(fato)"

    # Função para permitir a comparação entre diferentes regras
    def __eq__(self, other):
        if not isinstance(other, Regra):
            return False
        return vars(self) == vars(other)
