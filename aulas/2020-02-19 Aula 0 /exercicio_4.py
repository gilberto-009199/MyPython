print(" Programa que calcula a area de um quadrado")

while True:

    lado =  int(input(" Digite o valor de um dos lados }> "));
    if(lado < 0):
        print("Valor incompreensivel!");
    else:
        print(" Quadrado ",lado,"X",lado," tem area ", lado ** 2 ," ");
        print(" O Dobro dessa area é  ", (lado ** 2) * 2 ," ");
    proceder = input("\n Deseja recomeçar?(S/N) }> ");
    if (proceder.lower() == "s" or proceder.lower() == "sim" or proceder.lower() == "si" or proceder.lower() == "y"):
        continue;
    else:
        print("Bye :)");
        exit();
