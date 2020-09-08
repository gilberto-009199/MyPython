var input = require('fs').readFileSync('DeDentroparaFora1235.txt', 'utf8');
//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

NUMENTRADAS = lines.shift()*1;


while ( NUMENTRADAS-- > 0 ){

    entrada = lines.shift();
    linhaEsquerda = "";
    linhaDireita = "";
    
    for(    var i = entrada.length / 2 -1 , j = entrada.length - 1;
            i > -1;
            i--,j--
        ){

        linhaEsquerda += entrada[ i ];
        linhaDireita  += entrada[ j ];
        //console.log(` I :  ${ i } LETRA : ${ entrada[ i ] }`);
        //console.log(` J :  ${ j } LETRA : ${ entrada[ j ] }`);
    }

    //console.log(linhaEsquerda);
    //console.log(linhaDireita);

    //console.log(entrada)
    console.log(linhaEsquerda + linhaDireita)
}