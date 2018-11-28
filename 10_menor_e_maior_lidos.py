'''10) (BACKES, 2012) Escreva um programa que leia 10 números e escreva o menor valor lido e
o maior valor lido. Salve o programa com o nome “​ 10_menor_e_maior_lidos.py ​ ”.'''

maior=0
menor=0

for i in range(0,10):
    valor=int(input("Digite um numero:"))
    if valor>maior or maior==0:
        maior=valor
    if valor<menor or menor==0:
        menor=valor

print("Maior Valor:",maior)
print("Menor Valor:",menor)