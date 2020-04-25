import math;

precisao = 50;

def fatorial(val):
    if val > 1:
        return val * fatorial(val - 1);
    else:
        return 1;

def seno(val):
    seno  = 0;
    isSum = True; #Vai somar bonitao?
    for index in range(1, precisao , 2): # <= codigo rebetido
        if isSum :
            seno += (val**index)/ fatorial(index);
        else:
            seno -= (val**index)/ fatorial(index);
        isSum = not isSum; #Inverte a operação
    return round(seno,5);

def cos(val):
    cos   = 0;
    isSum = True; #Vai negativar?
    for index in range(0, precisao , 2):# <= codigo repetido
        if isSum :
            cos += (val**index)/ fatorial(index);
        else:
            cos -= (val**index)/ fatorial(index);
        isSum = not isSum;#Inverte a operação
    return round(cos,5);

#theta    = math.radians(int(input(" Valor }> ")));
#precisao = int(input(" Precisao }> "));
theta    = math.radians(int(input()));
precisao = int(input());

print(seno(theta));
print(cos(theta));