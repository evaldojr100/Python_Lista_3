'''14) (PUGA & RISSETI, 2016) Escreva um algoritmo que leia uma quantidade qualquer de
números, fornecidos pelo usuário. Faça a contagem e exiba quantos estão nos seguintes
intervalos: [0 a 25.9], [26 a 50.9], [51 a 75.9] e [76 a 100], sendo que a entrada de dados deve
terminar quando for digitado um número negativo. Salve o programa com o nome
“​ 14_intervalo_numeros.py ​ ”.'''

valor=0
intervalo1=0
intervalo2=0
intervalo3=0
intervalo4=0
while valor>=0:
    valor=int(input("Digite um numero:"))
    if 0<=valor<=25.9:
        intervalo1+=1
    if 26<=valor<=50.9:
        intervalo2+=1
    if 51<=valor<=79.9:
        intervalo3+=1
    if 76<=valor<=100:
        intervalo4+=1

print("Numeros no intervalo [0 a 25.9]:",intervalo1)
print("Numeros no intervalo [26 a 50.9]:",intervalo2)
print("Numeros no intervalo [51 a 75.9]:",intervalo3)
print("Numeros no intervalo [76 a 100]:",intervalo4)