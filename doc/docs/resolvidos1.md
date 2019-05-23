## Diferentes modelos

![er-aluno-nota](images/er-aluno-nota.svg)

**Aluno:**

|RA   |Nome                           |
|-----|-------------------------------|
|63060|Allainclair Flausino dos Santos|
|63061|Yan Xurupita                   |
|63062|Roberto Carlos Hideki          |

**Nota:**

|Codigo|RA       |Valor |
|------|---------|------|
|**1** |**63060**|**10**|
|2     |63060    |10    |
|3     |63060    |10    |
|4     |63061    |9     |
|5     |63061    |8     |
|6     |63061    |7     |
|**7** |**63061**|**10**|
|8     |63062    |5     |
|9     |63062    |5     |
|10    |63062    |5     |
|**11**|**63062**|**10**|

![nota-grupo-aluno](images/nota-grupo-aluno.svg)

**Aluno:**

|RA   |Nome                           |
|-----|-------------------------------|
|63060|Allainclair Flausino dos Santos|
|63061|Yan Xurupita                   |
|63062|Roberto Carlos Hideki          |


**Grupo:**

|CodigoGrupo|
|-----------|
|1          |
|2          |
|3          |
|4          |

**Grupo Aluno:**

|CodigoGrupo|RA   |
|-----------|-----|
|1          |63060|
|1          |63061|
|1          |63062|
|2          |63060|
|3          |63061|
|4          |63062|
|5          |63062|
|5          |63061|

**Nota:**

|CodigoNota|CodigoGrupo|Valor |
|----------|-----------|------|
|**1**     |**1**      |**10**|
|2         |2          |10    |
|3         |2          |10    |
|4         |3          |9     |
|5         |3          |8     |
|6         |3          |7     |
|7         |4          |5     |
|8         |4          |5     |
|9         |4          |5     |

Diminuiu duas instâncias na tabela **Nota**.

## 1.8 versão 1

## Relações / Tabelas

### Similaridade

<u>CódigoTipoVeículo1</u>, <u>CódigoTipoVeículo2</u>

### Tipo de Veículo

<u>Código</u>, Nome, ArCondicionado, Tipo, NúmeroPortas, DireçãoHidráulica, CâmbioAutomático, Rádio, NúmeroDePassageiros, Leito, Sanitário

* NúmeroPortas, DireçãoHidráulica, CâmbioAutomático e Rádio são originais da entidade automóvel;

* NúmeroDePassageiros, Leito, Sanitário são originais da entidade ônibus.

### Veículo

<u>Número</u>, DataPróximaManutenção, Placa, CódigoTipoVeículo

* CódigoTipoVeículo é original da entidade Tipo de Veículo.

### Contrato Aluguel

<u>Número, NúmeroEscritório</u>, Data, Duração, NúmeroVeículo,  
NúmeroCarteiraMotorista

* NúmeroVeículo é original da entidade Veículo;
* NúmeroCarteiraMotorista é original da entidade Cliente;
* NúmeroEscritório é original da entidade Escritório.

### Escritório

<u>Número</u>, Local

### Cliente

<u>NúmeroCarteiraMotorista</u>, EstadoCarteiraMotorista, Nome, Endereço,
Telefone

## 1.8 versão 2

## Relações / Tabelas

### Similaridade

<u>CódigoTipoVeículo1</u>, <u>CódigoTipoVeículo2</u>

### Tipo de Veículo

<u>Código</u>, Nome, ArCondicionado, Tipo

### Automóvel

<u>CódigoTipoVeículo</u>, NúmeroPortas, DireçãoHidráulica, CâmbioAutomático, Rádio

* CódigoTipoVeículo é original da entidade Tipo de Veículo.

### Ônibus

<u>CódigoTipoVeículo</u>, NúmeroDePassageiros, Leito, Sanitário

* CódigoTipoVeículo é original da entidade Tipo de Veículo.

### Veículo

<u>Número</u>, DataPróximaManutenção, Placa, CódigoTipoVeículo

* CódigoTipoVeículo é original da entidade Tipo de Veículo.

### Contrato Aluguel

<u>Número, NúmeroEscritório</u>, Data, Duração, NúmeroVeículo,  
NúmeroCarteiraMotorista

* NúmeroVeículo é original da entidade Veículo;
* NúmeroCarteiraMotorista é original da entidade Cliente;
* NúmeroEscritório é original da entidade Escritório.

### Escritório

<u>Número</u>, Local

### Cliente

<u>NúmeroCarteiraMotorista</u>, EstadoCarteiraMotorista, Nome, Endereço,
Telefone

## 1.9

## Relações / Tabelas

### Fornecedor

<u>Id</u>, Região, Nome

### Email

<u>IdFornecedor, Texto</u>

* IdFornecedor é original da entidade Fornecedor.

### Telefone

<u>IdFornecedor, Número</u>

* IdFornecedor é original da entidade Fornecedor.
