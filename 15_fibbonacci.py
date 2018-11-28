n = int(input("Insira qtd de termos p/ a sequencia de Fibonnacci: "))
i = 0
cont = 0
ant1 = 0
ant2 = 1
while cont <= n:
    i = ant1 + ant2
    print(i)
    ant2 = ant1
    ant1 = i
    cont += 1