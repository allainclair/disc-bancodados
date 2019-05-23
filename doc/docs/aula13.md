## Exercício 1

Modelar (ER-MR) uma compra do forncedor que tem "vários pedidos" de bebidas. Ou seja, uma
compra possui vários itens de  bebidas, assim como em um mercado temos vários itens
de compra.

### Primeiro passo

Modelar um pedido contendo apenas uma bebida e depois uma compra tendo vários pedidos.

![compra-pedido-fornecedor](../images/exerc/compra-pedido-fornecedor.svg)

* Bebida(<u>id</u>, volume, tipo, marca);

* Pedido(<u>id_compra, id_bebida</u>, **quantidade**);

* Compra(<u>id</u>, data, valor).

Como funciona na prática?

1. A compra foi feita e registrada na **Tabela Compra**;
2. Dado o **id da compra** é possível buscar todas as bebidas dessa compra
   devido ao da **id_compra** e **id_bebida** na **Tabela Pedido**.

### Segundo passo

Adicionar o Fornecedor no modelo.

![compra-pedido-fornecedor-1](../images/exerc/compra-pedido-fornecedor-1.svg)

* Bebida(<u>id</u>, volume, tipo, marca);

* Pedido(<u>id_compra, id_bebida</u>, quantidade);

* Compra(<u>id</u>, data, valor, **id_fornecedor**);

* Fornecedor(<u>id</u>, nome, região, ...).

## Exercício 2

![cliente-venda-bebida](../images/exerc/cliente-venda-bebida.svg)

* Bebida(<u>id</u>, volume, tipo, marca);

* Carrinho(<u>id_compra, id_bebida</u>, quantidade);

* Venda(<u>id</u>, data, valor, **id_cliente**);

* Cliente(<u>id</u>, p_nome, u_nome, nascimento, sexo).

![exerc-er-alternativa](../images/exerc/exerc-er-alternativa.svg)
[exerc-er-alternativa](../images/exerc/exerc-er-alternativa.svg)

![exerc-er-alternativa-1](../images/exerc/exerc-er-alternativa-1.svg)
[exerc-er-alternativa-1](../images/exerc/exerc-er-alternativa-1.svg)
