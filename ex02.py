"""Desenvolva um programa que recebe as notas dos alunos de uma turma. Seu programa deverá ser interrompido quando uma nota negativa for digitada.
Durante o processamento seu programa deverá contar o número de alunos nas seguintes condições:
- média abaixo de 3.5 (reprovados direto)
- média entre 3,5 e 7 (exame)
- acima de 7 (aprovados)
		Calcule a média aritmética da turma e informe o resultado no final.
E exiba na tela a quantidade de alunos: reprovados direto, exame aprovado.
"""

cont = 1
aprovados = 0
exame = 0
reprovados = 0
media = 0

alunos = float(input(f"Digite a nota do {cont}° aluno (0 a 10): "))

while(alunos>=0):

    cont += 1

    media += alunos

    if(alunos>7):
        aprovados += 1
    elif(alunos>= 3.5 and alunos<=7):
        exame += 1
    elif(alunos<3.5):
        reprovados += 1
    else:
        print("Nota digitada maior que 10, digite novamente")

    alunos = float(input(f"Digite a nota do {cont}° aluno (0 a 10): "))

media = media / cont

print(f"A média dos alunos é {media:.1f}")
print(f"Quantidade de alunos aprovados: {aprovados}")
print(f"Quantidade de alunos de exame: {exame}")
print(f"Quatidade de alunos reprovados: {reprovados}")

