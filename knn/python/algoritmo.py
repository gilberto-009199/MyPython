import math;
# Verifica se o arquivo existe
# copia de https://www.delftstack.com/pt/howto/python/how-to-check-if-a-file-exists-in-python/
def isExist(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def le_arquivo(nome):
    # Lista com os dados pegos linha por linha
    listDados = [];
    # Abre o arquivo para leitura 'r'
    with open( nome,'r') as arquivo:
        # Le o arquivo linah por linha
        for line in arquivo:
            # Corta o texto da linha para pegar cada dado
            carne_vermelha  = float(line[4:9]);
            carne_branca    = float(line[13:18]);
            massa           = float(line[22:27]);
            fruta           = float(line[31:36]);
            vegetais        = float(line[40:45]);
            nascionalidade  = line[50:57];
            # Monta o Cliente e adiciona na lista 
            listDados.append({  'carnes_vermelhas':carne_vermelha,
                                'carnes_brancas':carne_branca,
                                'massas':massa,
                                'frutas':fruta,
                                'vegetais':vegetais,
                                'nascionalidade':nascionalidade
                             });
        # Fecha o arquivo aberto
        arquivo.close();
    # Retorna as informação guardadas na lista
    return listDados;

# Função que retorna a distancia euclidiana de 2 clientes
def getEuclidiana( cliente0 , cliente1 ):
  """
      Distância euclidiana é a raiz quadrada da soma das
     diferenças dos valores dos atributos elevado ao quadrado
  """
  soma =  (cliente0['carnes_vermelhas'] - cliente1['carnes_vermelhas'])**2
  soma += (cliente0['carnes_brancas'] - cliente1['carnes_brancas'])**2
  soma += (cliente0['massas'] - cliente1['massas'] )** 2
  soma += (cliente0['frutas'] - cliente1['frutas'] )** 2
  soma += (cliente0['vegetais'] - cliente1['vegetais'] )** 2

  return math.sqrt(soma); # ou soma ** (1/2);



# Fluxo principal

listClassificados   = le_arquivo('mediaPorNasci.knn.algoritmo.txt');
listNaoClassificados = le_arquivo('comandas.knn.algoritmo.txt');
qtdAmericanos = 0;
qtdEspanhol = 0;
qtdFrances = 0;
qtdBrasileiro = 0;
for clienteNaoIdentificado in listNaoClassificados:
    # Codigo para comparar e determinar a classe mais proxima
    # Lista que ira ordenarar os clientes mais proximos dele 
    listIndexadaPelaDistancia = [];
    for pessoaIdentificada in listClassificados:
        # Codigo que vai comparar o
        # ClienteNãoIdentificado com
        # cada um dos pessoaIdentificada no estudo 
        distancia = getEuclidiana(clienteNaoIdentificado,pessoaIdentificada);
        # Colocando na lista de ordenacao
        listIndexadaPelaDistancia.append({
                                            'distancia':distancia,
                                            'nascionalidade': pessoaIdentificada['nascionalidade']
                                         });
    # Hora de ordenar pelos com menor
    # distancia
    funcaoDeOrdenacao = lambda clienteIndexado: clienteIndexado['distancia'];
    # Usando o recusro de sort da linguagem
    listIndexadaPelaDistancia.sort(key=funcaoDeOrdenacao)

    # Bem agora sabemos sabemos a distancia
    # e temos a distancia ordenando a lista
    # precisamos decidir oque é proximo
    # ao sejá o quanto distante a um inividuo
    # pode estar do individuo não  classificado
    # para ser considerado uma referencia na 
    # identificação o chamado " K " desse algoritmo
    K = 7;
    # Escolhi 7, mas na minha opniao seria melhor
    # pegar uma porcentagem dos classificados como 30% algo assim,
    # quem sabe , afinal eu não sou um experti em algoritmos de 
    # aprendizado supervisionado de maguina
    isAmerica = 0;
    isFrances = 0;
    isEspanho = 0;
    isBrasile = 0;
    for i in listIndexadaPelaDistancia[:K]:
        print(i);
        if i['nascionalidade'] == "America":
            isAmerica += 1;
        elif i['nascionalidade'] == "Espanho":
            isEspanho += 1;
        elif i['nascionalidade'] == "Frances":
            isFrances += 1;
        elif i['nascionalidade'] == "Brasile":
            isBrasile += 1;
        else:
            print("Categoria não identificada")
    categoriaDefinida = "Indefinida...";
    if isAmerica > isEspanho and isAmerica > isFrances and isAmerica > isBrasile:
        categoriaDefinida = "America";
        qtdAmericanos += 1;
    elif isEspanho > isAmerica and isEspanho > isFrances and isEspanho > isBrasile:
        categoriaDefinida = "Espanho";
        qtdEspanhol += 1;
    elif isFrances > isAmerica and isFrances > isEspanho and isFrances > isBrasile:
        categoriaDefinida = "Frances";
        qtdFrances += 1;
    elif isBrasile > isAmerica and isBrasile > isEspanho and isBrasile > isFrances:
        categoriaDefinida = "Brasile";
        qtdBrasileiro += 1;
    
    print("Categoria Definida   : %s " % categoriaDefinida)
    print("Categoria Verdadeira : %s " % clienteNaoIdentificado['nascionalidade'])
print(" Nacionalidade dos clientes :")
print(" Americanos %i " % qtdAmericanos);
print(" Espanhois %i " % qtdEspanhol);
print(" Franceses %i " % qtdFrances);
print(" Brasileiros %i " % qtdBrasileiro);

#    exit(0);
                                         