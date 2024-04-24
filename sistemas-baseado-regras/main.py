from regra import Regra
from regras import *
from base_conhecimento import BaseConhecimento
from maquina_inferencia import MaquinaInferencia

restaurante = Regra("regra_restaurante", regra_restaurante)
fastfood = Regra("regra_fastfood", regra_fastfood)
brasileiro = Regra("regra_brasileiro", regra_brasileira)
japones = Regra("regra_japones", regra_japonesa)
italiano = Regra("regra_italiano", regra_italiana)
hamburgueria = Regra("regra_hamburgueria", regra_hamburgueria)
pizzaria = Regra("regra_pizzaria", regra_pizzaria)
bodega_do_arthur = Regra("regra_bodega", regra_bodega)
coco_bambu = Regra("regra_coco", regra_coco)
spettus = Regra("regra_spettus", regra_spettus)
mazushi = Regra("regra_mazushi", regra_mazushi)
yugo = Regra("regra_yugo", regra_yugo)
hashimoto = Regra("regra_hashimoto", regra_hashimoto)
furetti = Regra("regra_furetti", regra_furetti)
la_trattoria = Regra("regra_trattoria", regra_trattoria)
famiglia_lucco = Regra("regra_famiglialucco", regra_famiglialucco)
burger_king = Regra("regra_burger", regra_burger)
mcdonalds = Regra("regra_mcdonalds", regra_mcdonalds)
bobs = Regra("regra_bobs", regra_bobs)
pizza_hut = Regra("regra_pizzahut", regra_pizzahut)
dominos = Regra("regra_dominos", regra_dominos)
habibs = Regra("regra_habibs", regra_habibs)


base_conhecimento = BaseConhecimento()
base_conhecimento.adicionar_regra(restaurante)
base_conhecimento.adicionar_regra(fastfood)
base_conhecimento.adicionar_regra(brasileiro)
base_conhecimento.adicionar_regra(japones)
base_conhecimento.adicionar_regra(italiano)
base_conhecimento.adicionar_regra(hamburgueria)
base_conhecimento.adicionar_regra(pizzaria)
base_conhecimento.adicionar_regra(bodega_do_arthur)
base_conhecimento.adicionar_regra(coco_bambu)
base_conhecimento.adicionar_regra(spettus)
base_conhecimento.adicionar_regra(mazushi)
base_conhecimento.adicionar_regra(yugo)
base_conhecimento.adicionar_regra(hashimoto)
base_conhecimento.adicionar_regra(furetti)
base_conhecimento.adicionar_regra(la_trattoria)
base_conhecimento.adicionar_regra(famiglia_lucco)
base_conhecimento.adicionar_regra(burger_king)
base_conhecimento.adicionar_regra(mcdonalds)
base_conhecimento.adicionar_regra(bobs)
base_conhecimento.adicionar_regra(pizza_hut)
base_conhecimento.adicionar_regra(dominos)
base_conhecimento.adicionar_regra(habibs)

# fato = {"tempo": "longo", "tipo_de_comida": "carne", "preco": "medio"}
# fato = {"tipo_de_comida": "sushi", "tempo": "curto", "preco": "alto"}
fato = {"tipo_de_comida": "sushi", "tempo": "curto",
        "tempo": "longo", "preco": "alto"}

maquina_inferencia = MaquinaInferencia(base_conhecimento, max_iter=5)
maquina_inferencia.executa(fato)
