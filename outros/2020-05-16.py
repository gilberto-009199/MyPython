# Inverte um vetor
vectFrutas = 10 * ["Abacate"];
vectFrutas[0] = "Maçã";
vectFrutas[1] = "Limão";
vectFrutas[2] = "Tomate";
vectFrutas[3] = "Banana";
vectFrutas[4] = "Abacaxi";
vectFrutas[5] = "Mamão";
vectFrutas[6] = "Lichia";
vectFrutas[7] = "Laranja";
vectFrutas[8] = "Mechirica";
vectFrutas[9] = "Goiaba";
print(vectFrutas);

# INVERTE COM VETOR AUXILIAR
def inverse(vect,n):
    vectInverse = n * [0];
    for index in range( 1 , n + 1):
        vectInverse[ index - 1]  = vect[ n - index];
    return vectInverse;

print(inverse(vectFrutas,10));

#  TROCA SEM VETOR AUXILIAR
def troca(vect,i,j):
#   vect[i] , vect[j] = vect[j], vect[i];
    tmp = vect[i];
    vect[i] = vect[j];
    vect[j] = tmp;
    return vect;

print(troca(vectFrutas,0, 2));

#  INVERTE SEM VETOR AUXILIAR
def inverse2(vect, n):
    for index in range( 1 , (n // 2) + 1 ):
        print(index)
        troca(vect, index -1 , n - index );

inverse2(vectFrutas,10);
print( vectFrutas );