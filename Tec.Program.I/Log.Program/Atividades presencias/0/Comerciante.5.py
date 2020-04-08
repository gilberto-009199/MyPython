"""
 Comerciante de alcool gel
    40%
    30%
"""
valorCompra = float(input("Digite o peco de compra }>"));

valorVenda  = valorCompra * 1.40;

if valorCompra  < 20:
    valorVenda = valorCompra * 1.30;

print("Valor de venda }> R$ %0.2f" % valorVenda);