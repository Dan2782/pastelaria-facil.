
# Pastelaria Facil - Controle de despesas
# Este modulo registra os gastos da pastelaria.
# Tambem permite calcular o total das despesas.
# Faz parte do projeto MVP Pastelaria Facil.


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
