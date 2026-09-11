-- 1. Ver todas as vendas
SELECT * FROM vendas;

-- 2. Faturamento total
SELECT
    SUM(quantidade * preco_unitario) AS faturamento_total
FROM vendas;

-- 3. Faturamento por marca
SELECT
    marca,
    SUM(quantidade * preco_unitario) AS faturamento
FROM vendas
GROUP BY marca
ORDER BY faturamento DESC;

-- 4. Quantidade total de resíduos
SELECT
    SUM(quantidade_kg) AS total_residuos_kg
FROM residuos;

-- 5. Total de resíduos reciclados
SELECT
    SUM(quantidade_kg) AS total_reciclado_kg
FROM residuos
WHERE reciclado = TRUE;

-- 6. Valor recuperado com reciclagem
SELECT
    SUM(valor_recuperado) AS valor_total_recuperado
FROM residuos;

-- 7. Fornecedores sustentáveis
SELECT
    fornecedor,
    cidade,
    distancia_km
FROM fornecedores
WHERE politica_ambiental = TRUE
  AND embalagem_reciclavel = TRUE
  AND certificacao_ambiental = TRUE
ORDER BY distancia_km;

-- 1. Faturamento total
SELECT
    SUM(quantidade * preco_unitario) AS faturamento_total
FROM vendas;

-- 2. Faturamento por marca
SELECT
    marca,
    SUM(quantidade * preco_unitario) AS faturamento
FROM vendas
GROUP BY marca
ORDER BY faturamento DESC;

-- 3. Faturamento por cidade
SELECT
    cidade,
    SUM(quantidade * preco_unitario) AS faturamento
FROM vendas
GROUP BY cidade
ORDER BY faturamento DESC;

-- 4. Produto com maior faturamento
SELECT
    produto,
    SUM(quantidade * preco_unitario) AS faturamento
FROM vendas
GROUP BY produto
ORDER BY faturamento DESC
LIMIT 1;

-- 5. Vendedor com maior faturamento
SELECT
    vendedor,
    SUM(quantidade * preco_unitario) AS faturamento
FROM vendas
GROUP BY vendedor
ORDER BY faturamento DESC;

-- 6. Total de resíduos gerados
SELECT
    SUM(quantidade_kg) AS total_residuos_kg
FROM residuos;

-- 7. Total reciclado ou reutilizado
SELECT
    SUM(quantidade_kg) AS total_reciclado_kg
FROM residuos
WHERE reciclado = TRUE;

-- 8. Taxa de reciclagem
SELECT
    ROUND(
        100.0 * SUM(CASE WHEN reciclado = TRUE THEN quantidade_kg ELSE 0 END)
        / SUM(quantidade_kg),
        2
    ) AS taxa_reciclagem_percentual
FROM residuos;

-- 9. Valor recuperado com reciclagem
SELECT
    SUM(valor_recuperado) AS valor_total_recuperado
FROM residuos;

-- 10. Resíduos por tipo
SELECT
    tipo_residuo,
    SUM(quantidade_kg) AS total_kg,
    SUM(valor_recuperado) AS valor_recuperado
FROM residuos
GROUP BY tipo_residuo
ORDER BY total_kg DESC;

-- 11. Fornecedores sustentáveis
SELECT
    fornecedor,
    cidade,
    distancia_km
FROM fornecedores
WHERE politica_ambiental = TRUE
  AND embalagem_reciclavel = TRUE
  AND certificacao_ambiental = TRUE
ORDER BY distancia_km;

-- 12. Fornecedor sustentável mais próximo
SELECT
    fornecedor,
    cidade,
    distancia_km
FROM fornecedores
WHERE politica_ambiental = TRUE
  AND embalagem_reciclavel = TRUE
  AND certificacao_ambiental = TRUE
ORDER BY distancia_km
LIMIT 1;

