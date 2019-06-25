## Formato do SELECT

```SQL tab=
SELECT     <attribute list>
FROM       <table list>
[ WHERE    <condition> ]
[ ORDER BY <attribute list> ];
```

[...] Significa opcional.

## Selecionar informações

* Selecionar todos empregados por ordem de salario;

* Selecionar todos os salários distindos ordenados de forma descrescente;

* Selecionar todos os salários ordenados de forma crescente do departamento de
  estatística;

* Selecionar todos dependentes "Filhos" e "Filhas" de todos empregados;

* Mostrar salários dos empregados de um projeto do departamento de informática
  em ordem crescente;

* Somar os salários do departamento de Estatística;

* Ver maior salário do departamento de Informática;

* Contar quantos projetos existem no do departamento de Física;

```SQL tab=
SELECT
```

```SQL tab=
SELECT COUNT(D.nome)
FROM   Projeto P, Departamento D
WHERE  D.nome = 'Fisica' AND P.departamento_id = D.id
```

* Fazer a média dos salários dos departamentos de Matemática e Física;

* Mostrar nomes dos dependentes dos empregados do departamento de Informática
  Ordenados alfabeticamente;

```SQL tab=
SELECT
```

```SQL tab=
SELECT   E.pnome, E.unome, D.nome
FROM     Empregado E, Dependente D, Departamento Dep
WHERE    Dep.nome = 'Informatica'
         AND E.departamento_id = Dep.id
	     AND E.id = D.empregado_id
ORDER BY D.nome
```

* Selecionar empregados que trabalham nos projetos do departamento de  
  estatística que tem mais de 500 horas de projeto. Ordenar pelas horas de projeto.

```SQL tab=
SELECT
```

```SQL tab=
SELECT E.pnome, D.nome, P.nome, TE.horas
FROM   Departamento D, Projeto P, Empregado E, TrabalhaEm TE
WHERE  D.nome = 'Estatistica'
       AND P.departamento_id = D.id
	   AND E.departamento_id = D.id
	   AND TE.empregado_id = E.id
	   AND TE.projeto_id = P.id
	   AND TE.horas > 500
ORDER BY TE.horas
```

* Para cada departamento, traga o número do deparatmento, o número de empregados
  no deparatmento e a média de salário.

```SQL tab=
SELECT
```

```SQL tab=
SELECT   departamento_id, COUNT(*) AS num_empregados, AVG(salario)
FROM     Empregado
GROUP BY departamento_id
```

* Para cada projeto, traga o número do projeto, o nome do projeto e o número de
  empregados que trabalham nesse projeto. Em outra *query* traga apenas os projetos que tenham mais do que um empregado.

  ```SQL tab=
  SELECT
  ```

  ```SQL tab=
  SELECT   id, nome, COUNT(*) AS num_empregados
  FROM     Projeto, TrabalhaEm
  WHERE    id = projeto_id
  GROUP BY id, nome;
  ```

  ```SQL tab=
  SELECT   id, nome, COUNT(*) AS num_empregados
  FROM     Projeto, TrabalhaEm
  WHERE    id = projeto_id
  GROUP BY id, nome
  HAVING   COUNT(*) > 1;
  ```

* Para cada projeto, traga o número do projeto, o nome do projeto, e o número
  de empregados do departamento 5 que trabalham no projeto.

  ```SQL tab=
  SELECT
  ```

  ```SQL tab=
  SELECT   P.id, P.nome, COUNT(*) AS numero_empregados
  FROM     Projeto P, TrabalhaEm T, Empregado E
  WHERE    P.id = T.projeto_id AND E.id = T.empregado_id AND E.departamento_id = 4
  GROUP BY P.id;
  ```

## Referências

Elmasri R., Navathe S. B., Fundamentals of Database Systems, 7a edição, 2011.
