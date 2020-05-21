

# copia de https://www.delftstack.com/pt/howto/python/how-to-check-if-a-file-exists-in-python/
def isExist(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

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


while True:
  
  
  ARQUIVO  = "db.csv";
  SEPARADOR = ":";
  NCOLS     =  6;
  ESQUEMA   = ["%s","%s","%s","%s","%s","%s"];

  listAtividades = [];

  if isExist(ARQUIVO):
      listAtividades = le_csv(ARQUIVO, SEPARADOR,NCOLS);
  else:
     print(" Criando arquivo %s.." % ARQUIVO );
     open(ARQUIVO,'x').close();
     print(" Arquivo %s montado!" % ARQUIVO );

  mediaGeral = 0;
  print("%s Alunos já foram registradas! " % len(listAtividades));
  alunos = int(input("Digite quantos alunos serão registrados }> "));
    

  for index in range( 0, alunos ):
    
    nome    = str(input("\n Digite o nome   }> "));
    nota1   = float(input(" Digite a nota 1 }> "));
    nota2   = float(input(" Digite a nota 2 }> "));
    nota3   = float(input(" Digite a nota 3 }> "));
    nota4   = float(input(" Digite a nota 4 }> "));
    nota5   = float(input(" Digite a nota 5 }> "));
    
    listAtividades.append( [nome, nota1, nota2, nota3, nota4, nota5] );
    
    grava_csv(ARQUIVO, 'a', [nome, nota1, nota2, nota3, nota4, nota5], ESQUEMA, SEPARADOR);

  
  alunoMediaMaior = listAtividades[0];
  
  for aluno in listAtividades:
      print("Aluno:  %s"     % str(aluno[0]));
      print("Nota 1: %0.2f"  % float(aluno[1]));
      print("Nota 2: %0.2f"  % float(aluno[2]));
      print("Nota 3: %0.2f"  % float(aluno[3]));
      print("Nota 4: %0.2f"  % float(aluno[4]));
      print("Nota 5: %0.2f"  % float(aluno[5]));


      media      = ( float(aluno[1]) + float(aluno[2]) + float(aluno[3]) + float(aluno[4]) + float(aluno[5]) ) / 5 ;
      mediaMaior = ( float(alunoMediaMaior[1]) + float(alunoMediaMaior[2]) + float(alunoMediaMaior[3]) + float(alunoMediaMaior[4]) + float(alunoMediaMaior[5]) ) / 5 ;
      if media > mediaMaior:
          alunoMediaMaior =  aluno;

      print( "Média: %0.2f \n" % media );
  
  
  mediaMaior = ( float(alunoMediaMaior[1]) + float(alunoMediaMaior[2]) + float(alunoMediaMaior[3]) + float(alunoMediaMaior[4]) + float(alunoMediaMaior[5]) ) / 5;
  print("O aluno %s possui a maior média:  %0.2f " % (  alunoMediaMaior[0], mediaMaior ));
  
  proceder = input("\n Deseja recomeçar?(S/N) }> ");
  if (proceder.lower() == "s" or proceder.lower() == "sim" or proceder.lower() == "si" or proceder.lower() == "y"):
    continue;
  else:
    print("Bye :)");
    exit();
    
