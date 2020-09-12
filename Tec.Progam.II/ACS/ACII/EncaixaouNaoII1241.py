# -*- coding: utf-8 -*-

NUMTEST = int(input());

def isContainFinal(palavra0, palavra1):
    # Verifica se o final e iqual 
    print(palavra0[-1*len(palavra1):]);
    return palavra0[-1*len(palavra1):] == palavra1;


while( NUMTEST > 0 ):

    entrada = str(input()).split(" ");

    if isContainFinal(entrada[0],entrada[1]) :
        print("encaixa");
    else:
        print("nao encaixa");

    NUMTEST -= 1;