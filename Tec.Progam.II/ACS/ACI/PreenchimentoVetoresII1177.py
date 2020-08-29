val = int(input());

count = 0;
for index in range(0,6):
    print("N[%s] = %s" %( index, count ) );
    if count < (val - 1):
        count+=1;
    else:
        count = 0;
    