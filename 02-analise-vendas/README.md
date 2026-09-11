# 📊 Análise de Vendas com Python e Pandas

Projeto de análise de dados desenvolvido com Python e Pandas com o objetivo de praticar análise exploratória de dados e criação de indicadores de negócio.

## 🎯 Objetivo

Analisar uma base de vendas e responder perguntas como:

- Qual é o faturamento total?
- Qual categoria gera maior faturamento?
- Qual produto possui maior faturamento?
- Qual cidade apresenta melhor desempenho?
- Como o faturamento evolui ao longo dos meses?
- Quais formas de pagamento são mais utilizadas?

## 🛠️ Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Git
- GitHub
- Sublime Text

## 📁 Estrutura do projeto

```text
02-analise-vendas/
├── dados/
│   └── vendas.csv
├── imagens/
│   ├── faturamento_categoria.png
│   └── faturamento_mes.png
├── analise_vendas.py
└── README.md
```
ranking_categoria = (
    df.groupby("Categoria")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
)

Salve com **Ctrl + S**.

### Um detalhe importante

O bloco da estrutura usa três crases:

````text

````text
...

e o exemplo Python também:

````text
````python
...
````
