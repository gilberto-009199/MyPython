# -*- coding: utf-8 -*-
while True:
    BANDEIRAS    = 0;
    SENTIDOS     = ["N","L","S","O"];

    entrada      = str(input()).split(" ");
    NLINHAS      = int(entrada[0]);
    NCOLUNAS     = int(entrada[1]);

    if (NLINHAS == 0):
        break;

    NINSTRUCOES  = int(entrada[2]);
    ROBO         = { "linha":0, "coluna":0 };

    TABULEIRO       = [0] * NLINHAS;
    listInstrucoes  = [0] * NINSTRUCOES;
    def operar(angulo,robo):
        countBandeira = 0;
        direcaoFinal = TABULEIRO[robo["linha"]][robo["coluna"]];
        sentido = SENTIDOS.index(direcaoFinal);
    
        if angulo["direcao"] == SENTIDOS[1]:
            index = ( sentido + angulo["angulo"] // 90 ) if (sentido + angulo["angulo"] // 90) < len(SENTIDOS) else 0;
            direcaoFinal = SENTIDOS[ index ];
        elif angulo["direcao"] == SENTIDOS[3]:
            index = ( sentido + angulo["angulo"] // 90 ) if (sentido + angulo["angulo"] // 90) < len(SENTIDOS) else 0;
            direcaoFinal = SENTIDOS[ index ];
        elif angulo["direcao"] == "AUTO":
            if direcaoFinal == SENTIDOS[0]:
                if (    (robo["linha"] - 1) > -1 
                    and 
                        TABULEIRO[robo["linha"] - 1][robo["coluna"]] != "#"
                    ):

                    TABULEIRO[ int(robo["linha"]) ][ int(robo["coluna"]) ] = ".";
                    if (TABULEIRO[robo["linha"] - 1][robo["coluna"]] == "*"):
                        countBandeira += 1;
                    TABULEIRO[robo["linha"] - 1][robo["coluna"]] = direcaoFinal;
                    robo = {"linha": robo["linha"] - 1 ,"coluna": robo["coluna"] };
            # LESTE
            elif direcaoFinal == SENTIDOS[1]:
                if ( len(TABULEIRO[robo["linha"]])  > (robo["coluna"] + 1)
                    and 
                    TABULEIRO[robo["linha"]][robo["coluna"] + 1] != "#"
                    ):
                    TABULEIRO[ int(robo["linha"]) ][ int(robo["coluna"]) ] = ".";
                    if (len(TABULEIRO[robo["linha"]]) >= robo["coluna"] + 1):
                        if (TABULEIRO[robo["linha"]][robo["coluna"] + 1] == "*"):
                            countBandeira += 1;
                        TABULEIRO[robo["linha"]][robo["coluna"] + 1] = direcaoFinal;
                        robo = {"linha": robo["linha"] ,"coluna": robo["coluna"] + 1};
                    elif(TABULEIRO[robo["linha"]+1][0] != "#"):
                        if (TABULEIRO[robo["linha"]][0] == "*"):
                            countBandeira += 1;
                        TABULEIRO[robo["linha"]][robo["coluna"] + 1] = direcaoFinal;
                        robo = {"linha": robo["linha"] ,"coluna": robo["coluna"] + 1};
            # SUL
            elif direcaoFinal == SENTIDOS[2]:
                if ( (robo["linha"] + 1) < len(TABULEIRO)
                        and
                    TABULEIRO[robo["linha"] + 1][robo["coluna"]] != "#") :
                    TABULEIRO[ int(robo["linha"]) ][ int(robo["coluna"]) ] = ".";

                    if (TABULEIRO[robo["linha"] + 1][robo["coluna"]] == "*"):
                        countBandeira += 1;
                    TABULEIRO[robo["linha"] + 1][robo["coluna"]] = direcaoFinal;
                    robo = {"linha": robo["linha"] + 1 ,"coluna": robo["coluna"] };
            # OESTE
            elif direcaoFinal == SENTIDOS[3]:
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
    for instrucao in listInstrucoes:
        resultado = operar(OPERACOES[instrucao],ROBO);
        ROBO = resultado["robo"];
        BANDEIRAS += resultado["count"];
    print(BANDEIRAS);