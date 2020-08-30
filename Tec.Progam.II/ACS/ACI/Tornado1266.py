TAMANHO_CERCA = 0;
listPostes = [];
N_Postes_Madeira = 0;

TAMANHO_CERCA = int(input());

while TAMANHO_CERCA > 0 :
    listPostes = str(input()).split(" ");
    for index in range(0,TAMANHO_CERCA):
        if index > 0 :
            if (int(listPostes[index]) == 0)  and (int(listPostes[index-1] )== 0):
                listPostes[index] = 1;
                N_Postes_Madeira += 1;
    print(N_Postes_Madeira);
    TAMANHO_CERCA = int(input());
    N_Postes_Madeira = 0;