'''5) (BACKES, 2012) Faça um programa que peça ao usuário para digitar 10 valores e some-os.
Salve o programa com o nome “​ 05_soma_de_10_valores.py ​ ”'''

soma=0
for i in range(1,11):
    valor=int(input("Digite o %d numero:"%(i)))
    soma+=valor

print("Soma Total:",soma)