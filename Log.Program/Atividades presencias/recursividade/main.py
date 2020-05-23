def fib(n):
    if n <= 2: return 1;
    else:
        return fib(n - 1) + fib(n - 2);

def fat(n):
    if n == 0 :
        return 1;
    else:
        return n * fat( n-1 );

print(fat(5))
print(fib(7))