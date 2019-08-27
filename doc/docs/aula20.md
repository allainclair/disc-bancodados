## SQL Selects na base de dados university.db

1 Selecione as colunas `(pnome, salario, sexo, data_dasc)` de todos empregados.

```SQL tab=

```

```SQL tab=
SELECT E.pnome, E.salario, E.sexo, E.data_nasc
FROM   Empregado E
```

1.1 Ordene por salário o `SELECT` anterior, do maior para o menor salário.

```SQL tab=

```

```SQL tab=
SELECT   E.pnome, E.salario, E.sexo, E.data_nasc
FROM     Empregado E
ORDER BY E.salario DESC
```

2 Retorne a média dos salarios de todos empregado.

```SQL tab=

```

```SQL tab=
SELECT AVG(E.salario)
FROM   Empregado E
```

2.1 Retorne a media dos salários apenas dos empregados que trabalham no
  departamento de identificador 2.
  
```SQL tab=

```

```SQL tab=
SELECT AVG(E.salario)
FROM   Empregado E
WHERE  E.departamento_id = 2
```

3 Selecione a média dos salários dos empregados que trabalham para o
  departamento de `Estatistica` ou `Matematica`. Use apenas os nomes para
  encontrar os departamentos.

```SQL tab=

```

```SQL tab=
SELECT AVG(E.salario)
FROM Departamento D, Empregado E
WHERE (D.nome = 'Matematica' OR D.nome = 'Estatistica') AND E.departamento_id = D.id
```

3.1 Seleciono o primeiro nome do empregado, nome do departamento e salário,
    a partir da *query* anterior. Ordene na ordem crescente pelo primeiro nome.

```SQL tab=

```

```SQL tab=
SELECT   E.pnome, D.nome, E.salario
FROM     Departamento D, Empregado E
WHERE    (D.nome = 'Matematica' OR D.nome = 'Estatistica') AND E.departamento_id = D.id
ORDER BY E.pnome
```

3.2 Conte a quantidade de empregados nos mesmos departamentos acima.

```SQL tab=

```

```SQL tab=
SELECT   COUNT(E.id)
FROM     Departamento D, Empregado E
WHERE    (D.nome = 'Matematica' OR D.nome = 'Estatistica') AND E.departamento_id = D.id
```

3.3 Some os salários desses empregados

```SQL tab=

```

```SQL tab=
SELECT   SUM(E.salario)
FROM     Departamento D, Empregado E
WHERE    (D.nome = 'Matematica' OR D.nome = 'Estatistica') AND E.departamento_id = D.id
```

4 Selecione os empregados que trabalham nos projetos do departamento de
  `Fisica` ou `Matematica`. Use apenas os nomes para encontrar os departamentos.
  Mostre o primeiro nome do empregado, nome do projeto, quantidade de horas do
  projeto e nome do departamento. Ordene pela quantidade de horas do empregado
  no projeto.
  
```SQL tab=

```

```SQL tab=
SELECT   E.pnome, P.nome, TE.horas, D.nome
FROM     Empregado E, Departamento D, Projeto P, TrabalhaEm TE 
WHERE    (D.nome = 'Matematica' OR D.nome = 'Fisica')
         AND E.departamento_id = D.id AND P.id = TE.projeto_id
         AND E.id = TE.empregado_id
ORDER BY TE.horas
```

5 Selecione os empregados que trabalham nos projetos do departamento de
  `Fisica` ou `Estatistica`. Também mostre os dependentes desses empregados.
  Além disso mostre os locais dos departamentos. Use apenas os nomes para
  encontrar os departamentos. Mostre o primeiro nome do empregado, nome do
  projeto, quantidade de horas do projeto, nome do departamento,
  local do departamento e dependente do empregado.

```SQL tab=

```

```SQL tab=
SELECT E.pnome, P.nome, TE.horas, D.nome, LD.departamento_local, DPE.nome
FROM   Empregado E, Departamento D, Projeto P, TrabalhaEm TE,
       LocalDepartamento LD, Dependente DPE
WHERE  (D.nome = 'Fisica' OR D.nome = 'Estatistica')
       AND E.departamento_id = D.id AND P.id = TE.projeto_id
       AND E.id = TE.empregado_id AND E.id = DPE.empregado_id
       AND D.id = LD.departamento_id
```

6 Para cada departamento, traga o número do deparatmento, o número de
  empregados no deparatmento e a média de salário.

```SQL tab=

```

```SQL tab=
SELECT   departamento_id, COUNT(*) AS num_empregados, AVG(salario)
FROM     Empregado
GROUP BY departamento_id
```

6.1 Traga também o nome do departamento e ordene pela quantidade de empregados
    por departamento na ordem descrescente.

```SQL tab=

```

```SQL tab=
SELECT   E.departamento_id, COUNT(*) AS num_empregados, AVG(E.salario), D.nome
FROM     Empregado E, Departamento D
WHERE    D.id = E.departamento_id
GROUP BY departamento_id
ORDER BY num_empregados DESC
```