import typing
import copy
from base_conhecimento import BaseConhecimento


class MaquinaInferencia:
    def __init__(self, base_conhecimento: BaseConhecimento, max_iter: int):
        self.base_conhecimento = base_conhecimento
        self.max_iter = max_iter

    def executa(self, fato: typing.Dict):
        self.conjunto_conflito = []
        self.regras_anteriores = []
        self.contador_iteracao = 0

        # 2. Adiciona os dados iniciais à memória de trabalho
        self.memoria_trabalho = copy.deepcopy(fato)

        print(f"> Memoria de trabalho inicial = {self.memoria_trabalho}")

        while (True):
            print(f"## Iteração {self.contador_iteracao}")

            # 3. Compara o antecedente das regras com os fatos na MT
            for regra in self.base_conhecimento.regras:
                memoria_temporaria = copy.deepcopy(self.memoria_trabalho)
                disparada = regra.funcao(memoria_temporaria)
                if disparada:
                    # Apenas adiciona a regra no conjunto de conflito se
                    self.conjunto_conflito.append(regra)

            # 4. Usa o procedimento de resolução de conflito para selecionar
            # uma única regra do conjunto de conflito
            # Nao considera regras do conjunto de conflito que foram utilizadas anteriormente
            indices_a_serem_removidos = []
            for indice, regra_conflito in enumerate(self.conjunto_conflito):
                for regra_anterior in self.regras_anteriores:
                    if regra_conflito == regra_anterior:
                        indices_a_serem_removidos.append(indice)

            # Reordena para evitar que indices iniciais sejam removidos primeiro
            indices_a_serem_removidos.sort(reverse=True)
            for indice in indices_a_serem_removidos:
                del self.conjunto_conflito[indice]

            print(f"> Conjunto de conflito = {self.conjunto_conflito}")

            # Checa se o conjunto de conflito está vazio
            # Se estiver vazio, finaliza a execução do algoritmo
            if not self.conjunto_conflito:
                print("Conjunto de conflito está vazio, finalizando o algoritmo...")
                break

            # Seleciona a primeira regra que restou do conjunto
            melhor_regra = self.conjunto_conflito[0]
            print(f"Regra escolhida = {melhor_regra}")

            # Atualiza as regras anteriores com a regra utilizada para evitar loop
            self.regras_anteriores.append(melhor_regra)

            # 5. Dispara a regra selecionada e verifica o seu consequente
            _ = melhor_regra.funcao(self.memoria_trabalho)
            print(f"> Memoria de trabalho atualizada = {
                  self.memoria_trabalho}")

            # Reinicia o conjunto de conflito para a proxima iteração
            self.conjunto_conflito.clear()

            self.contador_iteracao = self.contador_iteracao + 1

            if self.contador_iteracao > self.max_iter:
                print(f"> Finalizando o algoritmo por ter ultrapassado o número máximo de {
                      self.max_iter} iterações...")
                break
