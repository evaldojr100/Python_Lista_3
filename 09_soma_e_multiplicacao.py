'''9) (BACKES, 2012) Faça um programa que receba dois números. Calcule e mostre: A soma
dos números pares desse intervalo de números, incluindo os números digitados; A
multiplicação dos números ı́mpares desse intervalo, incluindo os digitados; Salve o programa
com o nome “​ 09_soma_e_multiplicacao.py ​ ”.'''

num1=int(input("Digite o 1 numero:"))
num2=int(input("Digite o 2 numero:"))
soma=0
mult=0
for i in range(num1,num2+1):
    if i%2==0:
        soma+=i
    if i%3==1:
        mult*=i
