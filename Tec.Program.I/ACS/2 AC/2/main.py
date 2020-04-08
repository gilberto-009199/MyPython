# -*- coding: utf-8 -*-

idade = int(input());

tipoEleitor = "nao eleitor";

if  17 < idade < 66:
    tipoEleitor = "eleitor obrigatorio";
elif 15 < idade or idade > 65: # entre 16 e 18 anos ou acima dos 65 anos
    tipoEleitor = "eleitor facultativo";

print(tipoEleitor);