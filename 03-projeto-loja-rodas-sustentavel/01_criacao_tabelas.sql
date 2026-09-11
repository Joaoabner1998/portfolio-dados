CREATE TABLE vendas (
    id_venda SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    pedido VARCHAR(20) UNIQUE NOT NULL,
    produto VARCHAR(100) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    aro INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario NUMERIC(10,2) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    vendedor VARCHAR(50) NOT NULL,
    forma_pagamento VARCHAR(30) NOT NULL
);

CREATE TABLE residuos (
    id_residuo SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    tipo_residuo VARCHAR(50) NOT NULL,
    quantidade_kg NUMERIC(10,2) NOT NULL,
    destino VARCHAR(50) NOT NULL,
    valor_recuperado NUMERIC(10,2) NOT NULL,
    reciclado BOOLEAN NOT NULL
);

CREATE TABLE fornecedores (
    id_fornecedor SERIAL PRIMARY KEY,
    fornecedor VARCHAR(100) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    distancia_km NUMERIC(10,2) NOT NULL,
    politica_ambiental BOOLEAN NOT NULL,
    embalagem_reciclavel BOOLEAN NOT NULL,
    certificacao_ambiental BOOLEAN NOT NULL
);