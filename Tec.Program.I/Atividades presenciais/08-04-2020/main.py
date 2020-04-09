"""
    'A vantagem de ter péssima memória é divertir-se muitas vezes com as mesmas coisas
    boas como se fosse a primeira vez.'
                                                                Friedrich Nietzsche
"""
# Exercicio 1
def somas_sucessivas(num1,num2):
    result = num1;
    while result != num1 * num2:
        result += num1;
    print(" %0.0f X %0.0f = %0.0f "%( num1, num2, result));
# Exercicio 2
def subtracoes_sucessivas(dividendo,divisor):
    resto       = dividendo;
    quociente   = 0;
    while resto != 0:
        #print(" Resto : ",resto)
        #print(" Quociente : ",quociente)
        if resto >= divisor : 
            #Divisão inteira aceita
            resto   = resto - divisor;
            quociente  += 1;
        else:
            #"Numero de resto não compativel"
            break;
    print(" %0.0f / %0.0f = %0.0f " % (dividendo,divisor,quociente));
    print(" RESTO : %0.0f " % resto);

#somas_sucessivas(5,10);
#subtracoes_sucessivas(37,5);
# Mesmo eu gostanto mais de java e javascript, isso aqui ficou bem bonitinho
while True :
    #Qual programa vc quer?
    print("Escolha o Exercicio:");
    print(" 1 - Somas Sucessivas");
    print(" 2 - Subtracoes Sucessivas");
    exercicio = str(input("Qual exercicio? (1/2) }>  "));

    # Alterando a referencia da função para uam variavel exec
    if exercicio == "1":
        exec = somas_sucessivas;
    elif exercicio == "2":
        exec = subtracoes_sucessivas;
    else:
        print("Não entendi!",exercicio);
        continue;
    
    num1 = int(input("Valor 1 }>"));
    num2 = int(input("Valor 2 }>"));

    exec(num1,num2);
    proceder = str(input("\n Deseja recomeçar?(S/N) }> ")).lower();
    if (proceder == "s" or proceder == "sim" or proceder == "si" or proceder == "y"):
        continue;
    else:
        print("Bye :)");
        exit();