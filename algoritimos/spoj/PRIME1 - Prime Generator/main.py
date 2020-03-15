# Tente implementar o Teste de primalidade de Miller-Rabin
# Função que cuida do modulo para verificar se existe um valor divisivel
divisible = lambda val0, val1: val0 % val1 == 0;

def isPrimo( val0 ):
  if val0 == 1 : return True;

  for val1 in range( 2 , val0 ):
#    print(" Testando ",val0," com  ",val1);
#    print(" * " , val0 , " %  " , val1 , " =  ");
#   print(divisible(val0,val1));
    if divisible(val0,val1) :
#      print(" Resultado Divisivel por  ",val1);
      return False;
  return True;




while True:
  listVal = str(input()).split(" ");
#  num = int(input());
#  print(" ", num, " e PRIMO?  ")
#  print(isPrimo(num))
  if len(listVal) == 1 and isPrimo(int(listVal[0])) :
#    print(listVal[0]," é PRIMO? ",isPrimo(int(listVal[0])));
    print(listVal[0]);
    exit();
  for val0 in range(int(listVal[0]),int(listVal[len(listVal)-1])+1) :
#    print(" \n Testando : ",val0)
    if isPrimo(val0) :
#      print(val0," é primo !");
      if(val0 != 1):
        print(val0);
  exit();
