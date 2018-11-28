'''16) (PUGA & RISSETI, 2016) Pedro tem 1,50 m e cresce 2 cm por ano, enquanto Lucas tem
1,10 m e cresce 3 cm por ano. Construa um algoritmo que calcule e imprima quantos anos
serão necessários para que:
a) Lucas e Pedro tenham o mesmo tamanho.
b) Lucas seja maior que Pedro.
Salve o programa com o nome “​ 16_crescimento.py ​ ”.'''


pedro=1.50
lucas=1.10
cont=0

while lucas<pedro:
    lucas+=0.03
    pedro+=0.02
    cont+=1

print(cont,"anos para Lucas passar Pedro!!")