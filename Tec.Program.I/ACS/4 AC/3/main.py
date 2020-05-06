# Escreva a funcao checa_quantidade_divisores(n, qtd) na sequencia:
divisible = lambda val0, val1: val0 % val1 == 0;

def checa_quantidade_divisores(n, qtd):
  flag = 0;
  for index in range( 1 , n + 1 ):
    if divisible(n,index):
      flag += 1;
  return flag == qtd;
# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
n = int(input())
qtd = int(input())
if checa_quantidade_divisores(n, qtd): # se a funcao devolve True, entao...
	print(n, "possui", qtd, "divisores")
else:
	print(n, "nao possui", qtd, "divisores")