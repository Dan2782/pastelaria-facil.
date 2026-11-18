
despesas = []

def registrar_despesa(descricao, valor):
    if valor <= 0:
        raise ValueError("O valor deve ser positivo.")

    despesa = {
        "descricao": descricao,
        "valor": valor
    }

    despesas.append(despesa)
    return "Despesa registrada com sucesso!"


def calcular_total_despesas():
    return sum(despesa["valor"] for despesa in despesas)
