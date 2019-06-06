create table Empregado(
    id integer,
    nome varchar(100),
    sexo char,
    salario decimal(10, 2),
    super_id integer
);

insert into Empregado(id, nome, sexo, salario, super_id)
values      (1, 'Joao', 'm', 1000, 1);

select * from Empregado;

select nome, sexo from Empregado;