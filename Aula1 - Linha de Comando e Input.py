# Exercícios AULA 1 - Pyhton 

# Faça um programa Python: Usando o input do usuario receba um nome e exiba a mensagem "Nome Recebido: (valor recebido)"  
nome = input ("Insira um nome: ")
print("Nome recebido:", nome)


# Faça um programa Python: Usando informacões via linha de comando receba um valor numerico e exiba a mensagem "Valor Recebido: x )" 
import sys
print("Digite um valor numérico:", str(sys.argv))
print("Valor recebido: ", str(sys.argv[1]))