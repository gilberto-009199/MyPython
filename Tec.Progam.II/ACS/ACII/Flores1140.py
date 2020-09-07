import re;
while True:
    texto = str(input());
    if texto == "*":
        break;
    else:
        listPalavra  = re.findall( "[a-zA-Z0-9@\\çã-ũÃ-Ũá-źÁ-Ź%#$&*\(\)!\"\{\}]+", texto.lower() );
        letraInicial = listPalavra[0][0].lower();
        msg = "Y";
        for item in listPalavra:
            if (item[0] != letraInicial):
                msg = "N";
        
        print( msg if (len(listPalavra) > 1) else "N" );

        
