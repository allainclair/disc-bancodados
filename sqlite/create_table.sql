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
