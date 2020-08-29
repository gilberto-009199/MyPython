# ERRO Exception line 8
TAMVETOR = 100;

vetor = [0] * TAMVETOR;

index = 0;
while index < TAMVETOR:
    tty = float(input());
    if tty < 10:
        vetor[index] = tty;
        index+=1;

for index,item in enumerate(vetor):
    print("X[%d] = %s" % ( index , item ));