Questão 1

select idcliente, nome, cpf, idcidade
from cliente;

Questão 2

select c.nome, v.parcelas
from venda v
join cliente c on v.idcliente = c.idcliente
where v.parcelas > 2;

Questão 3

select idproduto, descricao, estoque
from produto
where estoque < 50;

Questão 4

select c.nome, c.celular
from cliente c
join cidade ci on c.idcidade = ci.idcidade
where ci.nomecidade = 'maringá';

Questão 5

select c.nome as cliente, f.nomefuncionario as funcionario, v.datavenda
from venda v
join cliente c on v.idcliente = c.idcliente
join funcionario f on v.idfuncionario = f.idfuncionario
where v.datavenda = '2024-09-12';

Questão 6

select descricao, vrvenda
from produto
order by vrvenda desc;

Questão 7

update funcionario
set nomefuncionario = 'pedro silva'
where idfuncionario = 2;

Questão 8

update cidade
set nomecidade = 'nova londrina do sul'
where idcidade = 9;

Questão 9 

update bairro
set nomebairro = 'parque dos coqueiros ii'
where idbairro = 5;

Questão 10

update venda
set parcelas = 2
where datavenda = '2024-09-10';

Questão 11

delete from funcionario
where idfuncionario = 10;

Questão 12

delete from vendaitem
where idvenda in (select idvenda from venda where idcliente = 5);

delete from venda
where idcliente = 5;

