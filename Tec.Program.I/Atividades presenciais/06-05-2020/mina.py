
while True:


  listAtividades = [];
  mediaGeral = 0;

  alunos = int(input("Digite quantos alunos serão registrados }> "));
    
 


  for index in range( 0, alunos ):
    
    nome    = str(input("\n Digite o nome   }> "));
    nota1   = float(input(" Digite a nota 1 }> "));
    nota2   = float(input(" Digite a nota 2 }> "));
    nota3   = float(input(" Digite a nota 3 }> "));
    nota4   = float(input(" Digite a nota 4 }> "));
    nota5   = float(input(" Digite a nota 5 }> "));
    
    listAtividades.append( [nome, nota1, nota2, nota3, nota4, nota5] );
    
  alunoMediaMaior = listAtividades[0];
  
  for aluno in listAtividades:
      print("Aluno:  %s"     % aluno[0]);
      print("Nota 1: %0.2f"  % aluno[1]);
      print("Nota 2: %0.2f"  % aluno[2]);
      print("Nota 3: %0.2f"  % aluno[3]);
      print("Nota 4: %0.2f"  % aluno[4]);
      print("Nota 5: %0.2f"  % aluno[5]);


      media      = (aluno[1] + aluno[2] + aluno[3] + aluno[4] + aluno[5]) / 5 ;
      mediaMaior = ( alunoMediaMaior[1] + alunoMediaMaior[2] + alunoMediaMaior[3] + alunoMediaMaior[4] + alunoMediaMaior[5]) / 5 ;
      if media > mediaMaior:
          alunoMediaMaior =  alunos;

      print( "Média: %0.2f \n" % media );
  
  
  mediaMaior = ( alunoMediaMaior[1] + alunoMediaMaior[2] + alunoMediaMaior[3] + alunoMediaMaior[4] + alunoMediaMaior[5]) / 5 ;
  print("O aluno %s possui a maior média:  %0.2f " % (  alunoMediaMaior[0], mediaMaior ));
  
  proceder = input("\n Deseja recomeçar?(S/N) }> ");
  if (proceder.lower() == "s" or proceder.lower() == "sim" or proceder.lower() == "si" or proceder.lower() == "y"):
    continue;
  else:
    print("Bye :)");
    exit();
    
