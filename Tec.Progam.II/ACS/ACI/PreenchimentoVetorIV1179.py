vetorPar = [];
vetorImp = [];

MAX_INPUTS = 15;
def mostrarVetor(prefix,vetor):
    for index,item in enumerate(vetor):
        print((prefix+"[%s] = %s") % ( index, item ) );

def isPar(valor):
    return ( valor % 2 ) == 0;

for index in range(0,MAX_INPUTS):
    valor = int(input());

    if isPar(valor):
        vetorPar.append(valor);
    else:
        vetorImp.append(valor);

    if len(vetorPar) == 5 :
        mostrarVetor("par",vetorPar);
        vetorPar = [];
    if len(vetorImp) == 5 :
        mostrarVetor("impar",vetorImp);
        vetorImp = [];

if len(vetorImp) > 0 :
    mostrarVetor("impar",vetorImp);
    vetorImp = [];
if len(vetorPar) > 0 :
    mostrarVetor("par",vetorPar);
    vetorPar = [];



