'''(BACKES, 2012) Faça um programa que calcule a área de um triângulo, cuja base e altura
são fornecidas pelo usuário. Esse programa não pode permitir a entrada de dados inválidos, ou
seja, medidas menores ou iguais a 0. Salve o programa com o nome “​ 08_area_triangulo.py ” ​ .'''

base=float(input("Digite a base do triangulo:"))
altura=float(input("Digite a altura do triangulo"))

if base==0 or altura==0:
    print("Dados invalidos!!")
else:
    print("area do triangulo:",(base*altura)/2)