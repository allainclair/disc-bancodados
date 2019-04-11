## 1.2 Uma aplicação de banco de dados chamado EMPRESA. 

A empresa está organizada em departamentos. Cada departamento tem um nome único,
um número único, pode ter diversas localizações e um empregado que gerencia o
departamento. Temos a data em que o empregado começou a gerenciar o departamento.
Nem todo empregado gerencia necessariamente um departamento, mas um departamento
deve ter um gerente. Um departamento pode controlar um número qualquer de 
projetos, cada qual com um único nome, um único número e uma única localização. 
Armazenamos o nome de cada empregado (Pnome + Unome), o número do seguro social,
endereço, salário, sexo e data de nascimento. Um empregado obrigatoriamente está
alocado a um departamento, mas pode trabalhar em diversos projetos que não são
controlados, necessariamente, pelo mesmo departamento. Um empregado deve participar
de um projeto e um projeto deve vincular empregados, obrigatoriamente. Controlamos o
número de horas semanais que um empregado trabalha em cada projeto. Também controlamos
o supervisor direto de cada empregado, quando isto acontece. Queremos ter o controle
dos dependentes de cada empregado para fins de seguro. Guardamos o primeiro nome,
sexo, data de nascimento de cada dependente, e o parentesco dele com o empregado.


Faça um DER para esse domínio.