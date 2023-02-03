# Exercícios AULA 2 - Pyhton 

# Faça um programa que peça dois números via input e imprima a soma dos valores. 
num1 = input ("Digite o primeiro número: ")
num2 = input ("Digite o segundo número: ")
soma = int (num1) + int (num2)
print("A soma dos números é:", soma)

# Faça um programa que peça via linha de comando as 4 notas bimestrais e mostre a média. 
import sys

print("Primeira nota: "+ sys.argv[1])
print("Segunda nota: "+ sys.argv[2])
print("Terceira nota: "+ sys.argv[3])
print("Quarta nota: "+ sys.argv[4])

soma = (int(sys.argv[4]) + int(sys.argv[1]) + int(sys.argv[2]) + int(sys.argv[3]))
media = soma / 4

print ("A média das notas é:", media)

# Faça um programa que peça um valor numérico via input representando metros e converta esses metros para centímetros. 
metros = input ("Indique um valor em metros: ")
cm = int(metros) * 100
print("O valor em metros é", metros, "e em centímetros esse valor é de", cm)

# Faça um programa que peça via linha de comando o valor do tamanho do lado de um quadrado e faça o cálculo da área. Exiba o valor dessa área. ■ lado = 3cm 
import sys

print("Indique o lado do quadrado em centímetros: " + sys.argv[1])
area = int(sys.argv[1]) * int(sys.argv[1])
print("A área do quadrado é de", area)

