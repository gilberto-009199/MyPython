# -*- coding: utf-8 -*-
""" Basquete de Robôs """



distancia = int(input());
msg = "";
if distancia <= 800:
    msg = "1";
if 800 < distancia <=1400 :
    msg = "2";
if 1400 < distancia <= 2000:
    msg = "3";



print(msg);
