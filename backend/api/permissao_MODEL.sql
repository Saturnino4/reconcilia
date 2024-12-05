CREATE TABLE utilizador (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE
    -- outros campos como senha, e-mail, etc.
);
 
 
CREATE TABLE role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE permissao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    module VARCHAR(50) NOT NULL,
    autorizacao VARCHAR(4) NOT NULL
    -- O campo `permissao` pode ser 'rwdu' ou qualquer combinação das permissões
);


CREATE TABLE utilizador_role (
    utilizador_id INT,
    role_id INT,
    PRIMARY KEY (utilizador_id, role_id),
    FOREIGN KEY (utilizador_id) REFERENCES utilizador(id),
    FOREIGN KEY (role_id) REFERENCES role(id)
);


CREATE TABLE role_permissao (
    role_id INT,
    permission_id INT,
    PRIMARY KEY (role_id, permission_id),
    FOREIGN KEY (role_id) REFERENCES role(id),
    FOREIGN KEY (permission_id) REFERENCES permissao(id)
);


--- Inserindo dados

INSERT INTO utilizador (username) VALUES ('admin');

INSERT INTO role (name) VALUES ('admin');


INSERT INTO permissao (module, permissao) VALUES
('cliente', 'rwdu'),
('financas', 'rwd');



--- Atribuindo permissões a role

SELECT id FROM permissao WHERE module = 'cliente' AND permissao = 'rwdu';


-- associoa a permissão a role

INSERT INTO role_permissao (role_id, permission_id)
SELECT r.id, p.id
FROM role r, permissao p
WHERE r.name = 'admin_cliente'
AND p.module = 'cliente'
AND p.permissao = 'rwdu';


-- Atribuindo role a usuários

INSERT INTO utilizador_role (utilizador_id, role_id)
SELECT u.id, r.id
FROM utilizador u, role r
WHERE u.username = 'joao'
AND r.name = 'admin_cliente';


-- Verificando permissões

-- SELECT p.module, p.permissao
-- FROM utilizador u
-- JOIN utilizador_role ur ON u.id = ur.utilizador_id
-- JOIN role r ON ur.role_id = r.id
-- JOIN role_permissao rp ON r.id = rp.role_id
-- JOIN permissao p ON rp.permission_id = p.id
-- WHERE u.username = 'joao';


SELECT
    p.modulo,
    p.autorizacao
FROM utilizador u
JOIN utilizador_role ur ON u.id = ur.utilizador_id
JOIN role r ON ur.role_id = r.id
JOIN role_permissao rp ON r.id = rp.role_id
JOIN permissao p ON rp.permissao_id = p.id
WHERE u.id = 1;