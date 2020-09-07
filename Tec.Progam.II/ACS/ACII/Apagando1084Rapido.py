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
    
    # ordenação
    funcaoDeOrdenacao = lambda item: item["valor"];
    # Usando o recusro de sort da linguagem
    MapNumero.sort(key=funcaoDeOrdenacao);    
    # Removendo os algarismos eliminados
    MapNumero = MapNumero[TAMANHO_REMOVIDO:];
    # Usando o recusro de sort da linguagem para ordenar por index na palavra
    funcaoDeOrdenacao = lambda item: item["index"];
    MapNumero.sort(key=funcaoDeOrdenacao);
    teste = "";
    for item in range(0,TAMANHO_NUMERO - TAMANHO_REMOVIDO):
        teste += str(MapNumero[item]['valor']);
    # Apresentacao
    print(teste);