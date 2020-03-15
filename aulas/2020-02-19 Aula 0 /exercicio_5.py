print(" Programa que calcula o salario mensal")

while True:

    valorHora =  float(input(" Digite o valor/hora }> "));
    if (valorHora < 0) :
        print(" Valor incompreensivel!!");
    else:
        horaMes = int(input(" Digite as horas trabalhadas por mes }> "));
        if(horaMes < 0):
            print("Valor incompreensivel!!");
        else:
            print(" Salario mensal : ",(valorHora * horaMes));
    proceder = input("\n Deseja recomeçar?(S/N) }> ");
    if (proceder.lower() == "s" or proceder.lower() == "sim" or proceder.lower() == "si" or proceder.lower() == "y"):
        continue;
    else:
        print("Bye :)");
        exit();
