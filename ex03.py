"""Mostrar todos os inteiros entre dois números digitados pelo usuário. Exemplo: usuário digita os números 8 e 15,
e aparecem em tela: 9, 10, 11, 12, 13, 14."""

inicio = int(input("Digite um número inteiro: "))
fim = int(input("Digite outro número inteiro (maior que o primeiro): "))

while(inicio<fim - 1):
    inicio += 1
    print(inicio)