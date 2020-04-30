

listAlimentos = ['cereal', 'banana', 'maçã', 'melão','iogurte'];

def imprimirVetor(list):
    for index, item in enumerate(list):
        print(" %0.0f - %s " % (index,item));

imprimirVetor(listAlimentos);

print("Tamanho : %i" % len(listAlimentos));
print(" %0.0f - %s " % (3,listAlimentos[3]));

listAlimentos.append(input("Digite o novo alimento }> "));

imprimirVetor(listAlimentos);

del listAlimentos[2];

print("Retirando %0.0f - %s " % (2,listAlimentos[2]));
imprimirVetor(listAlimentos);
