# Escreva a funcao media_pares_impares(lista) abaixo:
def media_pares_impares(list):
    sumPar = 0;
    itemPar= 0;
    sumImP = 0;
    itemImP= 0;
    for item in list:
        if item % 2 == 0 :
            sumPar  += item;
            itemPar += 1;
        elif item > 0:
            sumImP  += item;
            itemImP += 1;
    print( (sumPar / itemPar ) );
    print( (sumImP / itemImP ) );
    

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
lista = eval(input())
media_pares_impares(lista)