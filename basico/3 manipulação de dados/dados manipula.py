"""""
manipulado tipos de dados

"""""

num_int=8
num_dec=8.7546
val_atr="oito e sete"

print(num_int)
print(num_dec)
print (val_atr)
#concatenar texto com numero
print( "o valor e:",num_int,"ta " )
#passando valor ja dentro
#(%+tipo da variavel)
print ("o valor e: %i"%num_int)
#%i= inteiro
#%f= decimal ponto flutuante
#%s =string texto
# nao se esqueca que o nome da variavel deve ter o % tambem
print ("o valor e: "+ str(num_int))
#str()=funcao que tranforma um valor em string texto
#""+str(num_int) * operador + usado para concatenar os dois texto

"""""
decimal e caracter
"""""

print ("decimal:",num_dec)
# ou
print ("decimal: %f"%num_dec)
#vc pode escolher ate quantos espacos depois da virgula
#seram apresentados
print ("decimal: %.2f"%num_dec)
#(%.2f)= 2 casas depois da virgula

""""
concateranar
para concatenar usamos o + ,mas
se os dados nao forem todos do tipo string entao
devemos convertelos
entao use sempre o stri() para a conversao
"""
print ("oi ",val_atr)
print ("oi "+val_atr)
# ou
print ("oi %s " %val_atr)
"""""
cocatenar 2 em uma so string

"""""
print ("int: %i double: %f string: %s"%(num_int,num_dec,val_atr))
