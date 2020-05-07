def StringReverse(texto):
    alter = "";
    for index in range(0,len(texto),2):
        #print("index:",index)
        #print("letra:",texto[index])
        alter += texto[index];

    return alter;

lista = [8, 9, 10, 6, 5, 3, 8, 7, 8, 3, 8]

def ocorrencias(list, ocorencia):
    totalOcorrencias = 0;
    for item in list:
        if item == ocorencia:
            totalOcorrencias += 1;
    return totalOcorrencias;

print( StringReverse("Faculdade Impacta de Tecnologia") );
print( ocorrencias(lista, 8) );