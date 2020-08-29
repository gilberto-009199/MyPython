TAMVETOR = 10;

vetor = [];

for index in range(0,TAMVETOR):
    tty = int(input());
    if tty < 1:
        tty = 1;
    
    vetor.append(tty);

for index,item in enumerate(vetor):
    print("X[%d] = %d" % ( index , item ));
    