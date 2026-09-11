import pandas as pd
import matplotlib.pyplot as plt

vendas = pd.read_csv("../dados/vendas.csv")
residuos = pd.read_csv("../dados/residuos.csv")
fornecedores = pd.read_csv("../dados/fornecedores.csv")

print(vendas.head())
print(residuos.head())
print(fornecedores.head())

import pandas as pd

# -----------------------------
# LEITURA DOS ARQUIVOS
# -----------------------------

vendas = pd.read_csv("../dados/vendas.csv")
residuos = pd.read_csv("../dados/residuos.csv")
fornecedores = pd.read_csv("../dados/fornecedores.csv")


# -----------------------------
# TRATAMENTO DAS DATAS
# -----------------------------

vendas["Data"] = pd.to_datetime(vendas["Data"])
residuos["Data"] = pd.to_datetime(residuos["Data"])


# -----------------------------
# CÁLCULO DO FATURAMENTO
# -----------------------------

vendas["Faturamento"] = (
    vendas["Quantidade"] * vendas["Preco_Unitario"]
)


# -----------------------------
# INDICADORES DE VENDAS
# -----------------------------

faturamento_total = vendas["Faturamento"].sum()

quantidade_total = vendas["Quantidade"].sum()

ticket_medio = vendas["Faturamento"].mean()


print("===== INDICADORES DE VENDAS =====")

print(f"Faturamento total: R$ {faturamento_total:,.2f}")

print(f"Quantidade de rodas vendidas: {quantidade_total}")

print(f"Ticket médio por pedido: R$ {ticket_medio:,.2f}")


# -----------------------------
# FATURAMENTO POR MARCA
# -----------------------------

faturamento_marca = (
    vendas.groupby("Marca")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== FATURAMENTO POR MARCA =====")
print(faturamento_marca)


# -----------------------------
# FATURAMENTO POR CIDADE
# -----------------------------

faturamento_cidade = (
    vendas.groupby("Cidade")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== FATURAMENTO POR CIDADE =====")
print(faturamento_cidade)


# -----------------------------
# PRODUTOS MAIS VENDIDOS
# -----------------------------

produtos_vendidos = (
    vendas.groupby("Produto")["Quantidade"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== PRODUTOS MAIS VENDIDOS =====")
print(produtos_vendidos)


# -----------------------------
# ANÁLISE DE RESÍDUOS
# -----------------------------

total_residuos = residuos["Quantidade_Kg"].sum()

residuos_reciclados = residuos[
    residuos["Reciclado"] == "Sim"
]["Quantidade_Kg"].sum()

taxa_reciclagem = (
    residuos_reciclados / total_residuos
) * 100

valor_recuperado = residuos[
    "Valor_Recuperado"
].sum()


print("\n===== INDICADORES DE SUSTENTABILIDADE =====")

print(f"Total de resíduos gerados: {total_residuos} kg")

print(f"Total reciclado/reutilizado: {residuos_reciclados} kg")

print(f"Taxa de reciclagem: {taxa_reciclagem:.2f}%")

print(f"Valor recuperado: R$ {valor_recuperado:,.2f}")


# -----------------------------
# RESÍDUOS POR TIPO
# -----------------------------

residuos_tipo = (
    residuos.groupby("Tipo_Residuo")["Quantidade_Kg"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== RESÍDUOS POR TIPO =====")
print(residuos_tipo)


# -----------------------------
# ANÁLISE DOS FORNECEDORES
# -----------------------------

fornecedores_sustentaveis = fornecedores[
    (fornecedores["Politica_Ambiental"] == "Sim")
    & (fornecedores["Embalagem_Reciclavel"] == "Sim")
    & (fornecedores["Certificacao_Ambiental"] == "Sim")
]

print("\n===== FORNECEDORES SUSTENTÁVEIS =====")

print(
    fornecedores_sustentaveis[
        [
            "Fornecedor",
            "Cidade",
            "Distancia_Km"
        ]
    ]
)

# -----------------------------
# GRÁFICO - FATURAMENTO POR MARCA
# -----------------------------

faturamento_marca.plot(
    kind="bar",
    title="Faturamento por Marca"
)

plt.xlabel("Marca")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("../imagens/faturamento_por_marca.png")
plt.close()

vendas["Mes"] = vendas["Data"].dt.to_period("M")

faturamento_mes = (
    vendas.groupby("Mes")["Faturamento"]
    .sum()
)

faturamento_mes.index = faturamento_mes.index.astype(str)
# -----------------------------
# GRÁFICO - RESÍDUOS POR TIPO
# -----------------------------

residuos_tipo.plot(
    kind="bar",
    title="Resíduos Gerados por Tipo"
)

plt.xlabel("Tipo de Resíduo")
plt.ylabel("Quantidade (kg)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("../imagens/residuos_por_tipo.png")
plt.close()

faturamento_mes.plot(
    kind="line",
    marker="o",
    title="Evolução Mensal do Faturamento"
)

plt.xlabel("Mês")
plt.ylabel("Faturamento (R$)")
plt.grid(True)
plt.tight_layout()

plt.savefig("../imagens/faturamento_mensal.png")
plt.close()
vendas["Data"].dt.to_period("M")