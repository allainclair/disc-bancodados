## Relacionamento ternário

Uma relação entre 3 entidades

![er-ternario](../images/er-ternario.png)

No caso de um relacionamento ternário, a cardinalidade refere-se a **pares de
entidades**. Em um relacionamento R entre três entidades A, B e C, a
cardinalidade máxima de A e B dentro de R indica quantas ocorrências de C
podem estar associadas a um par de ocorrências de A e B.

![er-ternario-card](../images/er-ternario-card.png)

O "1" na linha que liga o retângulo representativo da entidade Distribuidor
ao losango representativo do relacionamento expressa que cada par de
ocorrências (cidade, produto) está associado a no máximo um distribuidor.
Em outros termos, não há concorrência pela distribuição de um produto em uma
cidade.

Já os dois "n" expressam que:

* A um par (cidade, distribuidor) podem estar associados muitos
  produtos, ou em outros termos, um distribuidor pode distribuir em uma
  cidade muitos produtos;

* A um par (produto, distribuidor) podem estar associadas muitas
  cidades, ou em outros termos um distribuidor pode distribuir um
  produto em muitas cidades.

## Generalização / Especificação

Além de relacionamentos e atributos, propriedades podem ser atribuídas a
entidades através do conceito de generalização/especialização. Através deste
conceito é possível atribuir propriedades particulares a um subconjunto das
ocorrências (especializadas) de uma entidade genérica.

Nos relacionamentos de generalização e especialização as entidades de
nível inferior herdam os atributos e os relacionamentos das entidades de
nível superior.

![gen-espec-er](../images/gen-espec-er.png)

### Restrições Generalização/Especialização

* **Total:** CADA ocorrência da entidade genérica existe sempre uma
  ocorrência em uma das entidades especializadas.

    * Pode ser simbolizado por um "t".

* **Parcial:** NEM toda ocorrência da entidade genérica possui uma ocorrência
  correspondente em uma entidade especializada.

    * Pode ser simbolizado por um "p".

* **Exclusiva**: uma ocorrência de entidade genérica é especializada **no
  máximo uma vez**, nas folhas da árvore de generalização/especialização.

    * Pode ser simbolizado por um "x".

* **Compartilhada:** uma ocorrência de entidade genérica pode aparecer em
  várias entidades nas folhas da árvore de generalização/especialização.

    * Pode ser simbolizado por um "c".

## Entidade Associativa

* Limitação do modelo E-R: não é possível expressar relacionamento entre
  relacionamentos;

* Situação: suponha que cada par (médico, paciente) possua uma prescrição de
  medicamento.

![rel-rel-er-1](../images/rel-rel-er-1.png)

* Alternativa: fazer uso de entidade fraca.

![rel-rel-er-1](../images/rel-rel-er-2.png)

## Exercício de ER

* Uma empresa de bebidas quer automatizar algumas tarefas e processos;

* Bebidas tem tipos (whiskey, cerveja e suco primeiramente) e volume
  (mililitros). As bebidas também tem marca;

* O gerente do estabelecimento quer ver um relatório de vendas por período
  (dia, semana, mês e ano por exemplo) das bebidas de seu estabelecimento para
  saber se é preciso aumentar ou diminuir seu estoque nesses períodos
  apurados. O relatório deve conter bebidas agrupadas por tipo, quantidade
  vendida no período pertinente;

* O gerente da empresa quer cadastrar clientes que queiram ser cadastrados
  no sistema, para sugerir a eles produtos de acordo com o padrão de compra
  desses clientes. Um cliente tem um nome, data de nascimento, sexo,
  endereço. Logo, o gerente também quer relatórios de produtos que seus
  clientes consomem;

* Bebidas chegam ao estabelecimento por meio de fornecedores, os quais estão
  espalhados por vários lugares do Brasil. Logo o gerente quer relatórios de
  onde seus produtos estão sendo adquiridos. O gerente também quer saber quanto
  tempo leva em média de um determinado fornecedor para que um produto chegue
  a seu estabelecimento.


```Lógico tab=

```

```Lógico tab=
Bebida(id, tipo, volume, marca)

Venda(id, data)

Cliente(id, pnome, unome, nascimento, sexo)

Endereço(id, cep, complemento, número)

Fornecedor(id, nome)
```

### Entidades e atributos

* **Bebida**

    * tipo (simples, enumerado)

        * Ex: WHISKEY, SUCO ou CERVEJA.

    * volume (simples, inteiro)

        * Ex: 1000 ml.

    * marca (simples, string)

        * Ex: Coca-cola, Jack Daniels, Skol.

    * quantidade (derivado da quantidade de bebidas cadastradas, inteiro)

        * Ex: 50 bebidas cadastradas.

* **Venda** (entidade fraca)

    * período ? (derivado de data, inteiro)

        * Ex:

    * quantidade (derivado da quantidade de vendas, inteiro)

        * Ex: 100 vendas foram feitas no total.

    * data (simples, data)

        * Ex: data da venda: 2019-04-23 00:00:00.

    * valor (simples, decimal) (pode ser derivado)

        * Ex: R$ 100,00.

    * itens (multivalorado, "bebida")

        * Ex: bebida 1, bebida 2 e bebida 3 vendidas.

* **Cliente**

    * nome (composto)

        * Ex: (primeiro nome, string) (ultimo nome, string).

    * data de nascimento (simples, data)

        * Ex: data: 2000-04-23 00:00:00.

    * sexo (simples, enumerado)

        * Ex: MASCULINO, FEMININO, OUTRO.

    * endereço (composto)

        * Ex: (CEP, string) (cidade, string) (logradouro, string) (numero,
          inteiro).

* **Fornecedor**

    * nome (composto)

        * Ex: (primeiro nome, string) (ultimo nome, string).

    * endereço (composto)

        * Ex: (CEP, string) (cidade, string) (logradouro, string) (numero,
          inteiro).

    * região (simples, enumerado)

        * Ex: CENTRO-OESTE, SUL, SUDESTE, NORTE e NORDESTE.

    * prazo (derivado, inteiro)

        * Ex: 10 dias para entrega.

    * contato (composto)

        * Ex: (telefone fixo, string) (smartphone, string) (emails, strings).

* **Compra** (parecido com venda)

    * quantidade (derivado da quantidade de compras, inteiro)

        * Ex: 100 compras foram feitas no total.

    * data (simples, data)

        * Ex: data da venda: 2019-04-23 00:00:00.

    * preço (simples, decimal)

        * Ex: R$ 100,00

    * itens (multivalorado, "bebida")

        * Ex: bebida 1, bebida 2 e bebida 3 compradas.

* **Estoque**

    * quantidade (simples, inteiro)

        * Ex: 100 bebidas de uma entidade "bebida" no estoque para vender.


[er-exerc-5-1](../images/er-exerc-5-1.svg)
