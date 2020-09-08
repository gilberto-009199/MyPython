//var input = require('fs').readFileSync('FrequenciaNumeroTest.txt', 'utf8');
var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

NUMENTRADAS = lines.shift()*1;

listNumeros = {};
while ( NUMENTRADAS-- > 0 ){

    entrada = lines.shift();
    
    if (listNumeros[entrada+""] == undefined )listNumeros[entrada+""] = 1
    else listNumeros[entrada+""] += 1; 
}

for( let valor of Object.keys(listNumeros) ){
    console.log(`${valor} aparece ${listNumeros[valor]} vez(es)`);
}