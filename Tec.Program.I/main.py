"""lista = ['roteador','switch','modem','servidor','firewall'];
lista.append('transceiver')
del lista[3];
lista.insert(1, 'gbic');
print(lista[0])
print(lista[2])
print(lista[5])"""
x = 89;
y = 10;
a = x % y;
b = x / y;
print(a, 'e', b);
"""n = 75;
for i in range(60,71):
    resultado = n - i;
    print(n,'-',i, '=', resultado)"""

"""matriz = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16] ];
qtd_lin = len(matriz);
qtd_col = len(matriz[0]);
lista = [];
for i in range(qtd_lin):
    for j in range(qtd_col):
        if ( i  % 2 == 0) and ( j % 2 ) == 1:
           lista.append(matriz[i][j]) ;
print(lista);"""
"""
a = 2
b = 3
c = 1
d = 4

e = a + c;
f = (e*b) * d
print(f)
"""
"""
distancia = float(input());
#Muito Longe
#Muito próximo
#Distancia moderada
#Próximo
#Longe

if ( distancia > 24 ):
    print('Muito LONGE')
elif distancia > 20:
    print('longe');
elif distancia > 9:
    print('Distancia Moderada')
elif distancia > 5:
    print("proximo");
else:
    print("Muito Proximo")

"""

"""
media_provas = 6.0
media_trabalhos = 7
qtd_faltas = 10
if (media_provas > 6) and (media_trabalhos >= 7) and (qtd_faltas <= 10):
    print('Aluno aprovado!');
else:
    print('Aluno reprovado!');
"""
"""
(salario_bruto >= 2550 )
(tempo_relacionamento < 2 anos)
(tempo_relacionamento  >= 2 anos)  and  (tempo_relacionamento < 5 anos)
"""
"""
i = 100
m = 60
while i > m :
    print(i)
    i = i - 4;"""