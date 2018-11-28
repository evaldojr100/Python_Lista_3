'''17) (PUGA & RISSETI, 2016) Construa um algoritmo que encontre a mediana de uma
sequência de números inteiros fornecida pelo usuário (número inicial e final), utilizando
estrutura de repetição. Por exemplo, a mediana da sequência "1, 2, 3, 4, 5" é 3 e da sequência
"2, 3, 4, 5, 6, 7, 8, 9" é (5 + 6) / 2 = 5,5. Como sugestão utilize a variável i para o número iniciale j para o número final, realizando operações de incremento e decremento. Salve o programa
com o nome “​ 17_mediana.py ​ ”.'''

i = int(input("Insira valor inicial do intervalo: "))
j = int(input("Insira valor final do intervalo: "))

while i < j:
    i += 1
    j -= 1

mediana = (i+j)/2
print("a Mediana: ",mediana)