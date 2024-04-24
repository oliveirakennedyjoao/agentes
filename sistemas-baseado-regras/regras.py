def regra_restaurante(fato):
    try:
        if fato["tempo"] == "longo":
            fato["estabelecimento"] = "restaurante"
            return True
    except:
        pass
    return False


def regra_fastfood(fato):
    try:
        if fato["tempo"] == "curto":
            fato["estabelecimento"] = "fast_food"
            return True
    except:
        pass
    return False


def regra_brasileira(fato):
    try:
        if fato["estabelecimento"] == "restaurante" and fato["tipo_de_comida"] == "carne":
            fato["cozinha"] = "brasileira"
            return True
    except:
        pass
    return False


def regra_japonesa(fato):
    try:
        if fato["estabelecimento"] == "restaurante" and fato["tipo_de_comida"] == "sushi":
            fato["cozinha"] = "japonesa"
            return True
    except:
        pass
    return False


def regra_italiana(fato):
    try:
        if fato["estabelecimento"] == "restaurante" and fato["tipo_de_comida"] == "massa":
            fato["cozinha"] = "italiana"
            return True
    except:
        pass
    return False


def regra_hamburgueria(fato):
    try:
        if fato["estabelecimento"] == "fast_food" and fato["tipo_de_comida"] == "carne":
            fato["cozinha"] = "hamburgueria"
            return True
    except:
        pass
    return False


def regra_pizzaria(fato):
    try:
        if fato["estabelecimento"] == "fast_food" and fato["tipo_de_comida"] == "massa":
            fato["cozinha"] = "pizzaria"
            return True
    except:
        pass
    return False


def regra_bodega(fato):
    try:
        if fato["cozinha"] == "brasileira" and fato["preco"] == "baixo":
            fato["local"] = "bodega_do_arthur"
            return True
    except:
        pass
    return False


def regra_coco(fato):
    try:
        if fato["cozinha"] == "brasileira" and fato["preco"] == "medio":
            fato["local"] = "coco_bambu"
            return True
    except:
        pass
    return False


def regra_spettus(fato):
    try:
        if fato["cozinha"] == "brasileira" and fato["preco"] == "alto":
            fato["local"] = "spettus"
            return True
    except:
        pass
    return False


def regra_mazushi(fato):
    try:
        if fato["cozinha"] == "japonesa" and fato["preco"] == "alto":
            fato["local"] = "mazushi"
            return True
    except:
        pass
    return False


def regra_yugo(fato):
    try:
        if fato["cozinha"] == "japonesa" and fato["preco"] == "medio":
            fato["local"] = "yugo"
            return True
    except:
        pass
    return False


def regra_hashimoto(fato):
    try:
        if fato["cozinha"] == "japonesa" and fato["preco"] == "baixo":
            fato["local"] = "hashimoto"
            return True
    except:
        pass
    return False


def regra_furetti(fato):
    try:
        if fato["cozinha"] == "italiana" and fato["preco"] == "alto":
            fato["local"] = "furetti"
            return True
    except:
        pass
    return False


def regra_trattoria(fato):
    try:
        if fato["cozinha"] == "italiana" and fato["preco"] == "medio":
            fato["local"] = "la_trattoria"
            return True
    except:
        pass
    return False


def regra_famiglialucco(fato):
    try:
        if fato["cozinha"] == "italiana" and fato["preco"] == "baixo":
            fato["local"] = "famiglia_lucco"
            return True
    except:
        pass
    return False


def regra_burger(fato):
    try:
        if fato["cozinha"] == "hamburgueria" and fato["preco"] == "alto":
            fato["local"] = "burger_king"
            return True
    except:
        pass
    return False


def regra_mcdonalds(fato):
    try:
        if fato["cozinha"] == "hamburgueria" and fato["preco"] == "medio":
            fato["local"] = "mcdonalds"
            return True
    except:
        pass
    return False


def regra_bobs(fato):
    try:
        if fato["cozinha"] == "hamburgueria" and fato["preco"] == "baixo":
            fato["local"] = "bobs"
            return True
    except:
        pass
    return False


def regra_pizzahut(fato):
    try:
        if fato["cozinha"] == "pizzaria" and fato["preco"] == "alto":
            fato["local"] = "pizza_hut"
            return True
    except:
        pass
    return False


def regra_dominos(fato):
    try:
        if fato["cozinha"] == "pizzaria" and fato["preco"] == "medio":
            fato["local"] = "dominos"
            return True
    except:
        pass
    return False


def regra_habibs(fato):
    try:
        if fato["cozinha"] == "pizzaria" and fato["preco"] == "baixo":
            fato["local"] = "habibs"
            return True
    except:
        pass
    return False
