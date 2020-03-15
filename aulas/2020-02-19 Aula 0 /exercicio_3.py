import math

print(" Programa que calcula a area de um circulo");

while True:

    raio =  float(input(" Digite o raio do circulo }> "));
    if (raio < 0) :
        print("Valor incompreensivel!");
    else:
        area = round((raio ** 2) * math.pi,3)
        print(" Area do circulo de raio ",raio," => ", area ,"")
    proceder = input("\n Deseja recomeçar?(S/N) }> ");
    if (proceder.lower() == "s" or proceder.lower() == "sim" or proceder.lower() == "si" or proceder.lower() == "y"):
        continue;
    else:
        print("Bye :)");
        exit();
