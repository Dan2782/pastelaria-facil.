
# Pastelaria Fácil
# Controle básico de ingredientes

ingredientes = {
    "Farinha de trigo": {"quantidade": 2, "minimo": 5},
    "Queijo": {"quantidade": 4, "minimo": 2},
    "Oleo": {"quantidade": 1, "minimo": 3}
}


def verificar_estoque():
    """Mostra os ingredientes e identifica estoque baixo."""
    for nome, dados in ingredientes.items():
        quantidade = dados["quantidade"]
        minimo = dados["minimo"]

        if quantidade < minimo:
            status = "Estoque baixo"
        else:
            status = "Estoque adequado"

        print(f"{nome}: {quantidade} - {status}")


if __name__ == "__main__":
    verificar_estoque()
