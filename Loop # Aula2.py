# Exercícios AULA 2 - Pyhton 

# Usando estruturas de repetição, faça um programa que leia 5 números via input de usuário e exiba qual é o maior número 
maior_num = 0
for i in range (5):
    num = int(input("Digite um número: "))
    if num > maior_num:
        maior_num = num

print("O maior número é:", maior_num)

# Usando estruturas de repetição, faça um programa que leia 5 números via input de usuário e exiba a soma e a média dos números
soma = 0
for i in range (5):
    num = int(input("Digite um número: "))
    soma += num
media = soma / 5

print("A soma é", soma, "e a média é", media)

# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50 
for i in range(51):
    if (i % 2 != 0):
        print(i)

# Faça um programa que receba dois números inteiros via linha de comando e gere os números inteiros que estão no intervalo compreendido por eles 
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

if num1 < num2:
    for i in range(num1, num2 + 1):
        print(i)
else:
    for i in range(num2, num1 + 1):
        print(i)

# Use um loop for que faça a tabuada do 2

for i in range (11):
    print(f"2 x {i} = {2 * i}")

# Use loops para fazer um programa que demonstra a tabuada do 2 até o 9

for num in range(2, 10):
    print(f"Tabuada do {num}:")
    for i in range(11):
        print(f"{num} x {i} = {num * i}")
    print()
