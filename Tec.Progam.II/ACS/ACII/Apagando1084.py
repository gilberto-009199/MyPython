# -*- coding: utf-8 -*-
while True:
        
    TAMANHO_NUMERO_TAMANHO_REMOVIDO      = str(input()).split(" ");

    TAMANHO_NUMERO      = int(TAMANHO_NUMERO_TAMANHO_REMOVIDO[0]);
    TAMANHO_REMOVIDO    = int(TAMANHO_NUMERO_TAMANHO_REMOVIDO[1]);

    if TAMANHO_NUMERO < 1:
        break;

    NUMERO      =  str(input());

    if TAMANHO_REMOVIDO < 1:
        print(NUMERO);
        break;
    
    ListaOrdenadaDecrecente = [];
    MapNumero = [];
    for index in range(0,TAMANHO_NUMERO):
        MapNumero.append( { "index":index , "valor": int(NUMERO[index]) } );
    funcaoDeOrdenacao = lambda item: item["valor"];
    # Usando o recusro de sort da linguagem
    MapNumero.sort(key=funcaoDeOrdenacao);

    print(MapNumero[TAMANHO_REMOVIDO:]);
    # ordenação
    RESTO = [0] * (TAMANHO_NUMERO - TAMANHO_REMOVIDO);
    
    # Removendo os algarismos eliminados
    MapNumero = MapNumero[TAMANHO_REMOVIDO:];
    # Usando o recusro de sort da linguagem para ordenar por index na palavra
    funcaoDeOrdenacao = lambda item: item["index"];
    MapNumero.sort(key=funcaoDeOrdenacao);
    RESTO = [];
    for item in range(0,TAMANHO_NUMERO - TAMANHO_REMOVIDO):
        RESTO.append(MapNumero[item]);

    """for index, item in enumerate(MapNumero[TAMANHO_REMOVIDO:]):
        RESTO.insert(int(item['index']), item);"""
    print(RESTO);
    # APRESENTACAO
    RESULTADO = "";
    for item in RESTO:
        if item != 0:
            RESULTADO += str(item['valor']);
    print(RESULTADO);
    # SERÁ?
    # for algarismo in NUMERO:
    #    if algarismo 


    """
    for index in range(0,TAMANHO_NUMERO):
        MapNumero.append( { "index":index , "valor": int(NUMERO[index]) } );

    MAX = MapNumero[0];
    for item in MapNumero:
        if item["valor"] > MAX["valor"]:
            MAX = item;
    print(MAX);

    funcaoDeOrdenacao = lambda item: item["valor"];
    # Usando o recusro de sort da linguagem
    MapNumero.sort(reverse = True ,key=funcaoDeOrdenacao);
    RESTO = [];
    for item in range(0,TAMANHO_NUMERO - TAMANHO_REMOVIDO):
        RESTO.append(MapNumero[item]);
    print(MapNumero);
    print(RESTO);
    result = "";
    for item in RESTO:
        result += item["valor"];
    """