
maior = 0;

while True:
    val0 = int(input());
    if val0 < 0 :
        break;
    maior = maior if maior > val0 else val0;

print(maior);