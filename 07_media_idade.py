'''7) (BACKES, 2012) Faça um programa que leia um número indeterminado de idades de
indivı́duos (pare quando for informada a idade 0), e calcule a idade média desse grupo. Salve o
programa com o nome “​ 07_media_idade.py ​ ”.'''

soma=0.0
quant=0
idade=1

while idade!=0:
    idade=int(input("digite a idade:"))
    if idade==0:
        break
    soma+=idade
    quant+=1
print("Media das Idades:",soma/quant)