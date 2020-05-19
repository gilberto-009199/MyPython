
# Escreva a funcao todos_os_indices(seq, x) abaixo:
def todos_os_indices(sequencia, valor):
    listOcorrencia = [];
    for i in range(0,len(sequencia)):
        if sequencia[i] == valor:
            listOcorrencia.append(i);
    return listOcorrencia;


# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
sequencia = eval(input())
valor = eval(input())
resultado = todos_os_indices(sequencia, valor)
if isinstance(resultado, list):
	if len(resultado) > 0:
		for item in resultado:
			print(item)
	else:
		print('lista vazia')
else:
	print('Erro. Voce deve devolver uma lista')