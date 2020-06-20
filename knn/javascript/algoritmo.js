const fs = require('fs');

function le_arquivo(nome){
   // Lista com os dados pegos linha por linha
   listDados = [];
   arquivo = fs.readFileSync(nome,'utf8').split('\n');
   for(let line of arquivo){
        // Corta o texto da linha para pegar cada dado
        carne_vermelha  = line.slice(4,9)   * 1;
        carne_branca    = line.slice(13,18) * 1;
        massa           = line.slice(22,27) * 1;
        fruta           = line.slice(31,36) * 1;
        vegetais        = line.slice(40,45) * 1;
        nascionalidade  = line.slice(50,57);
        // Monta o Cliente e adiciona na lista 
        listDados.push({  'carnes_vermelhas':carne_vermelha,
                            'carnes_brancas':carne_branca,
                            'massas':massa,
                            'frutas':fruta,
                            'vegetais':vegetais,
                            'nascionalidade':nascionalidade
                            });
   }
    // Retorna as informação guardadas na lista
    return listDados;
}

// Função que retorna a distancia euclidiana de 2 clientes
function getEuclidiana( cliente0 , cliente1){
    /*
        Distância euclidiana é a raiz quadrada da soma das
        diferenças dos valores dos atributos elevado ao quadrado
    */

    let soma = (cliente0.carnes_vermelhas - cliente1.carnes_vermelhas)** 2
             + (cliente0.carnes_brancas - cliente1.carnes_brancas)** 2
             + (cliente0.massas        - cliente1.massas        )** 2
             + (cliente0.frutas        - cliente1.frutas        )** 2
             + (cliente0.vegetais      - cliente1.vegetais      )** 2;

    return Math.sqrt(soma, 2); // ou soma ** (1/2);
}

// Pegando os dados 
listClassificados   = le_arquivo('mediaPorNasci.knn.algoritmo.txt');
listNaoClassificados = le_arquivo('comandas.knn.algoritmo.txt');

// Variaveis Acumuladoras de cada nacionalidade
qtdAmericanos = 0;
qtdEspanhol = 0;
qtdFrances = 0;
qtdBrasileiro = 0;

for(let clienteNaoIdentificado of listNaoClassificados){
    // Lista que ira ordenarar as pessoa mais proximos dele 
    listIndexadaPelaDistancia = [];
    for(let pessoaIdentificada of listClassificados){
        // Comparando e pegando a distancia
        distancia = getEuclidiana(clienteNaoIdentificado,pessoaIdentificada)
        // Colocando na lista de ordenacao
        listIndexadaPelaDistancia.push({
                  'distancia':distancia,
                  'nascionalidade': pessoaIdentificada['nascionalidade']
                 });
    }
    // Hora de ordenar pelos com menor
    // distancia
    let funcaoDeOrdenacao = function(a, b){ return a['distancia'] - b['distancia'] }
    // Usando o recurso de sort da linguagem
    listIndexadaPelaDistancia.sort( funcaoDeOrdenacao );


    K = 7;
    /*
       Escolhi 7, mas na minha opniao seria melhor
      pegar uma porcentagem dos classificados como 30% algo assim,
      quem sabe , afinal eu não sou um experti em algoritmos de 
      aprendizado supervisionado de maguina 
    */
    isAmerica = 0;
    isFrances = 0;
    isEspanho = 0;
    isBrasile = 0;
    for(let i of listIndexadaPelaDistancia.slice(0, K)){
        // Codigo que verifica qual nascionalidade é predominate
        if (i['nascionalidade'] == "America")
            isAmerica += 1;
        else if(i['nascionalidade'] == "Espanho")
            isEspanho += 1;
        else if(i['nascionalidade'] == "Frances")
            isFrances += 1;
        else if(i['nascionalidade'] == "Brasile")
            isBrasile += 1;
        else console.log("Categoria não identificada");
    }
    categoriaDefinida = "Indefinida...";
    // IFs apra verificar qual nacionalidade esta mais presente
    if(isAmerica>isEspanho && isAmerica > isFrances && isAmerica> isBrasile)
    {
        categoriaDefinida = "America";
        qtdAmericanos += 1;
    }
    else if(isEspanho>isAmerica && isEspanho>isFrances && isEspanho> isBrasile)
    {
        categoriaDefinida = "Espanho";
        qtdEspanhol += 1;
    }
    else if(isFrances>isAmerica && isFrances>isEspanho && isFrances> isBrasile)
    {
        categoriaDefinida = "Frances";
        qtdFrances += 1;
    }
    else if(isBrasile>isAmerica && isBrasile>isEspanho && isBrasile>isFrances)
    {
        categoriaDefinida = "Brasile";
        qtdBrasileiro += 1;
    }

    console.log("Categoria Definida   : ",categoriaDefinida)
    console.log("Categoria Verdadeira : ",clienteNaoIdentificado['nascionalidade'])
}
console.log(" Nacionalidade dos clientes :")
console.log(" Americanos  ", qtdAmericanos);
console.log(" Espanhois   " , qtdEspanhol);
console.log(" Franceses   " , qtdFrances);
console.log(" Brasileiros " , qtdBrasileiro);