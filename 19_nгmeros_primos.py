n = int(input("Insira um número: "))
i = 0
cont = 0
cont2 = 0
while i <= n:
    i += 1
    if n % i == 0:
        cont += 1
    else:
        cont2 += 1
        
if cont <= 2:
    print("Primo")
else:
    print("Não Primo")