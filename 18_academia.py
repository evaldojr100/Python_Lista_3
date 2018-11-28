cont = 0
cod = 1
while cod != 0:
    cod = int(input("Informe código: "))
    altura = float(input("Insira altura(m): "))
    peso = float(input("Insira peso(Kg): "))
    cont +=1

    if cont == 1:
        maiorAlt = altura
        maiorPeso = peso
        menorAlt = maiorAlt
        menorPeso = maiorPeso

    if altura > maiorAlt:
        maiorAlt = altura
        maiorAltCod = int(cod)

    if altura < menorAlt:
        menorAlt = altura
        menorAltCod = int(cod)

    if peso > maiorPeso:
        maiorPeso = peso
        maiorPesoCod = int(cod)

    if peso < menorPeso:
        menorPeso = peso
        menorPesoCod = int(cod)

print("Maior Altura - Codigo", maiorAltCod)
print("Altura: ", maiorAlt, "m")
print("Menor Altura - Codigo", menorAltCod)
print("Altura: ", menorAlt, "m")
print(" ")
print("Maior Peso - Codigo", maiorPesoCod)
print("Peso: ", maiorPeso, "Kg")
print("Menor Peso - Codigo", menorPesoCod)
print("Peso: ", menorPeso, "Kg")





















