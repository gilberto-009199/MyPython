

while True:
    n = int(input("Digite o numero }> "));

    sum = 0;

    for index in range(1, n + 1):
        sum += index / (n - ( index - 1) );

        print("              %0.0f     " % index)
        print("%0.1f = ---------------" % (index / (n -  (index - 1 )) ))
        print("            %0.0f - %0.0f " % ( n , index - 1));

    print("+")
    print("----")
    print("%0.1f" % sum);

    proceder = str(input("\n Deseja recomeçar?(S/N) }> ")).lower();
    if (proceder == "s" or proceder == "sim" or proceder == "si" or proceder == "y"):
        continue;
    else:
        print("Bye :)");
        exit();