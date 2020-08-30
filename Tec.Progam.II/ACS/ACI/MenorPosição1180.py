TOTAL =  int(input());
listVal = str(input()).split(" ");

menorVal = {"valor":listVal[0],"index":0};
for index in range(0,TOTAL):
    if menorVal["valor"] > listVal[index];
       menorVal["valor"] = listVal[index];
       menorVal["index"] = index;
    
print("Menor valor: %s" % menorVal["valor"]);
print("Posicao: %s" % menorVal["index"]);
       