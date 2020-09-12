var input = require('fs').readFileSync('OrdenaçãoPorTamanho1244.txt', 'utf8');
//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

NUMENTRADAS = lines.shift() * 1;
listSaidas = [];

while ( NUMENTRADAS-- > 0 ){

    entrada = lines.shift();
    
    listPalavra = {};
    palavras = entrada.split(" ");
    saida = "";

    for(let item of palavras){
        if(listPalavra[item.length+""] == undefined)listPalavra[item.length+""] = item;
        else listPalavra[item.length+""] += " " + item;
    }
    // Executa uam ordenacao baseado
    for( let valor of Object.keys(listPalavra) ){
        //console.log(listPalavra[valor+""]);
        saida = listPalavra[valor+""] +" "+ saida;
    }
    listSaidas.push(saida);
}
// Achei que era para exibir conforme ele enviava kkk
for(let saida of listSaidas){
    console.log(saida.trim());
}