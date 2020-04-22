import math;

while True :
    


    #Validação  Da Promoção 
    val = float(input("Insira o valor da promocao }> "));
    if  0 > val  or val > 100:
        print("Não entendi %0.2f! Por favor digite denovo!" % val );
        continue;# Retoma o loop para pedir novamente o valor    
    promocao = val if 0 < val < 1 else  val / 100;

    print("Promoção  de %0.1f %% " % ( promocao * 100 ));

    #Validação  Do Produto
    produto = 0.0;
    while  produto <= 0:
        produto = float(input("Insira o valor do Produto }> "));
    
    novoValor = produto * (1 - promocao);

    print("O novo preço será %0.2f " % novoValor);




    proceder = str(input("\n Deseja recomeçar?(S/N) }> ")).lower();
    if (proceder == "s" or proceder == "sim" or proceder == "si" or proceder == "y"):
        continue;
    else:
        print("Bye :)");
        exit();