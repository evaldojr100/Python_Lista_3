'''11) (BACKES, 2012) Faça um programa que leia um número inteiro N e depois imprima os N
primeiros números naturais ı́mpares. Salve o programa com o nome “ 11_imprimir_impares.py ” ​ .'''

quant=int(input("Digite a quantidade de valores:"))
cont=0
i = 0
while cont != quant:
    if(i%2 == 1):
        print(i)
        cont += 1
    i += 1

