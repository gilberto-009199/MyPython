def tabuada(n,modo):
    isMult = True if modo == 2 else False;
    print("TABUADA : ")
    for index in range(1,11):
        if isMult :
            print(" %0.2f  x %0.2f  = %0.2f"% ( n, index, n * index ) );
        else:
            print(" %0.2f  - %0.2f  = %0.2f"% ( n, index, n - index ) );

tabuada(5,1)

def isPrimo( val0 ):
  if val0 == 1 : return True;

  for val1 in range( 2 , val0 ):
#    print(" Testando ",val0," com  ",val1);
#    print(" * " , val0 , " %  " , val1 , " =  ");
#   print(divisible(val0,val1));
    if val0 % val1 == 0 :
#      print(" Resultado Divisivel por  ",val1);
      return False;
  return True;

while True :
    #Qual programa vc quer?
    print("Escolha o Exercicio:");
    print(" 1 - Tabuada");
    print(" 2 - Primo ?");
    exercicio = str(input("Qual exercicio? (1/2) }>  "));

    # Alterando a referencia da função para uam variavel exec
    if exercicio == "1":
        n    = int(input("Valor N }> "));
        modo = int(input("Valor Modo (1/2) }> "));
        tabuada(n,modo);
    elif exercicio == "2":
        val0 = int(input("Valor que será testado }> "));
        if isPrimo(val0) :
            print(" %0.0f é Primo! " % val0);
        else:
            print(" %0.0f não é Primo! " % val0);
    else:
        print("Não entendi!",exercicio);
        continue;

    
    proceder = str(input("\n Deseja recomeçar?(S/N) }> ")).lower();
    if (proceder == "s" or proceder == "sim" or proceder == "si" or proceder == "y"):
        continue;
    else:
        print("Bye :)");
        exit();