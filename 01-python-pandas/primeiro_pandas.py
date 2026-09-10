import pandas as pd

# =========================
# CARREGAMENTO DOS DADOS
# =========================

df = pd.read_csv("dados/vendas.csv")

# =========================
# TRATAMENTO DOS DADOS
# =========================

df["Faturamento"] = df["Quantidade"] * df["Preco"]

# =========================
# VISUALIZAÇÃO
# =========================

print("\n--- BASE DE VENDAS ---")
print(df)

print("\n--- INFORMAÇÕES DA BASE ---")
df.info()

print("\n--- ESTATÍSTICAS ---")
print(df.describe())

# =========================
# INDICADORES
# =========================

faturamento_total = df["Faturamento"].sum()

print("\n--- FATURAMENTO TOTAL ---")
print(f"R$ {faturamento_total:.2f}")

produto_maior_faturamento = df.loc[df["Faturamento"].idxmax()]

print("\n--- PRODUTO COM MAIOR FATURAMENTO ---")
print(produto_maior_faturamento)


produtos_caros = df[df["Preco"] > 500]

print("\n--- PRODUTOS ACIMA DE R$ 500 ---")
print(produtos_caros)

df["Preco"] > 500

df[df["Preco"] > 500]

ranking_faturamento = df.sort_values(
    by="Faturamento",
    ascending=False
)

print("\n--- RANKING DE FATURAMENTO ---")
print(ranking_faturamento)

ascending=False

ascending=True

print(
    ranking_faturamento[
        ["Produto", "Faturamento"]
    ]
)

top_3 = ranking_faturamento[
    ["Produto", "Faturamento"]
].head(3)

print("\n--- TOP 3 PRODUTOS POR FATURAMENTO ---")
print(top_3)