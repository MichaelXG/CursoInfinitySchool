-- [PY-A16] Você está criando um banco de dados simples para registrar informações pessoais das pessoas. 
-- O banco terá uma tabela com colunas para ID, nome completo, idade, gênero, nacionalidade, e-mail, 
-- estado civil, nome do pai e nome da mãe. Após criar o banco, você adiciona três pessoas como exemplo. 
-- Agora, pense em uma pessoa que você conhece e escolha um número para ser o ID dela. Essa pessoa será 
-- atualizada com novas informações. Em seguida, escolha outro número de ID de uma pessoa que deseja 
-- remover completamente do banco de dados.

-- Criação do banco de dados pessoal
CREATE DATABASE IF NOT EXISTS Personal_Info;

-- Seleção do banco de dados
USE Personal_Info;

-- Criação da tabela Pessoas
CREATE TABLE IF NOT EXISTS Pessoas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    genero ENUM('Masculino', 'Feminino', 'Outro') NOT NULL,
    nacionalidade VARCHAR(50),
    email VARCHAR(100) UNIQUE NOT NULL,
    estado_civil ENUM('Solteiro', 'Casado', 'Divorciado', 'Viúvo') NOT NULL,
    nome_pai VARCHAR(100),
    nome_mae VARCHAR(100)
);

-- Inserção de registros de exemplo
INSERT INTO Pessoas (nome_completo, idade, genero, nacionalidade, email, estado_civil, nome_pai, nome_mae)
VALUES
('João Silva', 30, 'Masculino', 'Brasileira', 'joao.silva@email.com', 'Solteiro', 'Carlos Silva', 'Ana Silva'),
('Maria Oliveira', 28, 'Feminino', 'Brasileira', 'maria.oliveira@email.com', 'Casada', 'João Oliveira', 'Lúcia Oliveira'),
('Pedro Santos', 35, 'Masculino', 'Brasileiro', 'pedro.santos@email.com', 'Divorciado', 'Paulo Santos', 'Maria Santos');


-- Atualizar informações da pessoa com ID 1
UPDATE Pessoas
SET idade = 31, email = 'joao.silva.novo@email.com', nacionalidade = 'Brasileiro'
WHERE id = 1;


-- Remover a pessoa com ID 3
DELETE FROM Pessoas
WHERE id = 3;
