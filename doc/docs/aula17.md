## SELECT de várias tabelas

* Combinação de todas as linhas: Produto Cartesiano

### Exemplo simples

* Criar tabelas Nome1(a1, a2), Nome2(b1, b2) e Nome3(c)

* Inserir dados nas tabelas

```SQL tab=
INSERT INTO Nome1(a1, a2)
VALUES      ('Marco', 'Mauricio');

INSERT INTO Nome1(a1, a2)
VALUES      ('Allan', 'Alladin');

INSERT INTO Nome2(b1, b2)
VALUES      ('Erica', 'Estela');

INSERT INTO Nome2(b1, b2)
VALUES      ('Bruna', 'Beatriz');

INSERT INTO Nome3(c)
VALUES      ('Hamilton');

INSERT INTO Nome3(c)
VALUES      ('Hugo');
```

* Selecionar multiplas tabelas

```SQL tab=
SELECT *
FROM   Nome1, Nome2;

SELECT *
FROM   Nome1, Nome2, Nome3;
```

### Exemplos Empregado/Departamento

* ORDER BY;

* DISTINCT;

* BETWEEN;

* IS NOT NULL;

* LIKE

    * % zero, um ou vávrios caracteres;

    * _ um caracter.

### Agrupamentos

* COUNT

* SUM

* AVG

* MIN

* MAX
