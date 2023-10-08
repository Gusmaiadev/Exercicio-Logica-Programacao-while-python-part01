"""Escreva um algoritmo que solicite dois números e devolva quantos pares e ímpares há entre esses dois números.
Exemplo: entre 7 e 10 há 2 números pares e 2 números ímpares
"""
par = 0
impar = 0
aramazem = 0


inicio = int(input("Digite um número: "))
fim = int(input("Digite outro número (maior que o primeiro): "))

armazem = inicio

while(inicio<=fim):
    if(inicio%2==0):
        par += 1
    else:
        impar += 1

    inicio += 1

print(f"A {par} números pares entre {armazem} e {fim}")
print(f"A {impar} números impares entre {armazem} e {fim}")
