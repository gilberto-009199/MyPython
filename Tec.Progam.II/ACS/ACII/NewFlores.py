# -*- coding: utf-8 -*-

def listPalavras(linha):
    lista = [];
    palavraTemporaria = "";
    for index, letra in enumerate(linha.lower()):
        if  (letra == " " or letra == "  " or letra == "\t") and index > 0 :
            lista.append(palavraTemporaria);
            palavraTemporaria = "";
        elif letra != " " and letra != "\t":
            palavraTemporaria += letra;
    if len(palavraTemporaria) > 0:
        lista.append(palavraTemporaria);
    return lista;

while True:
    texto = str(input());
    if texto == "*":
        break;
    else:
        print(listPalavras(texto));
        ListaPalavras = listPalavras(texto);

        letraInicial = ListaPalavras[0][0].lower();
        
        msg = "Y";
        for item in ListaPalavras:
            if (item[0] != letraInicial):
                msg = "N";

        print( msg if (len(ListaPalavras) > 1) else "N" );
        
        """listPalavra  = re.findall( "", texto.lower() );
        letraInicial = listPalavra[0][0].lower();
        msg = "Y";
        for item in listPalavra:
            if (item[0] != letraInicial):
                msg = "N";

        print( msg if (len(listPalavra) > 1) else "N" );"""