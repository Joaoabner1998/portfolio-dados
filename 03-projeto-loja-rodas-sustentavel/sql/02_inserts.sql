INSERT INTO vendas
(data, pedido, produto, marca, aro, quantidade, preco_unitario, cidade, vendedor, forma_pagamento)
VALUES
('2026-01-05', 'P001', 'Roda Volcano Strong', 'Volcano', 17, 4, 850.00, 'Maua', 'Carlos', 'Pix'),
('2026-01-08', 'P002', 'Roda KR R70', 'KR', 18, 4, 1200.00, 'Santo Andre', 'Ana', 'Cartao'),
('2026-01-11', 'P003', 'Roda GT7 Strong', 'GT7', 20, 4, 1650.00, 'Sao Paulo', 'Bruno', 'Cartao');

INSERT INTO residuos
(data, tipo_residuo, quantidade_kg, destino, valor_recuperado, reciclado)
VALUES
('2026-01-05', 'Aluminio', 18, 'Reciclagem', 140.00, TRUE),
('2026-01-08', 'Papelao', 12, 'Reciclagem', 20.00, TRUE),
('2026-01-11', 'Plastico', 6, 'Reciclagem', 12.00, TRUE),
('2026-01-21', 'Plastico', 8, 'Descarte', 0.00, FALSE);

INSERT INTO fornecedores
(fornecedor, cidade, distancia_km, politica_ambiental, embalagem_reciclavel, certificacao_ambiental)
VALUES
('Rodas Alpha', 'Sao Paulo', 25, TRUE, TRUE, TRUE),
('Distribuidora Beta', 'Campinas', 110, FALSE, TRUE, FALSE),
('Rodas Premium', 'Santo Andre', 12, TRUE, TRUE, TRUE);