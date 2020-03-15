# -*- coding: utf-8 -*-
cifras     = int(input());
listLetras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listCifras = [];

class TextoCifrado:
  def setTexto(self,texto):
    self.texto = texto;
    return self;
  def setDeslocamento(self,deslocamento):
    self.deslocamento = deslocamento;
    return self;
  def genCifragem(self):
    cifragem = "";
    for letra in self.texto :
      #print(letra);
      NovaLetra = listLetras[listLetras.index(letra)-self.deslocamento];
      #print(letra,"  = @ =  ",NovaLetra);
      cifragem += NovaLetra;
    return cifragem;


while( cifras > len(listCifras)) :
 
 texto 	      = str(input()).lower();
 deslocamento = int(input());

 tmpTexto     = TextoCifrado();

 tmpTexto.setTexto(texto);
 tmpTexto.setDeslocamento(deslocamento);
 
 #tmpTexto.genCifragem();

 listCifras.append( tmpTexto.genCifragem().upper() );

for cifra in listCifras :
  print(cifra);
