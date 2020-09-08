var input = require('fs').readFileSync('OjogoMatemaricodePaula1992.txt', 'utf8');
//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

NUMENTRADAS = lines.shift() * 1;

let isUpperCase = (letra) => letra == letra.toUpperCase();

while ( NUMENTRADAS-- > 0 ){

    entrada = lines.shift();
    if( entrada[0]*1 == entrada[2]*1 )console.log( (entrada[2]*1) * (entrada[0]*1) )
    else if ( isUpperCase(entrada[1]) ) console.log( entrada[2]*1 - entrada[0]*1 )
    else console.log(  entrada[2]*1 + entrada[0]*1  ); 

}
