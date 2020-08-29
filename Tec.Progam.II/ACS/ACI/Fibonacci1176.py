# Aceito
testes = int(input());

def fib(val):
    if val  == 0:
        return 0;
    else:
        valorAnterior = 0;
        valorAtual = 1;
        for index in range(1,val):
            valorNovo = valorAtual + valorAnterior;
            valorAnterior =  valorAtual;
            valorAtual = valorNovo;
            #print("valorAnterior: %s, valorAtual: %s " % (valorAnterior,valorAtual));
        return valorAtual;



for idex in range(0,testes):
    val = int(input());
    print("Fib(%s) = %s" % ( val, fib(val) ))