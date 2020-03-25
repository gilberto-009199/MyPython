# Gilberto Ramos de Oliveira 1903991
# -*- coding: utf-8 -*-

PESSOAS = 5;

def genPositive(val):
    if val < 0 :
        return val * -1;
    else:
        return val;

#Lista com as pessoas
listPessoas = [];
soma        = 0;
mult        = 1;
#loop para pegar cada uma dos individuos
for index in range(0,PESSOAS):
    nome    = str(input());
    idade   = genPositive(float(input()) );
    idade   = int(idade);
    listPessoas.append({"nome":nome,"idade":idade});
    soma += idade;
    mult *= idade;

for pessoa in listPessoas:
    print("Pessoa: %s , %i" % (pessoa["nome"] , pessoa["idade"]));
print( (soma) );
print( soma / 5 );
# sqrt de 2 para 2  == 2 ^ (1/2)
# sqrt de 3 para 2  == 3 ^ (1/2)
# sqrt de 100 para 3  == 3 ^ (1/3)
# raiz de 2 por 2 = 2 ^ ( 1 / 2 ) 
print( int(mult ** ( 1 / PESSOAS )));