# ERRO 85% porcento
TAMVETOR = 51;

vetor = [0] * TAMVETOR;
vetor[0] = float(input()) * 1;

for index in range(1,TAMVETOR):
    vetor[index] = float(vetor[ index - 1 ]) * 2;


for index,item in enumerate(vetor):
        print("X[%d] = %s" % ( index , item ));