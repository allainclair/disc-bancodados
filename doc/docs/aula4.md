## Projeto de banco de dados

Duas fases:

* Modelagem conceitual;
* Projeto lógico.

### Modelagem idependente do SGDB

1. Levantamento e análise de requisitos
 
    Levantamento de requisitos é parte primeira no projeto do banco de dados
    que se for não for bem feito, pode levar facilmanente à ruína do sistema
    de banco de dados. Isso deve ser feito de forma iterativa, ou seja, o 
    projeto do banco é constante enquanto é pertinente. Deve ser feito 
    sempre que for necessário para o mesmo banco.
    
    A descrição deve ser concisa dos requisitos de dados para evitar 
    interpretações erradas.

    1.1 Requisitos funcionais;

    !!! example "Exemplo 4.1"
        Uma relatório de notas do alunos deve ser mostrado ao usuário do
        sistema junto com a disciplina e professor responsável pela 
        disciplina.
        ---
        Questões:
        
        * Quais notas? Todas as notas? Notas de prova e trabalhos?
        * Mostrar apenas nome do aluno, ou mostrar também seu RA?
    

    1.1 Requisitos de dados;
    
    !!! example "Exemplo 4.2"
        Cada professor pode ter mais do que uma disciplina, e uma disciplina
        pode ter até 3 professor;

        Papel do projetista perguntar e questionar esses tipso de requisitos 
        de dados.

2. Análise funcional

    2.1 Especificação de transação de alto nível.
    
    !!! example "Exemplo 4.3"
        O usuário do banco de dados deve "selecionar" as entidades professor, 
        aluno, disciplina e notas; relacionar essas entidades fazendo 
        "junções" delas para mostrar de forma tabular as notas dos alunos.
        

3. Projeto conceitual

    3.1 Modelo conceitutal: um diagrama (esquema) de entidade-relacionamento.
 
### Modelagem dependente do SGDB
 
1. Projeto lógico: esquema lógico → projeto físico;

2. Projeto do programa de aplicação → implementação das transações;

## Atributos do MER

Tipos de atributos que ocorrem no modelo ER

### Simples e Compostos

### Monovalorados e Multivalorados

**Monovalorados** assumem apenas um único valor para um entidade específica; 
já multivalorados podem assumir conjunto de valores para uma entidade.

Exemplos:

* A entidade empréstimo pode ter um atributo **código monovalorado**;
* A entidade empregado pode ter um atributo **nome-dependentes 
  multivalorado**: filhos (filho1, filho2, etc);
* A entidade cliente pode ter um atributo **endereço também multivalorado**:
  endereço = logradouro, número, bairro e CEP;
* A entidade professor pode ter um atributo email **multi ou mono** valorado?

O atributo multivalorado pode ter um limite superior ou/e inferior para o
número de ocorrências em um atributo multivalorado. Exemplos:



### Nulos

Um valor nulo é usado quando uma entidade não possui valor para determinado 
atributo.

Exemplo:

* Se o empregado não possui número da carteira de reservista, o valor nulo é
  atribuído a este atributo para esta entidade significando que o atributo 
  não é aplicável a ele;
  
* Valores desconhecidos podem ser representados por valores nulos significando,
  neste caso, a omissão da informação;
  
* Campos de cadastros **não obrigatórios** podem ser nulos: um campo 
  **telefone fixo** por exemplo.

### Armazenados e Derivados

O valor de um atributo pode ser derivado de outro:

* O atributo Idade (derivado) é calculado a partir do atributo
  data_nascimento (armazenado);

* O número de empréstimos de um cliente (atributo qtde_empréstimos) pode ser
  calculado a partir de uma pesquisa na entidade empréstimos de um banco;

* O valor do tempo de casa de um funcionário pode ser calculado a partir da 
  sua data de contratação.
  
Atributos derivados podem exigir "cálculo extra", diferente de pegar o 
dado já pronto do banco de dados, como exemplificados acima.

Exemplo:

```
quantidade_emprestimos = tamanho(emprestimos)
valor_emprestimos = soma(emprestimos)
quantidade_clientes = tamanho(clientes)
...
```

### Atributos Complexos

Atributos compostos e multivalorados podem ser aninhados de uma maneira 
arbitrária.

```
Endereco(
  EnderecoRua(Numero, Logradouro),
  Cidade, Estado, CEP, Apartamento))
```

![atrib-complexo](images/ex-atrib-complexo-endereco.svg)


### Atributos "enumerador" e "intervalos"

``` Enumerador tab=
Sexo = {Masculino, Feminino, Outro}

Atributo qualitativo.
```

``` Enumerador tab=
Renda = {Baixa, Média, Alta}

Atributo quantitativo discretizado.
Intervalo discreto (Alta > Média > Baixa)
```

``` Intervalo tab=
Altura = [0.3, 3.0]

Atributo com intervalo contínuo.
```

### Exemplo de entidades e atributos

Mundo real: um banco (simplificado)

* Entidades
    * (cliente, agência, conta, empréstimo)

* Esquemas (tipos entidades)
    ```
    cliente_esquema = (
      nome_cliente: string,
      seguro_social: string, 
      rua_cliente: string,
      cidade_cliente: string)
    ```
    
    ```
    conta_esquema = (numero_conta: integer, saldo: real)
    ```
    
    ```
    emprestime_esquema = (numero_emprestimo: integer, total: real) 
    ```
    
    ```
    agencia_esquema = (
      nome_agencia: string,
      cidade_agência: string,
      fundos: real)
    ```
    
### Atributos-chave de um tipo Entidade

* Uma restrição importante de um tipo entidade é a chave ou restrição de
  unicidade em atributos;
* Um tipo entidade tem, geralmente, um atributo cujos valores são distintos
  para cada uma das entidades do conjunto entidade;
* Esse atributo é chamado **atributo-chave**.

Exemplos:

* Departamento

    * <u>Nome</u>, <u>Número</u>, {Localizações}, Gerente, DataInícioGerência;

* Projeto

    * <u>Nome</u>, <u>Número</u>, Localização, DepartamentoControle;
    
* Empregado

    * Nome(Pnome ,Mnome ,Unome), <u>SSN</u>, Sexo, Endereço, Salário, 
      DataNascimento, Departamento, Supervisor, {TrabalhaEm(Projeto, Horas)};

* Dependente

    * <u>Empregado</u>, <u>NomeDependente</u>, Sexo, DataNascimento, 
    Parentesco.


### Notação de atributos

* **Atributo simples:** atributo_simples
    * ex: <u>Código</u>

* **Atributo composto:** atributo_composto(sub_atributo_1, ..., sub_atributo_n)
    * ex: Endereço(rua, número, logradouro)

* **Atributo multivalorado:** {atributo_multivalorado}
    * ex: {dependentes}
