#arquivo = open('lista.txt','w'); 
# ou arquivo = open('lista.txt','a'); 
#arquivo.write("oi \n");
#arquivo.close();
#arquivo = open('lista.txt','r');
#print(arquivo.readline());


def grava_csv(nome, modo, dados, esquema, separador):
    mascara = separador.join(esquema) +"\n";
    with open( nome, modo) as arquivo:
        arquivo.write(mascara % ( (dados[0])  ,  (dados[1]),  (dados[2]), (dados[3]), (dados[4]), (dados[5]) ));
        arquivo.close()

def le_csv(nome, separador, nCols):
    listDados = [];
    with open( nome,'r') as arquivo:
        for line in arquivo:
            item = [];
            for colums in range(0,nCols):
#                print("Linha:")
#                print(line)
#                print(line.split(separador))
#                print(line.split(separador)[colums])
                item.insert(colums, line.split(separador)[colums].replace('\n',''));
            listDados.append(item);
        arquivo.close();
    return listDados;

ARQUIVO  = "db.csv";
SEPARADOR = ":";
NCOLS     =  6;
ESQUEMA   = ["%s","%s","%s","%s","%s","%s"];

nome    = str(input("\n Digite o nome   }> "));
nota1   = float(input(" Digite a nota 1 }> "));
nota2   = float(input(" Digite a nota 2 }> "));
nota3   = float(input(" Digite a nota 3 }> "));
nota4   = float(input(" Digite a nota 4 }> "));
nota5   = float(input(" Digite a nota 5 }> "));


grava_csv(ARQUIVO, 'a', [nome, nota1, nota2, nota3, nota4, nota5], ESQUEMA, SEPARADOR);


print(le_csv(ARQUIVO, SEPARADOR,NCOLS));
