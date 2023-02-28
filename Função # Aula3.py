# Exercícios AULA 3 - Pyhton 

# Escrever uma função chamada "escreve_nome". Usando o while, escrever "Academia Python" por 5 vezes, usando print 
def escreve_nome():
    i = 0
    while i < 5:
        print("Academia Python")
        i += 1


# Escrever uma função chamada "escreve_nome_com_retorno". Fazer com que essa função retorne "Academia Python". Usando print, imprima o retorno dessa função 
def escreve_nome_com_retorno():
    return "Academia Pyhton"


# Faça uma função que receba um argumento inteiro. A função retorna o valor de caractere 'P', se seu argumento for positivo, e 'N', se seu argumento for zero ou negativo
def inteiro(arg):
    if arg > 0:
        return "P"
    else:
        return "N"

print(inteiro(-2))
print(inteiro(50))


# Faça uma função que necessite de três argumentos, e que retorne a soma desses três argumentos. 
def soma (arg1, arg2, arg3):
    return arg1 + arg2 + arg3

print(soma(2,4,3))
print(soma(300,500,400))


# Criar uma função chamada "imprime_tabuada". Usando o for, imprimir as tabuadas de 1 a 9, no mesmo formato do exercício anterior: 
def imprime_tabuada():
    for num in range(1, 10):
        print(f"Tabuada do {num}:")
    for i in range(11):
        print(f"{num} x {i} = {num * i}")
    print()


# Faça uma função que receba 4 notas em valor decimal, entre O e 10. Caso a nota seja menor que 5, retornar "Reprovada". Caso a nota esteja entre 5 e 7, retornar "Está na média". Caso a nota esteja maior que 7, retomar "Aprovada". 
def calcula_aprovacao():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 7:
        print("Aprovada")
    elif media >= 5:
        print("Está na média")
    else:
        print("Reprovada")


# Faça uma função que receba 5 números e imprima a soma e a média dos números. 
def calcula_soma_media():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    num4 = float(input("Digite o quarto número: "))
    num5 = float(input("Digite o quinto número: "))
    
    soma = num1 + num2 + num3 + num4 + num5
    media = soma / 5
    
    print("A soma dos números é:", soma)
    print("A média dos números é:", media)


# Faça uma função que receba parãmetros variáveis. Faça algumas chamadas dessa função passando valores inteiros e, de acordo com a quantidade de parãmetros recebidos, calcule a média def calcula_media(*args):
def calcula_media(*args):
    n = len(args)
    if n == 0:
        return 0
    soma = sum(args)
    media = soma / n
    return media