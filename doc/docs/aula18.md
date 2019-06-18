## Banco de dados de exemplo

* Empregado(<u>id</u>, pnome, unome, endereco, salario, sexo, data_nasc, *super_id*,
  *departamento_id*);

    * super_id: referencia o atributo **id** da própria tabela Empregado;

    * departamento_id: referencia o atributo **id** a tabela Departamento.

* Departamento(<u>id</u>, nome, gerente_data_inicio, *gerente_id*);

    * gerente_id: referencia o atributo **id** da tabela de Empregado;

    * nome é atributo único (chave alternativa).

* LocalDepartamento(<u>*departamento_id*, departamento_local</u>)

    * departamento_id: referencia o atributo **id** a tabela Departamento.

* Projeto(<u>id</u>, nome, *departamento_id*)

    * departamento_id: referencia o atributo **id** a tabela Departamento.

* TrabalhaEm(<u>*empregado_id, projeto_id*</u>, horas)

    * empregado_id: referencia o atributo **id** a tabela Empregado;

    * projeto_id: referencia o atributo **id** a tabela Projeto.

* Dependente(<u>*empregado_id*, nome</u>, data_dasc, relacao)

    * empregado_id: referencia o atributo **id** a tabela Empregado.

## Universidade (empresa_start.db)

### Inserir dados nas tabelas

* Inserir um novo empregado do departamento de fisica que trabalha em um novo
  projeto chamado de "Fisica para principiantes". Tem dois dependentes, um filho
  e uma filha.

* Inserir um novo projeto de Matematica em que todos os empregados do departamento
  de matematica participam.

### Declarações do SELECT em SQL

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


### Selecionar informacoes

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
