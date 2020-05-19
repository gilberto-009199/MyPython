# Escreva a funcao interseccao(lista1, lista2) abaixo:
def interseccao(list0, list1):
    listInterseccao = [];

    listFormada0    = [];


    for item0 in list0:
        isGravado = False; # Verifica se o valor ja foi gravado;
        for item2 in listFormada0:
            if item2 == item0:
                isGravado = True;
        if not(isGravado) :
            listFormada0.append(item0);
#        else:
#             print(item0);
#             print(isGravado);
#             print("----------");

    for item0 in listFormada0:
        isOcorrencia = 0;

        for item2 in list1:
            if item2 == item0 : isOcorrencia +=1;

        if isOcorrencia > 0: listInterseccao.append(item0);

    
    return listInterseccao;


# Programa principal 

#[10, 11, 14, 20, 8, 2, 14, 3, 11]
#[1, 10, 9, 14, 20, 14]

#[1, 2, 3, 4, 5]
#[3, 4, 6]

# (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
lista1 = eval(input())
lista2 = eval(input())
resultado = interseccao(lista1, lista2)
if isinstance(resultado, list):
	print(resultado)
else:
	print("Erro. Voce deve devolver uma lista")