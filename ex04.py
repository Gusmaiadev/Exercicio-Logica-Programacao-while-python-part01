"""Faça um programa que verifique se uma "senha” numérica digitada pelo usuário está correta. O programa deve repetir o
pedido até que o usuário escreva o valor correto. A senha correta deve estar definida no próprio programa."""

senha = 225599

tentativa = int(input("Digite a senha: "))

while(tentativa!=225599):
    print("SENHA INCORRETA")
    tentativa = int(input("Digite a senha novamente: "))

print("ACESSO LIBERADO")