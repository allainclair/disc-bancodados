## Queries de "recuperação" de dados (SELECT)

```SQL tab=
SELECT  <attribute list>
FROM    <table list>
WHERE   <condition>;
```

attribute list: lista de nomes dos atributos quais valores são recuperados pela
requisição (*query*);

table list: lista de nomes de tabelas (relações) requeridas para processar a
*query*;

condition: expressão **Booleana** que identifica as tuplas que serão recuperadas
pela *query*.

Operadores: =, <, <=, >, >= e <>

### Exemplos

#### Q1

Retrieve the birth date and address of the employee(s) whose name is ‘John B. Smith’.

```SQL tab=
SELECT  Bdate, Address
FROM    EMPLOYEE
WHERE   Fname = ‘John’ AND Minit = ‘B’ AND Lname = ‘Smith’;
``` 

Essa *query* envolve apenas a tabela EMPLOYEE listada na cláusula FROM. A *query*
*seleciona* as tuplas (linhas) que satisfazem a condição na cláusula WHERE, então
**projeta** o resultado nos atributos `Bdate` e `Address` listados na cláusula SELECT.

Podemos pensar que existe uma um iterador que passa por todas as linhas da tabela
EMPLOYEE e avalia a condição na cláusula WHERE. Apenas as linhas que satisfaçam
a condição (condição = TRUE) será projetada (selecionada).

#### Q2

Retrieve the name and address of all employees who work for the ‘Research’ department.

```SQL tab=
SELECT  Fname, Lname, Address
FROM    EMPLOYEE, DEPARTMENT
WHERE   Dname = ‘Research’ AND Dnumber = Dno;
```

A condição `Dname = ‘Research’` é a **condição de seleção** que escolhe uma
linha particular da tabela DEPARTMENT, porque Dname é um atributo da tabela
DEPARTAMENT. A condição Dnumer = Dno é chamada de **condição de junção**, porque
combina duas tuplas: uma do DEPARTMENT e outra do EMPLOYEE, sempre que o Dnumber
no DEPARTMENT é igual a Dno no EMPLOYEE.

#### Q3

For every project located in ‘Stafford’, list the project number, the controlling
department number, and the department manager’s last name, address, and birth date.

```SQL tab=
SELECT  Pnumber, Dnum, Lname, Address, Bdate
FROM    PROJECT, DEPARTMENT, EMPLOYEE
WHERE   Dnum = Dnumber AND Mgr_ssn = Ssn AND
        Plocation = ‘Stafford’
```

### Mais Exemplos

**Departamento**(<u>id</u>, nome, bloco)

**Empregado**(<u>id</u>, departamento_id, nome, sexo, salario, super_id)

#### DISTINCT

```SQL tab=
SELECT DISTINC salario FROM Empregado
```


## INSERT, DELETE, e UPDATE em SQL

Em SQL existem três comandos para **modificar** o banco de dados: INSERT, DELETE e
UPDATE.

### INSERT

Adiciona uma única tupla (*row*) em uma relação (*table*). É preciso especificar
a **tabela** e a lista de valores para a tupla (*row*). Os valores devem ser
especificados na mesma ordem dos atributos na tabela (de quando ela foi criada
por exemplo).

```SQL tab=
INSERT INTO     EMPLOYEE
VALUES          (‘Richard’, ‘K’, ‘Marini’, ‘653298653’, ‘1962-12-30’, ‘98
                Oak Forest, Katy, TX’, ‘M’, 37000, ‘653298653’, 4);
```

Uma outra forma de inserir é especificar explicitamente os nomes dos atributos.

```SQL tab=
INSERT INTO     EMPLOYEE (Fname, Lname, Dno, Ssn)
VALUES          (‘Richard’, ‘Marini’, 4, ‘653298653’);
```

Variação do INSERT com inserção de várias tuplas. É necessário fazer uma *query*
SELECT.

Tabela auxiliar:

```SQL tab=
CREATE TABLE    WORKS_ON_INFO
(Emp_name       VARCHAR (15),
 Proj_name      VARCHAR (15),
 Hours_per_week DECIMAL (3,1));
```

Inserção na tabela auxliar:

```SQL tab=
INSERT INTO     WORKS_ON_INFO (Emp_name, Proj_name,
                Hours_per_week)
SELECT          E.Lname, P.Pname, W.Hours
FROM            PROJECT P, WORKS_ON W, EMPLOYEE E
WHERE           P.Pnumber = W.Pno AND W.Essn = E.Ssn;
```








## Atributo (Attribute), Tipo de Dados (Data Types) e Domínios (Domains) em SQL

Os tipos básicos de dados disponíveis para atributos incluem: numérico, string de
caracteres, string de bits, booleano, data e tempo.

* Vários tamanhos de inteiros: INTEGER, INT e SMALLINT;

* Floating-point (real): FLOAT, REAL e DOUBLE PRECISION;

* Números formatados: DECIMAL(i, j), DEC(i, j) ou NUMERIC(i, j);

* String de caracteres: CHAR(n) e VARCHAR(n);

  * || operador de concatenação. `'ab' || 'cd' = 'abcd'`.

* Bit-string: BIT(n) ou BIT VARYING(n): `B'  10101 ' ou B'10101'`;

* Boolean: TRUE ou FALSE;

* Date: DATE: YEAR, MONTH, DAY: YYYY-MM-DD;

* Time: HOUR, MINUTE e SECOND;

* TIMESTAMP: 2014-09-27 09:12:47.648302.


### Domain

```SQL tab=
CREATE DOMAIN SSN_TYPE AS CHAR(9);
```

## Restrições (*Constraints*)

* NULL: Padrão é deixar campos nulos, logo é preciso configurar para NOT NULL. Isso
  é sempre válido para *primary key*;
  
* DEFAULT: é possível deixar um valor padrão DEFAULT <value>. Se não for especificado
  NULL é o padrão (DEFAULT), se não tiver a restrição NOT NULL.
  
## Especificar chaves

* PRIMARY KEY: `Dnumber INT PRIMARY KEY`;

* UNIQUE: especificação de chave alternativa: `Dname VARCHAR(15) UNIQUE`;

* FOREIGN KEY