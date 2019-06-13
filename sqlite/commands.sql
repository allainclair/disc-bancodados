/* Tabelas */

CREATE TABLE Departamento(
    id INT,
    nome VARCHAR(100)   UNIQUE,
    bloco VARCHAR(10),
    PRIMARY KEY (id)
);


CREATE TABLE Empregado(
    id INT,
    departamento_id INT,
    nome VARCHAR(100),
    sexo CHAR,
    salario DECIMAL(10, 2),
    super_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (departamento_id) REFERENCES Departamento(id)
);


/* Insercoes na tabela Departamento */

INSERT INTO Departamento(id, nome, bloco)
VALUES      (1, 'Estatistica', 'E90');

INSERT INTO Departamento(id, nome, bloco)
VALUES      (2, 'Informatica', 'C56');

INSERT INTO Departamento(id, nome, bloco)
VALUES      (3, 'Biologia', 'A20');

INSERT INTO Departamento(id, nome, bloco)
VALUES      (4, 'Matematica', 'F10');

INSERT INTO Departamento(id, nome, bloco)
VALUES      (5, 'Economia', 'F10');

INSERT INTO Departamento(id, nome, bloco)
VALUES      (6, 'Farmacia', 'A20');

/* Nome duplicado.
*  INSERT INTO Departamento(id, nome, bloco)
*  VALUES      (5, 'Estatistica', 'E90'); */


/* Insercoes na tabela Empregado */

INSERT INTO Empregado(id, departamento_id, nome, sexo, salario, super_id)
VALUES      (1, 1, 'Joao', 'M', 1000, NULL);

INSERT INTO Empregado(id, departamento_id, nome, sexo, salario, super_id)
VALUES      (2, 2, 'Maria', 'F', 1200, 1);

INSERT INTO Empregado(id, departamento_id, nome, sexo, salario, super_id)
VALUES      (3, 3, 'Marco', 'M', 1300, 2);

INSERT INTO Empregado(id, departamento_id, nome, sexo, salario, super_id)
VALUES      (4, 4, 'Marcio', 'M', 1400, 2);

INSERT INTO Empregado(id, departamento_id, nome, sexo, salario, super_id)
VALUES      (5, 1, 'Jose', 'M', 1400, 2);

INSERT INTO Empregado(id, departamento_id, nome, sexo, salario, super_id)
VALUES      (6, 6, 'Hugo', 'M', 1500, 3);

INSERT INTO Empregado(id, departamento_id, nome, sexo, salario, super_id)
VALUES      (7, 6, 'Beatriz', 'F', 1300, 3);

INSERT INTO Empregado(id, departamento_id, nome, sexo, salario, super_id)
VALUES      (8, 2, 'Aline', 'F', 1350, 1);

INSERT INTO Empregado(id, departamento_id, nome, sexo, salario, super_id)
VALUES      (9, 1, 'Hamilton', 'M', 1300, 4);


/* Seleciona todas (*) as colunas da tabela Empregado. */
/* SELECT * FROM Empregado; */

/* Seleciona todas (*) as colunas da tabela Departamento. */
/* SELECT * FROM Departamento; */


/* Seleciona apenas nome e sexo da tabela Empregado. */
/* SELECT nome, sexo FROM Empregado; */

/* Seleciona apenas nome e salario da tabela Empregado. */
/* SELECT nome, salario FROM Empregado; */

/* Seleciona apenas nome e id do supervisor da tabela Empregado. */
/* SELECT nome, super_id FROM Empregado; */


/* Seleciona nome e bloco da tabela Departamento. */
/* SELECT nome, bloco FROM Departamento; */

/* Seleciona nome e salario (> 1100) da tabela Empregado. */
/* SELECT nome, salario FROM Empregado WHERE salario > 1100; */

/* Seleciona id e nome da tabela Departamento. Onde bloco = 'F10' */
/* SELECT id, nome FROM Departamento WHERE bloco = 'F10'; */

/* SELECT ALL salario FROM Empregado */
/* SELECT DISTINCT salario FROM Empregado */
/* SELECT DISTINCT nome, salario FROM Empregado; */

/* SELECT *
*  FROM Empregado AS E, Departamento AS D; */

/* SELECT E.nome, E.salario, D.nome
*  FROM Empregado AS E, Departamento AS D;*/

/* SELECT E.nome, E.salario, D.nome
*  FROM Empregado AS E, Departamento AS D
*  WHERE D.nome = 'Informatica'; */

/* SELECT E.nome, E.salario, D.nome
*  FROM Empregado AS E, Departamento AS D
*  WHERE D.nome = 'Informatica' AND E.departamento_id = D.id; */

/* SELECT nome, salario
* FROM Empregado
ORDER BY salario; */

/* SELECT nome, salario
* FROM Empregado
ORDER BY salario DESC; */

/* SELECT nome, salario
* FROM Empregado
* ORDER BY salario, nome */

/* SELECT nome, salario
* FROM Empregado
* WHERE salario BETWEEN 1200 AND 1350; */

/* SELECT nome, salario
* FROM Empregado
* WHERE salario BETWEEN 1200 AND 1350; */

/* SELECT nome, salario, super_id
*  FROM Empregado
*  WHERE super_id IS NOT NULL; */

/* SELECT nome, salario
*  FROM Empregado
*  WHERE nome LIKE '_a%'; */

/* SELECT count(*)
*  FROM Empregado; */

/* SELECT COUNT(*)
*  FROM Departamento; */

/* SELECT SUM(salario)
*  FROM Empregado;*/
