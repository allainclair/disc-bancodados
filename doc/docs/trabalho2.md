* Desenvolver sistema computacional usando banco de dados;

* Usar banco de dados SQLite: `university/db/university.db`;
* Python versão 3;

## Funcionalidades

* **Entrada** significa um `input()`;

* **Saída** significa um retorno de função ou print(). Pode-se usar um `print()`
  para indicar que a operação foi feita com sucesso, ou o contrário em caso negativo;
  
* **Entradas** opcionais são campos em "branco" (string vazia), por exemplo quando
  é dado enter no terminal.

### Inserir

* **Entrada 1**: Opção 1

* **Saída**: *Print* do menu de inserção

#### Departamento

* **Entrada 1:** Opção 1.1

* **Entrada 2:** nome, gerente_data_inicio (opcional), gerente_id (opcional)

* **Saída:** `True` se inserido `False` caso contrário

É necessário checar os campos da **Entrada 2** no banco de dados para
retornar `True` ou `False`. Por exemplo: checar se o id do gerente existe no banco.

#### Dependente

* **Entrada 1:** Opção 1.2

* **Entrada 2:** empregado_id, nome, data_nasc, relacao

* **Saída:** `True` se inserido `False` caso contrário

É necessário checar os campos da **Entrada 2** no banco de dados para
retornar `True` ou `False`. Por exemplo: checar se o id do empregado existe no banco.

#### Empregado

* **Entrada 1:** Opção 1.3

* **Entrada 2:** pnome, unome, endereco, salario, sexo, data_nasc, supder_id (opcional), departamento_id

* **Saída:** `True` se inserido `False` caso contrário

É necessário checar os campos da **Entrada 2** no banco de dados para
retornar `True` ou `False`. Por exemplo: checar se o id do supervisor e id do
departamento existem no banco.

#### LocalDepartamento

* **Entrada 1:** Opção 1.4

* **Entrada 2:** departamento_id, departamento_local

* **Saída:** `True` se inserido `False` caso contrário

É necessário checar os campos da **Entrada 2** no banco de dados para
retornar `True` ou `False`. Por exemplo: checar se o id do departamento existe no banco.

#### Projeto

* **Entrada 1:** Opção 1.5

* **Entrada 2:** nome, departamento_id

* **Saída:** `True` se inserido `False` caso contrário

É necessário checar os campos da **Entrada 2** no banco de dados para
retornar `True` ou `False`. Por exemplo: checar se o id do departamento existe no banco.

#### TrabalhaEm

* **Entrada 1:** Opção 1.6

* **Entrada 2:** empregado_id, projeto_id, horas

* **Saída:** `True` se inserido `False` caso contrário

É necessário checar os campos da **Entrada 2** no banco de dados para
retornar `True` ou `False`. Por exemplo: checar se o id do projeto e empregado
existem no banco.

### Atualizar

* **Entrada 1**: Opção 2

* **Saída**: *Print* do menu de atualização

Cada tabela tem uma chave primária (que pode ser composta). Logo deve ser feita
uma busca por chave primária e atualizar uma instância da tabela.

Todos requisitos do item [Inserir](#inserir) devem ser feitos e satisfazer as
mesmas condições.

### Excluir por chave primária

* **Entrada 1**: Opção 3

* **Saída**: *Print* do menu de exclusão

Cada tabela tem uma chave primária (que pode ser composta). Logo deve ser feita
uma busca por chave primária e excluir uma instância da tabela. 

Instâncias (linhas) de todas as tabelas do item [Inserir](#inserir) devem ter
opção de exclusão por chave primária e essa chave primária deve ser checada se 
ela existe no banco.

## Envio do trabalho

* Enviar para **afsantos2@uem.br** com título (assunto): **BD 4573 T2 - Nome1 RA1 - Nome2 RA2**;

* Até 4 membros;
