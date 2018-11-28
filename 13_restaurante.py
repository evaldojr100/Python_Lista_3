'''13) (LIVI & EDELWEISS, 2014) Em pesquisa feita em um Restaurante Universitário,
perguntou-se a cada aluno quantas refeições ele fez no mê anterior. Faça um programa que
forneça:
● O número de alunos entrevistados;
● O número de alunos que fez menos de 10 refeições ao mês;
● O número de alunos que fez entre 10 e 20 refeições;
● O número de alunos que fez mais de 20 refeições;
Salve o programa com o nome “​ 13_restaurante.py” ​ .'''

opcao='s'
alunos=0
alu_menos_10=0
alu_10_20=0
alu_mais_20=0

while opcao == 's':
    valor=int(input("Digite quantas refeição vc faz por dia:"))
    alunos += 1
    if valor<10:
        alu_menos_10+=1
    if 10<=valor<=20:
        alu_10_20+=1
    if valor>20:
        alu_mais_20+=1
    opcao=input("deseja inserir mais uma entrevista (s/n):")

print("O número de alunos entrevistados:",alunos)
print("O número de alunos que fez menos de 10 refeições ao mês:",alu_menos_10)
print("O número de alunos que fez entre 10 e 20 refeições:",alu_10_20)
print("O número de alunos que fez mais de 20 refeições:",alu_mais_20)
