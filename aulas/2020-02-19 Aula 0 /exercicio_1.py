class Quesitos:
  def getMedia(self):
    return (self.conteudo + self.criatividade + self.validacao + self.elaboracao ) / 4;
  def setConteudo(self,nota):
    self.conteudo = int(nota);
    return self;
  def setCriatividade(self,nota):
    self.criatividade = int(nota);
    return self;
  def setValidacao(self,nota):
    self.validacao = int(nota);
    return self;
  def setElaboracao(self,nota):
    self.elaboracao = int(nota);
    return self;
  def getConteudo(self):
    return self.conteudo;
  def getCriatividade(self):
    return self.criatividade;
  def getValidacao(self,nota):
    return self.validacao;
  def getElaboracao(self,nota):
    return self.elaboracao;

class Ativity:
  def __init__(self,nome):
    self.nome = nome;
    self.quesitos = Quesitos();
  def setNome(self,nome):
    self.nome = nome;
    return self;
  def getNome(self):
    return self.nome;
  def setQuesitos(self,quesitos):
    self.quesitos = quesitos;
    return self;
  def getQuesitos(self):
    return self.quesitos;

# Caso eu esteja errado sobre as atividades altere para 1 
ATIVIDADES = 7;


print("Programa que calcula a media de ", ATIVIDADES ,"atividades");

while True:

  listAtividades = [];
  mediaGeral = 0;
  
  for atividade in range(0,ATIVIDADES):
    
    nome          = input("\n Digite o nome da atividade }> ");
    conteudo      = input(" Digite o valor no quesito conteudo geral }> ");
    criatividade  = input(" Digite o valor no quesito criatividade }> ");
    validacao     = input(" Digite o valor no quesito Validação }> ");
    elaboracao    = input(" Digite o valor no quesito Estruturação e Elaboração do Problema }> ");
    tmpAtividade  = Ativity(nome);
    quesitos      = tmpAtividade.getQuesitos();
    quesitos.setConteudo(conteudo).setCriatividade(criatividade).setValidacao(validacao).setElaboracao(elaboracao);  
    # Se fosse em java isso seria bem mais bonito
    # obj.sadsdd3(sads)
    #    .asdsada(asdad)
    #    .sadad(asadsd);
    mediaGeral += quesitos.getMedia(); 
    print("\n Atividade ",atividade + 1 ," - ",tmpAtividade.getNome()," registrada!")
    print(" Media :",tmpAtividade.getQuesitos().getMedia());
    print(" Faltam ", (ATIVIDADES - atividade) - 1 ," atividades não registradas ");
    listAtividades.append(tmpAtividade)

  mediaGeral = round(mediaGeral / ATIVIDADES,3) ;
  print("\n Media final baseada nas ",ATIVIDADES," atividades registradas : ",mediaGeral);
  proceder = input("\n Deseja recomeçar?(S/N) }> ");
  if (proceder.lower() == "s" or proceder.lower() == "sim" or proceder.lower() == "si" or proceder.lower() == "y"):
    continue;
  else:
    print("Bye :)");
    exit();
    
