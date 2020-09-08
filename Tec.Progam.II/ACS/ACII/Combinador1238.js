var input = require('fs').readFileSync('Combinador1238.txt', 'utf8');
//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

NUMENTRADAS = lines.shift()*1;

while ( NUMENTRADAS-- > 0 ){

    entrada = lines.shift();

    palavras = entrada.split(" ");
    TamanhoPalavraMenor = palavras[1].length < palavras[0].length ? palavras[1].length : palavras[0].length;
    palavraFinal = "";
    
    for( var i = 0 ; i < TamanhoPalavraMenor / 2 +1  ; i++ ){
        console.log(palavras[0][i] +""+ palavras[1][i]);
        palavraFinal  += palavras[0][i] +""+ palavras[1][i];
    }
    
    //palavraFinal += palavras[1].length > TamanhoPalavraMenor ? palavras[1].slice(j+1,palavras[1].length) : palavras[0].slice(j+1,palavras[0].length);
    
    if(palavraFinal.length < (palavras[0].length + palavras[1].length)){
        console.log(`Tem algo faltando! ${palavraFinal.length}`);
        palavraFinal +=  palavras[0].slice(palavraFinal.length ,palavras[0].length ) + palavras[1].slice( palavraFinal.length-1, palavras[1].length ) 
    }

    //console.log(TamanhoPalavraMenor)
    console.log(palavraFinal)
}