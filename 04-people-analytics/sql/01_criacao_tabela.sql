CREATE TABLE funcionarios (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    departamento VARCHAR(50) NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    data_admissao DATE NOT NULL,
    data_desligamento DATE,
    salario NUMERIC(10,2) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL,
    avaliacao_desempenho INT NOT NULL
);