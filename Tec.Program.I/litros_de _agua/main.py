"""

    Comentario de varias linha

"""

salarioMinimo   = float(input("Digite o salario minimo: }> R$ "))
aguaConsumida   = float(input("Digite a Quantidade consumida de Agua: }> "))

valorPorLitro   = (salarioMinimo * 0.02)/1000
valorConsumido  = aguaConsumida * valorPorLitro

print(" Valor por litro :   ",round(valorPorLitro,3))
print(" Valor a ser pago :  ",valorConsumido)
print(" Valor a ser pago com 15% de desconto :  ",round(valorConsumido * 0.85,3))


