def regra_restaurante(fato):
    try:
        if fato["tempo"] == "demorado":
            fato["Local"] = "restaurante"
            return True
    except:
        pass
    return False


def regra_fastfood(fato):
    try:
        if fato["tempo"] == "rapido":
            fato["Local"] = "fast_food"
            return True
    except:
        pass
    return False


def regra_brasileiro(fato):
    try:
        if fato["Local"] == "restaurante" and fato["estrangeiro"] == "nao":
            fato["nacionalidade"] = "brasileiro"
            return True
    except:
        pass
    return False


def regra_japones(fato):
    try:
        if fato["Local"] == "restaurante" and fato["estrangeiro"] == "sim" and fato["continente"] == "asia":
            fato["nacionalidade"] = "japones"
            return True
    except:
        pass
    return False


def regra_italiano(fato):
    try:
        if fato["Local"] == "restaurante" and fato["estrangeiro"] == "sim" and fato["continente"] == "europa":
            fato["nacionalidade"] = "italiano"
            return True
    except:
        pass
    return False


def regra_hamburgueria(fato):
    try:
        if fato["Local"] == "fast_food" and fato["compartilhar"] == "nao":
            fato["tipo"] = "hamburgueria"
            return True
    except:
        pass
    return False


def regra_pizzaria(fato):
    try:
        if fato["Local"] == "fast_food" and fato["compartilhar"] == "sim":
            fato["tipo"] = "pizzaria"
            return True
    except:
        pass
    return False


def regra_bodega(fato):
    try:
        if fato["nacionalidade"] == "brasileiro" and fato["preco"] == "baixo":
            fato["estabelecimento"] = "bodega_do_arthur"
            return True
    except:
        pass
    return False


def regra_coco(fato):
    try:
        if fato["nacionalidade"] == "brasileiro" and fato["preco"] == "medio":
            fato["estabelecimento"] = "coco_bambu"
            return True
    except:
        pass
    return False


def regra_spettus(fato):
    try:
        if fato["nacionalidade"] == "brasileiro" and fato["preco"] == "alto":
            fato["estabelecimento"] = "spettus"
            return True
    except:
        pass
    return False


def regra_mazushi(fato):
    try:
        if fato["nacionalidade"] == "japones" and fato["preco"] == "alto":
            fato["estabelecimento"] = "mazushi"
            return True
    except:
        pass
    return False


def regra_yugo(fato):
    try:
        if fato["nacionalidade"] == "japones" and fato["preco"] == "medio":
            fato["estabelecimento"] = "yugo"
            return True
    except:
        pass
    return False


def regra_hashimoto(fato):
    try:
        if fato["nacionalidade"] == "japones" and fato["preco"] == "baixo":
            fato["estabelecimento"] = "hashimoto"
            return True
    except:
        pass
    return False


def regra_furetti(fato):
    try:
        if fato["nacionalidade"] == "italiano" and fato["preco"] == "alto":
            fato["estabelecimento"] = "furetti"
            return True
    except:
        pass
    return False


def regra_trattoria(fato):
    try:
        if fato["nacionalidade"] == "italiano" and fato["preco"] == "medio":
            fato["estabelecimento"] = "la_trattoria"
            return True
    except:
        pass
    return False


def regra_famiglialucco(fato):
    try:
        if fato["nacionalidade"] == "italiano" and fato["preco"] == "baixo":
            fato["estabelecimento"] = "famiglia_lucco"
            return True
    except:
        pass
    return False


def regra_burger(fato):
    try:
        if fato["tipo"] == "hamburgueria" and fato["preco"] == "alto":
            fato["estabelecimento"] = "burger_king"
            return True
    except:
        pass
    return False


def regra_mcdonalds(fato):
    try:
        if fato["tipo"] == "hamburgueria" and fato["preco"] == "medio":
            fato["estabelecimento"] = "mcdonalds"
            return True
    except:
        pass
    return False


def regra_bobs(fato):
    try:
        if fato["tipo"] == "hamburgueria" and fato["preco"] == "baixo":
            fato["estabelecimento"] = "bobs"
            return True
    except:
        pass
    return False


def regra_pizzahut(fato):
    try:
        if fato["tipo"] == "pizzaria" and fato["preco"] == "alto":
            fato["estabelecimento"] = "pizza_hut"
            return True
    except:
        pass
    return False


def regra_dominos(fato):
    try:
        if fato["tipo"] == "pizzaria" and fato["preco"] == "medio":
            fato["estabelecimento"] = "dominos"
            return True
    except:
        pass
    return False


def regra_habibs(fato):
    try:
        if fato["tipo"] == "pizzaria" and fato["preco"] == "baixo":
            fato["estabelecimento"] = "habibs"
            return True
    except:
        pass
    return False
