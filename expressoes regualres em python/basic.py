import re;

texto = " Numeros 123456789";

resposta = re.search("([1-3])+[0-9]*([7-9])+", texto);


if resposta is not None :
    print( resposta.group() );
else:
    print("Padrão não encontrado");