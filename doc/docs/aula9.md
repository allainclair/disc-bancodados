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

![gen-espec-mr](../images/mr/gen-espec-mr.png)

MR correspondente:

![mr-gen-espec](../images/mr/mr-gen-espec.png)

MR correspondente:

![mr-gen-espec2](../images/mr/mr-gen-espec2.png)


* Relações múltiplas – superclasse e subclasse

    * Qualquer tipo de especialização (total, parcial, exclusiva e compartilhada)‏.

* Relações múltiplas – somente relações de subclasses

    * Especialização total.

* Relação única com um atributo tipo

    * Especialização exclusiva.

* Relação única com o tipo atributos múltiplo

    * Atributo do tipo booleano indicando a qual classe a tupla pertence;

    * Especialização compartilhada.
