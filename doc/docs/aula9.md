## Exemplo

![er-to-mr](../images/mr/er-to-mr.png)
[er-to-mr](../images/mr/er-to-mr.png)

![mr-from-er](../images/mr/mr-from-er.png)
[mr-from-er](../images/mr/mr-from-er.png)

## Tipos Relacionamento N-ário

* O relacionamento R é transformado em uma entidade E;

* A entidade E é ligada a cada uma das entidades que participavam do relacionamento
  original por meio de relacionamentos binários;

* Considerar as regras de implementação de entidades e relacionamentos binários
  apresentadas anteriormente.

![nario-to-binario](../images/mr/nario-to-binario.png)

Esquema Relacional correspondente:

* Produto(<u>CodProd</u>, Nome)‏;
* Cidade(<u>CodCid</u>, Nome)‏;
* Distribuidor(<u>CodDistr</u>, Nome)‏;
* Distribuição(<u>CodProd</u>, CodDistr, <u>CodCid</u>, DatedeInicio)‏;
* CodProd referencia Produto;
* CodDistr referencia Distribuidor;
* CodCid  referencia Cidade.

## Especialização ou Generalização

Considerando uma tabela por **hierarquia**, a tabela é composta por:

* Chave primária correspondente ao id da entidade mais genérica;
* Uma coluna Tipo para identificar a entidade especializada;
* Uma coluna para cada atributo da entidade genérica;
* Colunas referentes aos relacionamentos dos quais participa a entidade genérica,
  se necessário;
* Uma coluna para cada atributo de cada entidade especializada;
* Colunas referentes aos relacionamentos dos quais participa cada entidade
  especializada, se necessário.

Considerando uma tabela por **entidade especializada** temos:

* Criar uma tabela para cada entidade que compõe a hierarquia, aplicando as
  regras de implementação de entidades e relacionamentos apresentadas anteriormente;
* Uma coluna Tipo na tabela da superclasse;
* Acrescentar a chave primária da entidade genérica em cada nova tabela
  considerando também a chave primária desta.

![gen-espec-mr](../images/mr/gen-espec-mr.png)

MR correspondente:

![mr-gen-espec](../images/mr/mr-gen-espec.png)

MR correspondente:

![mr-gen-espec2](../images/mr/mr-gen-espec2.png)
