
DIAS = 7

diasCompridos = 0;
media = 0;

for index in range(0, DIAS):
    cartas = int(input());
    media += cartas;
    if cartas >= 100 :
        diasCompridos += 1;

print( diasCompridos );
print( "%0.0f" % (media / DIAS) );

