'''6) (Python.org.br) O Departamento Estadual de Meteorologia lhe contratou para desenvolver
um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a
menor e a maior temperaturas informadas, bem como a média das temperaturas. Salve o
programa com o nome “​ 06_meteorologia.py ” ​.'''

soma=0.0
quant=0
maior=0
menor=0
escolha='s'

while escolha=='s':
    temp=float(input("digite a temperatura:"))
    soma+=temp
    quant+=1
    if temp>maior or maior==0:
        maior=temp
    if temp<menor or menor==0:
        menor=temp
    escolha=input("Digite (s) para digitar outra temperatura ou (n) para não")
print("Media das temperaturas:%.2f, Maior Temperatura: %.2f, Menor Temperatura: %.2f"%(soma/quant,maior,menor))