# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.
numero = int(input("digite um número para ver a sua tabuada: "))

print(f"a tabuada de {numero}")

for i in range(1, 11):
    multiplos = numero * i
    print(f"{numero} * {i} = {multiplos} ")
