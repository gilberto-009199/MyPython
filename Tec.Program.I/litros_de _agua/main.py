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

""" CAP 3 exercicio 5 """
import math
# A }
a = float(input("Digite o valor  de A :"))
b = float(input("Digite o valor  de B :"))
x = float(input("Digite o valor  de X :"))

numerador = (a ** 2) +  math.sqrt(3*b)
divisor   =  5 * math.pow(x,3)
y         =  numerador / divisor

input(y)


""" Uso de fuções trigonometricas """

graus = float(input("iNFORME O VALOR E GRAUS"))
radian = math.radians(graus)

seno = math.sin(radian)
cos  = math.cos(radian)
tan  = math.tan(radian)

print(" Seno :  ",seno)
print(" Coseno :  ",cos)
print(" Tangente :  ",tan)



