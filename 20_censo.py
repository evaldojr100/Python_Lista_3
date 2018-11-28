op = 's'
soma = 0
idadeSoma = 0
pesoSoma = float(0)
alturaSoma = float(0)
contF = 0
contM = 0
contVerdeLoiro = 0

while op == 's':
    soma += 1
    sexo = input("Sexo(f/m): ")
    sexo.lower()
    if sexo == 'f':
        contF += 1
    elif sexo == 'm':
        contM += 1
    else:
        print("Valor Inválido. Não será contabilizado")
    olho_cor = input("Cor dos olhos (Verdes = v | Azuis = a | Castanhos = c): ")
    cabelo_cor = input("Cor dos cabelos (Loiros = l | Ruivos = r | Castanhos = c | Pretos = p): ")
    if olho_cor == 'v' and cabelo_cor == 'l':
        contVerdeLoiro += 1
    idade = int(input("Idade: "))
    idadeSoma += idade
    altura = float(input("Altura(m): "))
    alturaSoma += altura
    peso = float(input("Peso(Kg): "))
    pesoSoma += peso
    op = input("Continuar a Inserir valores para  novas pessoas?(S/N): ")
    print(" ")

print("Media da idade dos participantes: ", idadeSoma/soma, " anos")
print("Media de peso dos participantes: ", round(pesoSoma/soma), " Kg")
print("Media da altura dos participantes: ", round(alturaSoma/soma)," metros")
print("Porcentagens de pessoas do sexo feminino: ", round((contF+contM)/(contF*100)*100), "%")
print("Porcentagens de pessoas do sexo masculino: ", round((contF+contM)/(contM*100)*100), "%")
print("Quantia de pessoas com olhos verdes e cabelos loiros: ", contVerdeLoiro, " pessoas")