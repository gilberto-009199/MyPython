# -*- coding: utf-8 -*-
import math;

# Angulo >>> radianos
theta       = math.radians(float(input()));

# m/s²
velocidade  = float(input());
gravidade   = float(input());


altura = ( (velocidade**2) * (math.sin(theta) ** 2)  ) / (2 * gravidade);

print(altura)
