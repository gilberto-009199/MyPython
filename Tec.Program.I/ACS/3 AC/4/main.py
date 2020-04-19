
isImpar =   lambda val : val % 2 == 1;

val0    =   int(input());
val1    =   int(input()); 


for index in range(val0, val1 + 1):
    if isImpar(index):
        print(index);