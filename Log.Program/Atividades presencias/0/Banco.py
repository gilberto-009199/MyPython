salario = float(input("salario : "))
tempo   = int(input("anos :"))
emp     = float(input("emprestimo :"))

msg = "";

if salario > 2000 :
    if  tempo > 2 :
        juros = emp * 0.2;
    else:
        juros = emp * 0.15;
    msg = emp + juros;
else:
    msg = "Emprestimo negado"

print(msg)