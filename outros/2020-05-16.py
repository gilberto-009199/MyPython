vectFrutas = 10 * ["Abacate"];
vectFrutas[0] = "Mação";
vectFrutas[1] = "Limão";
vectFrutas[2] = "Tomate";
vectFrutas[3] = "Banana";
vectFrutas[4] = "Abacaxi";
vectFrutas[5] = "Mamão";
vectFrutas[6] = "Lichia";
vectFrutas[7] = "Laranja";
vectFrutas[8] = "Mechirica";
vectFrutas[9] = "Goiaba";

def inverse(vect,n):
    vectInverse = n * [0];
    for index in range( 1 , n + 1):
        print(n - index);
        vectInverse[ index - 1]  = vect[ n - index];
    return vectInverse;

print(inverse(vectFrutas,10));