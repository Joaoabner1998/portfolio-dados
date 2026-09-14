-- 1. Total de funcionários
SELECT COUNT(*) AS total_funcionarios
FROM funcionarios;


-- 2. Funcionários ativos
SELECT COUNT(*) AS funcionarios_ativos
FROM funcionarios
WHERE status = 'Ativo';


-- 3. Funcionários desligados
SELECT COUNT(*) AS funcionarios_desligados
FROM funcionarios
WHERE status = 'Desligado';


-- 4. Salário médio
SELECT ROUND(AVG(salario), 2) AS salario_medio
FROM funcionarios;


-- 5. Avaliação média de desempenho
SELECT ROUND(AVG(avaliacao_desempenho), 2) AS avaliacao_media
FROM funcionarios;


-- 6. Quantidade de funcionários por departamento
SELECT
    departamento,
    COUNT(*) AS quantidade_funcionarios
FROM funcionarios
GROUP BY departamento
ORDER BY quantidade_funcionarios DESC;


-- 7. Salário médio por departamento
SELECT
    departamento,
    ROUND(AVG(salario), 2) AS salario_medio
FROM funcionarios
GROUP BY departamento
ORDER BY salario_medio DESC;


-- 8. Desligamentos por departamento
SELECT
    departamento,
    COUNT(*) AS quantidade_desligados
FROM funcionarios
WHERE status = 'Desligado'
GROUP BY departamento
ORDER BY quantidade_desligados DESC;


-- 9. Taxa geral de desligamento
SELECT
    ROUND(
        COUNT(*) FILTER (WHERE status = 'Desligado') * 100.0
        / COUNT(*),
        2
    ) AS taxa_desligamento
FROM funcionarios;


-- 10. Taxa de desligamento por departamento
SELECT
    departamento,
    COUNT(*) AS total_funcionarios,
    COUNT(*) FILTER (
        WHERE status = 'Desligado'
    ) AS desligados,

    ROUND(
        COUNT(*) FILTER (
            WHERE status = 'Desligado'
        ) * 100.0 / COUNT(*),
        2
    ) AS taxa_desligamento
FROM funcionarios
GROUP BY departamento
ORDER BY taxa_desligamento DESC;


-- 11. Desempenho médio por status
SELECT
    status,
    ROUND(AVG(avaliacao_desempenho), 2) AS desempenho_medio
FROM funcionarios
GROUP BY status;


-- 12. Funcionários por avaliação e status
SELECT
    avaliacao_desempenho,
    status,
    COUNT(*) AS quantidade
FROM funcionarios
GROUP BY avaliacao_desempenho, status
ORDER BY avaliacao_desempenho, status;


-- 13. Tempo médio de empresa
SELECT
    ROUND(
        AVG(
            EXTRACT(
                DAY FROM
                (
                    COALESCE(
                        data_desligamento,
                        DATE '2026-09-11'
                    )
                    - data_admissao
                )
            ) / 365.25
        ),
        2
    ) AS tempo_medio_anos
FROM funcionarios;


-- =========================================
-- 1. INDICADORES GERAIS
-- =========================================

SELECT
    COUNT(*) AS total_funcionarios,
    COUNT(*) FILTER (WHERE status = 'Ativo') AS ativos,
    COUNT(*) FILTER (WHERE status = 'Desligado') AS desligados,
    ROUND(AVG(salario), 2) AS salario_medio,
    ROUND(AVG(avaliacao_desempenho), 2) AS avaliacao_media
FROM funcionarios;


-- =========================================
-- 2. FUNCIONÁRIOS POR DEPARTAMENTO
-- =========================================

SELECT
    departamento,
    COUNT(*) AS quantidade
FROM funcionarios
GROUP BY departamento
ORDER BY quantidade DESC;


-- =========================================
-- 3. SALÁRIO MÉDIO POR DEPARTAMENTO
-- =========================================

SELECT
    departamento,
    ROUND(AVG(salario), 2) AS salario_medio
FROM funcionarios
GROUP BY departamento
ORDER BY salario_medio DESC;


-- =========================================
-- 4. DESLIGAMENTOS POR DEPARTAMENTO
-- =========================================

SELECT
    departamento,
    COUNT(*) AS desligados
FROM funcionarios
WHERE status = 'Desligado'
GROUP BY departamento
ORDER BY desligados DESC;


-- =========================================
-- 5. TAXA DE DESLIGAMENTO POR DEPARTAMENTO
-- =========================================

SELECT
    departamento,
    COUNT(*) AS total_funcionarios,

    COUNT(*) FILTER (
        WHERE status = 'Desligado'
    ) AS desligados,

    ROUND(
        COUNT(*) FILTER (
            WHERE status = 'Desligado'
        ) * 100.0 / COUNT(*),
        2
    ) AS taxa_desligamento
FROM funcionarios
GROUP BY departamento
ORDER BY taxa_desligamento DESC;


-- =========================================
-- 6. DESEMPENHO MÉDIO POR STATUS
-- =========================================

SELECT
    status,
    ROUND(AVG(avaliacao_desempenho), 2) AS desempenho_medio
FROM funcionarios
GROUP BY status
ORDER BY status;