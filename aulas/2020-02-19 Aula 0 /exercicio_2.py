
print(" Programa que converte metros para milimetros")

while True:

    metros =  int(input(" Digite o seu valor em metros }> "));
    if(metros < 1):
        print("Valor incompreensivel!");
    else:
        print(" ",metros," metros => ", metros * 1000 ," milimetros")
    proceder = input("\n Deseja recomeçar?(S/N) }> ");
    if (proceder.lower() == "s" or proceder.lower() == "sim" or proceder.lower() == "si" or proceder.lower() == "y"):
        continue;
    else:
        print("Bye :)");
        exit();
