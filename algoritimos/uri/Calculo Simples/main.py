# -*- coding: utf-8 -*-

produto1   = (str(input())).split(" ");
produto2   = (str(input())).split(" ");

totalProduto1 = float(produto1[1])  * float(produto1[2]); 
totalProduto2 = float(produto2[1]) * float(produto2[2]); 


print("VALOR A PAGAR: R$ %.2f" % (totalProduto1 + totalProduto2));
