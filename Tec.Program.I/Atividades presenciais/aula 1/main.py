"""
    
    3 :             
        # E um pena que (not isAprovado) não é o suficiente!

        isAprovado  = n_aluno >= 7 and f_aluno <= 25
        isReprovado = n_aluno < 5  and f_aluno  > 25
         
        O contrario passou o sinal de (maior ou iqual) para (menor) a nota
        O contrario passou o sinal de (menor ou iqual) para (maior) a falta

        "Quanto mais sofisticado é o jogo mais sofisticado e o oponente"
                                                    Filme: Revolver 2015
"""


def exibe_status(n_aluno,f_aluno):

    msg = "Aluno reprovado!";

    if n_aluno >= 7 and f_aluno <= 25 :
        msg = "Aluno aprovado!";
    elif n_aluno >= 5 and f_aluno <= 25 :
        msg = "Aluno em recuperação!";

    return msg;

aluno = {"falta":0,"nota":0};
aluno["nota"] = float(input("   Nota final  }> "));
aluno["falta"] = float(input("   Faltas   %  }> "));

print(exibe_status(aluno["nota"],aluno["falta"]));