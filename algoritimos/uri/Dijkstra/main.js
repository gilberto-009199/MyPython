var input = require('fs').readFileSync('./file.txt', 'utf8');
var lines = input.split('\n');

var listJoias = [];
var joias = 5;
var tipo  = 0;

for(i = 0; i < joias ; i++){
 
   tty = lines.shift();
   //console.log("TIPO : "+tipo)
   console.log("TTY  : " + tty)
   //console.log(listJoias.join(","))
   //console.log("if   :" + listJoias.indexOf(tty))
   if(listJoias.indexOf(tty) == -1){
     tipo++;
     console.log("Não tem \n")
   }
   
   listJoias.push(tty);

}
console.log(tipo)
