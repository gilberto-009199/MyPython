var input = require('fs').readFileSync('EncaixaouNao1171.txt', 'utf8');
//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

NUMTESTES = lines.shift()*1;

while ( NUMTESTES-- > 0 ){

    entrada = lines.shift();
    numeros = entrada.split(" ");
    //console.log("RODADA : "+ NUMTESTES)
    // Verifica se o numero encaixa no ultimo
    isContain = true;
    for( var i = (numeros[0].length - numeros[1].length) + 1;
         i < (numeros[0].length) ;
         i++ ){
        
        //console.log("NUMERO 1°:" + numeros[0].slice( i - 1,i));
        //console.log("NUMERO 2°:" + numeros[1].slice( (i - numeros[0].length) - 1, i - numeros[0].length ));

        val0 = numeros[0].slice( i - 1,i);
        val1 = numeros[1].slice( (i - numeros[0].length) - 1, i - numeros[0].length );

        // Compara nao for iqual 
        if( isContain )isContain = val0 == val1;

    }
    if( isContain )console.log("encaixa");
    else console.log("nao encaixa");

}
