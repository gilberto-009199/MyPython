# ERRO Exception line 9
TAMVETOR = 20;

vetor = [0] * TAMVETOR;

index = 1;

while index < TAMVETOR:
    tty = int(input());
    if tty < 10:
        vetor[ (TAMVETOR)  - index]  = tty;
        index+=1;

for index,item in enumerate(vetor):
    print("X[%d] = %s" % ( index , item ));