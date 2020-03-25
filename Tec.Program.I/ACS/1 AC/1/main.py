# -*- coding: utf-8 -*-

distancia = lambda x1,y1,x2,y2: ( (x2 - x1)**2 + (y2 - y1)**2 )**(1/2)

A = { "x":0, "y":0 };
B = { "x":0, "y":0 };

A["x"] = float(input());
A["y"] = float(input());
B["x"] = float(input());
B["y"] = float(input());

AB = distancia(A["x"],A["y"],B["x"],B["y"]);

print(AB);