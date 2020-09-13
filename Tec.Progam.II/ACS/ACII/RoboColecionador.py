# -*- coding: utf-8 -*-
while True:
    BANDEIRAS    = 0;
    SENTIDOS     = ["N","L","S","O"];

    entrada      = str(input()).split(" "); #["10","10","20"]
    NLINHAS      = int(entrada[0]);
    NCOLUNAS     = int(entrada[1]);

    if (NLINHAS == 0):
        break;

    NINSTRUCOES  = int(entrada[2]);
    ROBO         = { "linha":0, "coluna":0 };

    TABULEIRO       = [0] * NLINHAS;
    listInstrucoes  = [0] * NINSTRUCOES;
    """
    # MOCKANDO PARA TESTAR
    TABULEIRO       = [ [".",".",".",".","*",".",".",".",".","."],
                        [".",".",".",".",".",".",".","*",".","."],
                        [".",".",".",".",".","*",".",".",".","."],
                        [".",".","*",".","#",".",".",".",".","."],
                        [".",".",".","#","N",".","*",".",".","*"],
                        [".",".",".","*",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".",".",".","."]
                    ];
    listInstrucoes  = ["F","D","F","F","F","F","F","F","E","E",
                    "F","F","F","F","F","F","E","F","D","F"];
    ROBO         = { "linha":4, "coluna":4 };
    """
    #MONTAR tabuleiro KKK vamo ver a confusao kkk

    # RETORNA N,S,L,O DEPENDENDO DO GIRO
    def operar(angulo,robo):
        countBandeira = 0;
        direcaoFinal = TABULEIRO[robo["linha"]][robo["coluna"]];
        sentido = SENTIDOS.index(direcaoFinal);
    #    print("DIREÇÃO ATUAL : %s" % direcaoFinal);
        # DIRECAO LESTE
        if angulo["direcao"] == SENTIDOS[1]:
            # Coloca  
    #        print("DIREÇÃO LESTE ! ")
    #        print("sentido NUMERICO: %s " % sentido);
            # Conserta se tiver fora do range
            index = ( sentido + angulo["angulo"] // 90 ) if (sentido + angulo["angulo"] // 90) < len(SENTIDOS) else 0;
            #direcaoFinal = SENTIDOS[ sentido + angulo["angulo"] // 90  ];
            direcaoFinal = SENTIDOS[ index ];
        # DIRECAO OESTE
        elif angulo["direcao"] == SENTIDOS[3]:
            #Coloca
    #        print("DIREÇÃO OESTE !")
            index = ( sentido + angulo["angulo"] // 90 ) if (sentido + angulo["angulo"] // 90) < len(SENTIDOS) else 0;
            #direcaoFinal = SENTIDOS[ sentido + angulo["angulo"] // 90 ]
            direcaoFinal = SENTIDOS[ index ];
        # MOVIMENTAR
        elif angulo["direcao"] == "AUTO":
            # Nao se esqueca de verificar pilastras!!!
            # NORTE
            if direcaoFinal == SENTIDOS[0]:
                
#              print("MOVIMENTAR PARA CIMA!");
                if (    (robo["linha"] - 1) > -1 
                    and 
                        TABULEIRO[robo["linha"] - 1][robo["coluna"]] != "#"
                    ):

                    TABULEIRO[ int(robo["linha"]) ][ int(robo["coluna"]) ] = ".";
                    if (TABULEIRO[robo["linha"] - 1][robo["coluna"]] == "*"):
                        countBandeira += 1;
                    TABULEIRO[robo["linha"] - 1][robo["coluna"]] = direcaoFinal;
                    robo = {"linha": robo["linha"] - 1 ,"coluna": robo["coluna"] };
#                else:
#                    print((robo["linha"] - 1));
#                    print("NORTE 70");
            # LESTE
            elif direcaoFinal == SENTIDOS[1]:
#                print("MOVIMENTAR PARA ESQUERDA!");
                if ( len(TABULEIRO[robo["linha"]])  > (robo["coluna"] + 1)
                    and 
                    TABULEIRO[robo["linha"]][robo["coluna"] + 1] != "#"
                    ):
                    TABULEIRO[ int(robo["linha"]) ][ int(robo["coluna"]) ] = ".";
                    # Verifica se passou da linha
                    if (len(TABULEIRO[robo["linha"]]) >= robo["coluna"] + 1):
                        if (TABULEIRO[robo["linha"]][robo["coluna"] + 1] == "*"):
                            countBandeira += 1;
                        TABULEIRO[robo["linha"]][robo["coluna"] + 1] = direcaoFinal;
                        robo = {"linha": robo["linha"] ,"coluna": robo["coluna"] + 1};
    #Não se esquecao de verificar se est ano ultimo quadro da ultima linha
                    elif(TABULEIRO[robo["linha"]+1][0] != "#"):
                        if (TABULEIRO[robo["linha"]][0] == "*"):
                            countBandeira += 1;
                        TABULEIRO[robo["linha"]][robo["coluna"] + 1] = direcaoFinal;
                        robo = {"linha": robo["linha"] ,"coluna": robo["coluna"] + 1};
#                else:
#                   print("LESTE 90");
            # SUL
            elif direcaoFinal == SENTIDOS[2]:
#                print("MOVIMENTAR PARA BAIXAR!");
                if ( (robo["linha"] + 1) < len(TABULEIRO)
                        and
                    TABULEIRO[robo["linha"] + 1][robo["coluna"]] != "#") :
                    TABULEIRO[ int(robo["linha"]) ][ int(robo["coluna"]) ] = ".";

                    if (TABULEIRO[robo["linha"] + 1][robo["coluna"]] == "*"):
                        countBandeira += 1;
                    TABULEIRO[robo["linha"] + 1][robo["coluna"]] = direcaoFinal;
                    robo = {"linha": robo["linha"] + 1 ,"coluna": robo["coluna"] };
#                else:
#                    print(" SUL 102 ")
            # OESTE
            elif direcaoFinal == SENTIDOS[3]:
    #            print("MOVIMENTAR PARA DIREITA!");
                if ( (robo["coluna"] - 1) >= 0
                        and
                      TABULEIRO[robo["linha"]][robo["coluna"] - 1] != "#"
                    ):
                    TABULEIRO[ int(robo["linha"]) ][ int(robo["coluna"]) ] = ".";

                    if (TABULEIRO[robo["linha"]][robo["coluna"] - 1] == "*"):
                        countBandeira += 1;
                    TABULEIRO[robo["linha"]][robo["coluna"] - 1] = direcaoFinal;
                    robo = {"linha": robo["linha"] ,"coluna": robo["coluna"] - 1};
            
        TABULEIRO[robo["linha"]][robo["coluna"]] = direcaoFinal;
        #return direcaoFinal;
        return {"count":countBandeira,"robo":robo};

    OPERACOES = {"D":{
                        "desc":"gire 90 graus para a direita",
                        "angulo":+90,
                        "direcao":"L"
                    },
                "E":{
                        "desc":"gire 90 graus para a esquerda",
                        "angulo":-90,
                        "direcao":"O"
                    },
                "F":{
                        "desc":"ande uma célula para a frente",
                        "angulo":0,
                        "direcao":"AUTO"
                    }
            };

    # Mockado para testar
    for linha in range(0,NLINHAS):
        TABULEIRO[linha] = ["."] * NCOLUNAS;
        conteudoDaLinha = str(input());
        for coluna in range(0,NCOLUNAS):
            # Tenta encontrar o robo
            if conteudoDaLinha[coluna] in SENTIDOS:
                ROBO =  { "linha":linha, "coluna":coluna };
            
            TABULEIRO[linha][coluna] = conteudoDaLinha[coluna];


    # Carrega as instruções 
    conteudoDaInstrucao = str(input());
    for instrucao in range(0, NINSTRUCOES):
        listInstrucoes[instrucao] = conteudoDaInstrucao[instrucao];

    """
    # debugger embrovisado
    modoMostrar = "";
    print("TABULEIRO ANTES:");
    for linha in range(0,NLINHAS):
        print(modoMostrar.join(TABULEIRO[linha]));
    print("ROBO:");
    print(ROBO);
    """

#    modoMostrar = "";
    # Executando Operacoes no ROBO
    for instrucao in listInstrucoes:
        #print("Tabuleiro ATUAL! Bandeiras: %s " % BANDEIRAS)
        #print(instrucao)
#        for linha in range(0,NLINHAS):
#            print(modoMostrar.join(TABULEIRO[linha]));
        #input();
        resultado = operar(OPERACOES[instrucao],ROBO);
        ROBO = resultado["robo"];
        BANDEIRAS += resultado["count"];
        #print("ROBO:");
        #print(ROBO);

    # D Test
    """
    print("RESULTADO DE IR PARA E: %s" % OPERACOES["D"]["desc"])
    print(operar(OPERACOES["D"],ROBO));
    print(operar(OPERACOES["D"],ROBO));
    print(operar(OPERACOES["D"],ROBO));
    print(operar(OPERACOES["D"],ROBO));
    """


    # E Tests
    """print("RESULTADO DE IR PARA E: %s" % OPERACOES["E"]["desc"])
    print(operar(OPERACOES["E"],ROBO));
    print(operar(OPERACOES["E"],ROBO));
    print(operar(OPERACOES["E"],ROBO));"""


#    modoMostrar = "";
#    print("TABULEIRO DEPOIS:");
#    for linha in range(0,NLINHAS):
#        print(modoMostrar.join(TABULEIRO[linha]));
    """
    print("INSTRUÇÕES:");
    print(listInstrucoes);

    print("ROBO:");
    print(ROBO);"""
    #print("BANDEIRAS: ")
    print(BANDEIRAS);