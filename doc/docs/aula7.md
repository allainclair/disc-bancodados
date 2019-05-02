## Aspecto temporal

Uma pessoa (empregado) só pode locar uma mesa por vez, e uma mesa só pode ser
locada por uma pessoa. Logo é uma relação de 1 para 1. Só que existe um aspecto
temporal, pois pessoas podem locar mesas em tempos diferentes, assim como
mesas são locadas em tempos diferentes para pessoas diferentes.

Como adicionar esse aspecto temporal?

![empregado-mesa](../images/empregado-mesa.png)

[empregado-mesa](../images/empregado-mesa-n-n.png)

### Empregado salário

![empregado-salario](../images/empregado-salario.png)

[empregado-salario-2](../images/empregado-salario-2.png)

Verificar essa abordagem para o [ER-Bebidas](../images/er-exerc-5-1.svg).

## Modelo Relacional

### Introdução

* Um banco de dados relacional é composto de **tabelas ou relações**. A
  terminolo gia tabela é mais comum nos produtos comerciais e na prática. Já
  a terminologia relação foi utilizada na literatura original sobre a abordagem
  relacional (daía denominação “relacional”);

* Este modelo é considerado o primeiro modelo de dados efetivamente usado em
  aplicações comerciais;

* Modelo usa o conceito de uma **relação matemática** como seu bloco de
  construção básica e tem sua base teórica na teoria dos conjuntos e na
  lógica de predicado de primeira ordem.

* Um banco de dados relacional consiste de uma coleção de relações (tabelas de
  valores) de nomes únicos.

* Tabela (relações)

    * Uma tabela é formada por um conjunto de colunas denominadas de
      atributos e por um conjunto de linhas denominadas de tuplas.

![tabela-mr](../images/tab-exemplo.png)


* Linhas (tuplas)

    * Cada tabela possui um conjunto de linhas que representa um
      relacionamento entre um conjunto de valores, um fato.

* Colunas (atributos)

    * Grau da relação.

* Domínios

    * Para cada atributo existe um conjunto de valores permitidos, chamado de
      domínio: inteiro, string, data, etc.


![tabela-mr](../images/tabela-mr.png)

### Chaves

O conceito básico para estabelecer relações entre linhas de tabelas de um
banco de dados relacional é o da **chave**. Em um banco de dados relacional, há
ao menos três tipos de chaves a considerar:

* Chave primária;
* Chave estrangeira;
* Chave alternativa.

### Chave primária

Uma chave primária é uma coluna ou uma combinação de colunas cujos valores
distinguem uma linha das demais dentro de uma tabela.

**Empregado:**

|**<u>CodigoEmp</u>**|Nome  |CodigoDepto|CategoriaFuncional|
|--------------------|------|-----------|------------------|
|**E5**              |Souza |D1         |C5                |
|**E3**              |Santos|D2         |C5                |
|**E1**              |Soares|D1         |C2                |
|**E2**              |Silva |D1         |-                 |

* Chave primária → **<u>CodigoEmp</u>** → chave primária **simples**;

* Apenas o **<u>CodigoEmp</u>** serve para identificar um empregado.


**Dependente:**

|**<u>CodigoEmp</u>**|**<u>NoDepen</u>**|Nome |Tipo  |DataNasc  |
|--------------------|------------------|-----|------|----------|
|**E1**              |**01**            |João |Filho |2000-01-01|
|**E1**              |**02**            |Maria|Esposa|1990-01-01|
|**E2**              |**01**            |Ana  |Esposa|1990-01-02|
|**E5**              |**01**            |Paula|Esposa|1990-01-03|
|**E5**              |**02**            |José |Filho |2000-01-01|

* Chave primária → **<u>CodigoEmp</u>**  e **<u>NoDepen</u>**→ chave primária
  **composta**;

* É necessário considerar ambos valores (**<u>CodigoEmp</u>**  e
  **<u>NoDepen</u>**) para identificar uma linha na tabela, ou seja para
  identificar um dependente.

### Chave estrangeira

CONTINUAR DAQUI

Uma chave estrangeira é uma coluna ou uma combinação de colunas, cujos
valores aparecem necessariamente na chave primária de uma tabela. A chave
estrangeira é o mecanismo que permite a **implementação de relacionamentos**
em um banco de dados relacional.

** Departamento: **

| **<u>CodigoDepto</u>** | NomeDepto  |
|------------------------|------------|
| **D1**                 | Compras    |
| **D2**                 | Engenharia |
| **D3**                 | Vendas     |

**Empregado:**

| <u>CodigoEmp</u> | Nome   | **CodigoDepto** | CategoriaFuncional |
|------------------|--------|-----------------|--------------------|
| E1               | Souza  | **D1**          | -                  |
| E2               | Santos | **D2**          | C5                 |
| E3               | Silva  | **D2**          | C5                 |
| E5               | Soares | **D1**          | C2                 |


A coluna **CodigoDepto** da tabela Empregado é uma chave estrangeira **em
relação a chave primária** da tabela Departamento.

* *Quando da inclusão de uma linha na tabela que contém a chave estrangeira*:
  neste caso, deve ser garantido que o valor da chave estrangeira apareça na
  coluna da chave primária referenciada. No exemplo, isso significa que um
  novo empregado deve atuar em um departamento já existente no banco de dados;

* *Quando da alteração do valor da chave estrangeira*: deve ser garantido que
  o novo valor de uma chave estrangeira apareça na coluna da chave primária
  referenciada;

* *Quando da exclusão de uma linha da tabela que contém a chave primária
  referenciada pela chave estrangeira*: deve ser garantido que na coluna chave
  estrangeira não apareça o valor da chave primária que está sendo excluída.
  Exemplo: isso significa que um departamento não pode ser excluído, caso nele
  ainda existirem empregados.

PARAMOS DAQUI

A palavra “estrangeira” usada para denominar este tipo de chave pode ser
enganosa. Ela pode levar a crer que a chave estrangeira sempre referencia uma
chave primária de outra tabela. Entretanto, esta restrição não existe. Uma
chave primária pode referenciar a chave primária da própria tabela.

**Empregado:**

| <u>CodigoEmp</u> | Nome   | CodigoDepto     | **CodigoEmpGerente** |
|------------------|--------|-----------------|----------------------|
| E5               | Souza  | D1              | **-**                |
| E3               | Santos | D2              | **E5**               |
| E2               | Silva  | D1              | **E5**               |
| E1               | Soares | D1              | **E1**               |


### Chave alternativa

Em alguns casos, mais de uma coluna ou combinações de colunas podem servir para
distinguir uma linha das demais. Uma das colunas (ou combinação de colunas) é
escolhida como chave primária. As demais colunas ou combinações são denominadas
*chaves alternativas*.

**Empregado:**

| <u>CodigoEmp</u> | Nome   | CodigoDepto     | **CPF**            |
|------------------|--------|-----------------|--------------------|
| E5               | Souza  | D1              | **019.585.222-20** |
| E3               | Santos | D2              | **019.585.223-21** |
| E2               | Silva  | D1              | **059.585.223-22** |
| E1               | Soares | D1              | **159.585.223-23** |

Quando especificamos que uma chave é primária, estamos especificando, além da
unicidade de valores, também o fato de esta coluna **ser usada nas chaves
estrangeiras** que referenciam a tabela em questão.

### Exemplo

![mr-esquema](../images/mr-esquema.png)
