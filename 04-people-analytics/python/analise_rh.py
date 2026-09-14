import pandas as pd
import matplotlib.pyplot as plt


funcionarios = pd.read_csv("../dados/funcionarios.csv")

print("=== PRIMEIRAS LINHAS ===")
print(funcionarios.head())

print("\n=== INFORMAÇÕES DA BASE ===")
print(funcionarios.info())

print("\n=== QUANTIDADE DE FUNCIONÁRIOS ===")
print(len(funcionarios))

# Funcionários ativos
ativos = funcionarios[funcionarios["Status"] == "Ativo"]
quantidade_ativos = len(ativos)

# Funcionários desligados
desligados = funcionarios[funcionarios["Status"] == "Desligado"]
quantidade_desligados = len(desligados)

# Salário médio
salario_medio = funcionarios["Salario"].mean()

# Avaliação média
avaliacao_media = funcionarios["Avaliacao_Desempenho"].mean()

print("\n=== INDICADORES DE RH ===")
print("Funcionários ativos:", quantidade_ativos)
print("Funcionários desligados:", quantidade_desligados)
print("Salário médio: R$", round(salario_medio, 2))
print("Avaliação média:", round(avaliacao_media, 2))
salario_departamento = (
    funcionarios.groupby("Departamento")["Salario"]
    .mean()
    .sort_values(ascending=False)
)

print("\n=== SALÁRIO MÉDIO POR DEPARTAMENTO ===")
print(salario_departamento)
funcionarios_departamento = (
    funcionarios.groupby("Departamento")["ID"]
    .count()
    .sort_values(ascending=False)
)

print("\n=== FUNCIONÁRIOS POR DEPARTAMENTO ===")
print(funcionarios_departamento)

# Taxa de desligamento
total_funcionarios = len(funcionarios)

taxa_desligamento = (
    quantidade_desligados / total_funcionarios
) * 100

print("\n=== TAXA DE DESLIGAMENTO ===")
print(f"{taxa_desligamento:.2f}%")

# Converter datas
funcionarios["Data_Admissao"] = pd.to_datetime(
    funcionarios["Data_Admissao"]
)

funcionarios["Data_Desligamento"] = pd.to_datetime(
    funcionarios["Data_Desligamento"],
    errors="coerce"
)
# Tempo de empresa em anos

data_referencia = pd.Timestamp("2026-09-11")

funcionarios["Data_Final"] = funcionarios[
    "Data_Desligamento"
].fillna(data_referencia)

funcionarios["Tempo_Empresa_Anos"] = (
    funcionarios["Data_Final"]
    - funcionarios["Data_Admissao"]
).dt.days / 365.25

tempo_medio = funcionarios[
    "Tempo_Empresa_Anos"
].mean()

print("\n=== TEMPO MÉDIO DE EMPRESA ===")
print(round(tempo_medio, 2), "anos")

tempo_por_status = (
    funcionarios.groupby("Status")[
        "Tempo_Empresa_Anos"
    ]
    .mean()
)

print("\n=== TEMPO MÉDIO POR STATUS ===")
print(tempo_por_status)

# Desligamentos por departamento
desligamentos_departamento = (
    desligados.groupby("Departamento")["ID"]
    .count()
    .sort_values(ascending=False)
)

print("\n=== DESLIGAMENTOS POR DEPARTAMENTO ===")
print(desligamentos_departamento)

# Total de funcionários por departamento
total_por_departamento = (
    funcionarios.groupby("Departamento")["ID"]
    .count()
)

# Taxa de desligamento por departamento
taxa_por_departamento = (
    desligamentos_departamento / total_por_departamento * 100
).fillna(0).sort_values(ascending=False)

print("\n=== TAXA DE DESLIGAMENTO POR DEPARTAMENTO ===")
print(taxa_por_departamento.round(2))

desempenho_status = (
    funcionarios.groupby("Status")["Avaliacao_Desempenho"]
    .mean()
)

print("\n=== DESEMPENHO MÉDIO POR STATUS ===")
print(desempenho_status.round(2))

desligamentos_desempenho = (
    funcionarios.groupby(
        ["Avaliacao_Desempenho", "Status"]
    )["ID"]
    .count()
)

print("\n=== DESEMPENHO X STATUS ===")
print(desligamentos_desempenho)

funcionarios_departamento.plot(
    kind="bar",
    title="Funcionários por Departamento"
)

plt.xlabel("Departamento")
plt.ylabel("Quantidade de Funcionários")
plt.tight_layout()

plt.savefig("../imagens/funcionarios_departamento.png")
plt.close()
salario_departamento.plot(
    kind="bar",
    title="Salário Médio por Departamento"
)

plt.xlabel("Departamento")
plt.ylabel("Salário Médio (R$)")
plt.tight_layout()

plt.savefig("../imagens/salario_departamento.png")
plt.close()

taxa_por_departamento.plot(
    kind="bar",
    title="Taxa de Desligamento por Departamento"
)

plt.xlabel("Departamento")
plt.ylabel("Taxa de Desligamento (%)")
plt.tight_layout()

plt.savefig("../imagens/taxa_desligamento_departamento.png")
plt.close()