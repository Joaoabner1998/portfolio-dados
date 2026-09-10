import pandas as pd
import matplotlib.pyplot as plt

# =========================
# CARREGAMENTO DOS DADOS
# =========================

df = pd.read_csv("dados/vendas.csv")

# =========================
# TRATAMENTO DOS DADOS
# =========================

df["Data"] = pd.to_datetime(df["Data"])

df["Faturamento"] = df["Quantidade"] * df["Preco"]

df["Mes"] = df["Data"].dt.month

# =========================
# VISUALIZAÇÃO INICIAL
# =========================

print("\n--- PRIMEIRAS LINHAS ---")
print(df.head())

print("\n--- INFORMAÇÕES DA BASE ---")
df.info()

# =========================
# INDICADORES
# =========================

faturamento_total = df["Faturamento"].sum()
quantidade_total = df["Quantidade"].sum()
ticket_medio = df["Faturamento"].mean()

print("\n--- FATURAMENTO TOTAL ---")
print(f"R$ {faturamento_total:.2f}")

print("\n--- QUANTIDADE TOTAL VENDIDA ---")
print(quantidade_total)

print("\n--- TICKET MÉDIO ---")
print(f"R$ {ticket_medio:.2f}")

# =========================
# FATURAMENTO POR CATEGORIA
# =========================

faturamento_categoria = df.groupby("Categoria")["Faturamento"].sum()

print("\n--- FATURAMENTO POR CATEGORIA ---")
print(faturamento_categoria)

# =========================
# FATURAMENTO POR CIDADE
# =========================

faturamento_cidade = df.groupby("Cidade")["Faturamento"].sum()

print("\n--- FATURAMENTO POR CIDADE ---")
print(faturamento_cidade)

# =========================
# FATURAMENTO POR MÊS
# =========================

faturamento_mes = df.groupby("Mes")["Faturamento"].sum()

print("\n--- FATURAMENTO POR MÊS ---")
print(faturamento_mes)

# =========================
# RANKING POR CATEGORIA
# =========================

ranking_categoria = (
    df.groupby("Categoria")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- RANKING DE FATURAMENTO POR CATEGORIA ---")
print(ranking_categoria)


# =========================
# RANKING POR CIDADE
# =========================

ranking_cidade = (
    df.groupby("Cidade")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- RANKING DE FATURAMENTO POR CIDADE ---")
print(ranking_cidade)


# =========================
# RANKING POR PRODUTO
# =========================

ranking_produto = (
    df.groupby("Produto")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- RANKING DE FATURAMENTO POR PRODUTO ---")
print(ranking_produto)

melhor_categoria = ranking_categoria.idxmax()
melhor_cidade = ranking_cidade.idxmax()
melhor_produto = ranking_produto.idxmax()

print("\n--- DESTAQUES ---")
print(f"Categoria com maior faturamento: {melhor_categoria}")
print(f"Cidade com maior faturamento: {melhor_cidade}")
print(f"Produto com maior faturamento: {melhor_produto}")

df.groupby("Categoria")["Faturamento"].sum()
# =========================
# FATURAMENTO POR FORMA DE PAGAMENTO
# =========================

ranking_pagamento = (
    df.groupby("FormaPagamento")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- FATURAMENTO POR FORMA DE PAGAMENTO ---")
print(ranking_pagamento)


# =========================
# FATURAMENTO POR MÊS
# =========================

ranking_mes = (
    df.groupby("Mes")["Faturamento"]
    .sum()
    .sort_index()
)

print("\n--- FATURAMENTO POR MÊS ---")
print(ranking_mes)

# =========================
# GRÁFICO 1 - FATURAMENTO POR CATEGORIA
# =========================

ranking_categoria.plot(kind="bar")

plt.title("Faturamento por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Faturamento")
plt.tight_layout()
plt.show()

# =========================
# GRÁFICO 2 - FATURAMENTO POR MÊS
# =========================

ranking_mes.plot(kind="line", marker="o")

plt.title("Faturamento por Mês")
plt.xlabel("Mês")
plt.ylabel("Faturamento")
plt.tight_layout()
plt.show()

