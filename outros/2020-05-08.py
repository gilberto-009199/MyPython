# Exercicio 4  Apostila Pg. 17

divisible = lambda val0, val1: val0 % val1 == 0;

def isPrimo( val0 ):
  if val0 == 1 : return True;

  for val1 in range( 2 , val0 ):
    if divisible(val0,val1) :
      return False;
  return True;


while True:
  val0 = int(input());
  val1 = int(input());

  #soma dos numeros primos entre os valores 
  sum = 0;

  if isPrimo(int(val0)) :
    print(val0);
  for valor in range( val0, val1 +1 ):

    if isPrimo(valor) :
      if(valor != 1):
        #print(valor);
        sum += valor;
  
  print(sum);
  exit();