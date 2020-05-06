# Implemente a funcao juros_simples(c, i, t) na sequencia:

def juros_simples(c, i, t):
    return c + (c * i * t);

# Implemente a funcao juros_compostos(c, i, t) na sequencia:
def juros_compostos(c,i,t):
   return c * (1 + i) ** t
# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo a partir deste ponto)
opcao = input()
capital = float(input())
taxa = float(input())
tempo = float(input())
if opcao == 'simples':
	montante_final = juros_simples(capital, taxa, tempo)
elif opcao == 'composto':
	montante_final = juros_compostos(capital, taxa, tempo)
print("{0:.2f}".format(montante_final))