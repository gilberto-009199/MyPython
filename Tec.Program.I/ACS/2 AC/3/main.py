# -*- coding: utf-8 -*-

# O programa deve exibir o IMC arredondado em duas casas decimais,
# e em outra linha exibir um status dependendo do valor do IMC. Para arredondar em duas casas decimais,
# utilize a função round(imc, 2), onde imc é a variável que armazena o valor do IMC. 
altura  = float(input()); # Em m  recebido
peso    = float(input()); # Em Kg recebido
imc     = round(peso / (altura * altura),2);
state   = "";
if  imc < 17:

    state="Muito abaixo do peso \n";
#    "Queda de cabelo, infertilidade, ausencia menstrual "

elif imc < 18.5 : 
		
    state="Abaixo do peso \n";
#    "Fadiga, stress, ansiedade"
    
elif imc < 24.9 :
	
    state="Peso normal \n";
#	"Menor risco de doencas cardiacas e vasculares"
					
elif imc < 29.9 :
	
    state="Acima do peso \n";
#	"Fadiga, ma circulacao, varizes "
						
elif imc < 34.9 :
	state="Obesidade grau I \n";
#	"Diabetes, angina, infarto, aterosclerose "
							
elif imc < 40 :
	
    state="Obesidade grau II \n";
#	"Apneia do sono, falta de ar"
								
elif imc > 40 :
	state="Obesidade grau III \n";
#	"Refluxo, dificuldade para se mover, escaras,diabetes, infarto, AVC"

print(imc)
print(state)

"""
Leia os seguintes números:

Para calcular o IMC, utilize a seguinte fórmula: peso/(altura * altura)

-A altura da pessoa em metros (ponto flutuante)

-O pesso da pessoa em kg (ponto flutuante)

-Um número decimal (float) representando o IMC da pessoa.

-Uma string (das 7 possibilidades a seguir) representando o status da pessoa:
 Muito abaixo do peso, Abaixo do peso, Peso normal, Acima do peso, Obesidade grau I,
 Obesidade grau II, Obesidade grau III
"""
