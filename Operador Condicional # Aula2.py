# Exercícios AULA 2 - Pyhton 

# Faça um programa que peça dois números via linha de comando e imprima o maior deles 
import sys 

print("O primeiro número é", sys.argv[1])
print("O segundo número é", sys.argv[2])

if (int(sys.argv[1]) > int(sys.argv[2])):
    print("O maior número é", sys.argv[1])
elif (int(sys.argv[1]) < int(sys.argv[2])):
    print("O maior número é", sys.argv[2])
else:
    print ("Números iguais.")
       
# Faça um programa que peça um valor via input de usuário e mostre na tela se o valor é positivo ou negativo 
num1 = float(input ("Digite um valor: "))

if (num1 > 0):
    print("O valor é positivo.")
elif (num1 == 0):
    print("o número digitado foi 0")
else:
    print("O valor é negativo.")

# Faça um programa que peça uma idade via input de usuário e exiba uma mensagem informando se essa pessoa é maior ou menor de idade 
idade = int(input ("Informe uma idade: "))

if (idade >= 18):
    print ("Vocês é maior de idade.")
else:
    print ("Você é menor de idade.")

# Faça um programa que leia três números e mostre o maior deles 
import sys 

if (int(sys.argv[1]) > int(sys.argv[2]) and int(sys.argv[1]) > int(sys.argv[3])):
    print("O maior número é", sys.argv[1])
elif (int(sys.argv[1]) < int(sys.argv[2]) and int(sys.argv[2]) > int(sys.argv[3])):
    print("O maior número é", sys.argv[2])
else:
    print ("O maior número é", int(sys.argv[3]))

# Faça um programa que leia um número via input de usuário e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.). 
# Para valores negativos ou maiores que 7 exibir a mensagem "valor inválido" 

numero = int(input("Insira o número referente ao dia correspondente da semana: "))

if (numero == 1):
    print("1- Domingo")
elif (numero == 2):
    print("2- Segunda")
elif (numero == 3):
    print("3 - Terça")
elif (numero == 4):
    print("4 - Quarta")
elif (numero == 5):
    print("5 - Quinta")
elif (numero == 6):
    print("6 - Sexta")
elif (numero == 7):
    print("7 - Sábado")
else:
    print("Valor inválido")

# Faça um programa que leia via input de usuário um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto 
ano = int(input("Insira um ano: "))

if (ano % 4 == 0):
    print("O ano", (ano), "é bissexto")
else:
    print("O ano", (ano), "não é bissexto")

# Faça um programa que receba via input de usuário os valores de duas notas de uma aluna. O programa deve calcular a média alcançada e apresentar: 
# A mensagem "Aprovado", se a média alcançada for maior ou igual a 7; A mensagem "Reprovado", se a média for menor do que 7; A mensagem "Aprovado com Distinção", se a média for igual a 10 
nota1 = int(input("Insira a nota 1: "))
nota2 = int(input("Insira a nota 2: "))
media = (nota1+ nota2) / 2

if (media >= 7):
    if (media == 10):
        print("Aprovado com distinção")
    else:
        print("Aprovado")
else:
    print("Reprovado")

# [Desafio] Faça um programa que leia via linha de comando três números e mostre-os em ordem decrescente. 
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
print("Os números são", num1, num2, num3)

print(*sorted([num1, num2, num3], reverse=True))


#[Desafio] Faça um programa que faça 5 perguntas para uma pessoa sobre um crime: "Falou com a vítima no dia do crime?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia dinheiro para a vítima?" "Já trabalhou com a vitima?" 
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassina". Caso contrário, ela será classificada como "Inocente" 

positive_answers = 0

answer = input("Falou com a vítima no dia do crime? (s/n) ")
if answer.lower() == "s":
    positive_answers += 1

answer = input("Esteve no local do crime? (s/n) ")
if answer.lower() == "s":
    positive_answers += 1

answer = input("Mora perto da vítima? (s/n) ")
if answer.lower() == "s":
    positive_answers += 1

answer = input("Devia dinheiro para a vítima? (s/n) ")
if answer.lower() == "s":
    positive_answers += 1

answer = input("Já trabalhou com a vitima? (s/n) ")
if answer.lower() == "s":
    positive_answers += 1

if positive_answers == 2:
    print("Suspeita")
elif positive_answers >= 3 and positive_answers <= 4:
    print("Cúmplice")
elif positive_answers == 5:
    print("Assassina")
else:
    print("Inocente")
