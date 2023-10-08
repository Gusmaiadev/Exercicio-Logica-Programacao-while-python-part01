"""Desenvolva um programa que solicite números inteiros ao usuário e calcule a soma deles até que o 0 seja digitado."""

soma = 0

num = int(input("Digite um número: "))

while(num!=0):
    soma += num
    num = int(input("Digite outro número (Digite zero caso queira encerrar): "))
print(f"A soma dos números digitados é {soma}")
    