v = 7 * [0]
i = 0;

while i < 7:
    v[i] = float(input("Valor }> "));
    i += 1;

s = 0;
q = 0;
i = 0;

while i < 7 :

    if v[i] > 0:
        s += v[i];
        q += 1;
    else:
        print('%.1f' % v[i]);
    i += 1;

print('%.1f' % (s/q) )