# -*- coding: utf-8 -*-

xy1 = str(input()).split(" ");
x1  = float(xy1[0]);
y1  = float(xy1[1]);
  
xy2 = str(input()).split(" ");
x2  = float(xy2[0]);
y2  = float(xy2[1]);

distancia =( ( x2 - x1 )**2 + ( y2 - y1 )**2 ) ** (1/2);

print("%.4f"% distancia );
