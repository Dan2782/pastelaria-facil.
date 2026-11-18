
# Pastelaria Facil
# Registro basico de vendas e pagamentos fiados

vendas = []


def registrar_venda(cliente, valor, forma_pagamento):
    if not cliente.strip():
        raise ValueError("Informe o nome do cliente.")

    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")

    if forma_pagamento not in ("Fiado", "Pago"):
        raise ValueError("Forma de pagamento invalida.")

    venda = {
        "cliente": cliente,
        "valor": valor,
        "forma_pagamento": forma_pagamento
    }

    vendas.append(venda)
    return venda


def consultar_fiados(cliente):
    return sum(
        venda["valor"]
        for venda in vendas
        if venda["cliente"] == cliente
        and venda["forma_pagamento"] == "Fiado"
    )


if __name__ == "__main__":
    registrar_venda("Joao Silva", 30.00, "Fiado")
    registrar_venda("Maria", 15.00, "Pago")

    print("Vendas registradas:", len(vendas))
    print("Saldo fiado de Joao Silva: R$",
          consultar_fiados("Joao Silva"))
