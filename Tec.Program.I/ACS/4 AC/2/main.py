# Escreva o codigo da funcao le_e_devolve_menor() na sequencia:
def le_e_devolve_menor():
    low = 0;
    while True:
        val = int(input());
        if val < 0 :
            break;
        elif low != 0:
            low = val if val < low else low;
        else:
            low = val;
    return low; 
# Escreva o codigo da funcao le_e_devolve_maior() na sequencia:
def le_e_devolve_maior():
    more = 0;
    while True:
        val = int(input());
        if val < 0 :
            break;
        else:
            more = val if val > more else more;
    return more; 

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo a partir deste ponto)
opcao = input()
if opcao == 'menor':
	menor = le_e_devolve_menor()
	print(menor)
elif opcao == 'maior':
	maior = le_e_devolve_maior()
	print(maior)