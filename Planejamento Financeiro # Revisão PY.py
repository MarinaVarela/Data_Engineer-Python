
import os
    
def limpar_tela():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_dinheiro(caixinha, valor, operacoes):
    """Adiciona dinheiro à caixinha."""
    if valor >= 0 or abs(valor) <= caixinha['saldo']:
        caixinha['saldo'] += valor
        operacoes.append({'tipo': 'adicao', 'valor': valor, 'saldo': caixinha['saldo'], 'nome': caixinha['nome']})
        return caixinha
    else:
        print("Não é possível adicionar esse valor. Operação cancelada.")
        return {input("Pressione ENTER para continuar...")}
    
def retirar_dinheiro(caixinha, valor, operacoes):
    """Retira dinheiro da caixinha, se houver saldo suficiente."""
    if caixinha['saldo'] >= valor:
        caixinha['saldo'] -= valor
        operacoes.append({'tipo': 'retirada', 'valor': valor, 'saldo': caixinha['saldo'], 'nome': caixinha['nome']})
        return caixinha
    else:
        print("Saldo insuficiente. Operação cancelada.")
        return {input("Pressione ENTER para continuar...")}

def verificar_saldo(caixinhas, operacoes):
    """Exibe o saldo das caixinhas e o histórico de operações."""
    print("Saldo das caixinhas:")
    for caixinha in caixinhas:
        nome = caixinha['nome']
        saldo = caixinha['saldo']
        print(f"{nome}: R${saldo:.2f}")
    print("\nHistórico de operações:")
    for operacao in operacoes:
        tipo = "adicionado" if operacao['tipo'] == 'adicao' else "retirado"
        valor = operacao['valor']
        saldo = operacao['saldo']
        nome = operacao['nome']
        print(f"{tipo} R${valor:.2f} da caixinha {nome}. Saldo: R${saldo:.2f}")
    print()

def criar_caixinha():
    """Cria uma nova caixinha."""
    nome = input("Digite o nome da nova caixinha: ")
    saldo = float(input("Digite o saldo inicial da nova caixinha: "))
    return {'nome': nome, 'saldo': saldo}

def planejamento_financeiro():
    """Realiza o planejamento financeiro."""
    caixinhas = []
    operacoes = []
    while True:
        limpar_tela()
        print("O que você gostaria de fazer?")
        print("1. Adicionar caixinha")
        print("2. Adicionar dinheiro em uma caixinha")
        print("3. Retirar dinheiro de uma caixinha")
        print("4. Verificar saldo das caixinhas e histórico de operações")
        print("5. Sair")
        opcao = int(input("Digite o número da opção desejada: "))
        if opcao == 1:
            caixinhas.append(criar_caixinha())
            print("Caixinha criada com sucesso.")
        elif opcao == 2:
            limpar_tela()
            nome_caixinha = input("Digite o nome da caixinha que deseja adicionar dinheiro: ")
            valor = float(input("Digite o valor que deseja adicionar: "))
            for caixinha in caixinhas:
                if caixinha['nome'] == nome_caixinha:
                    adicionar_dinheiro(caixinha, valor, operacoes)
                    break
            else:
                print("Caixinha não encontrada. Operação cancelada.")
        elif opcao == 3:
            limpar_tela()
            nome_caixinha = input("Digite o nome da caixinha que deseja retirar dinheiro: ")
            valor = float(input("Digite o valor que deseja retirar: "))
            for caixinha in caixinhas:
                if caixinha['nome'] == nome_caixinha:
                    retirar_dinheiro(caixinha, valor, operacoes)
                    break
            else:
                print("Caixinha não encontrada. Operação cancelada.")
        elif opcao == 4:
            limpar_tela()
            verificar_saldo(caixinhas, operacoes)
            input("Pressione ENTER para continuar...")
        elif opcao == 5:
            limpar_tela()
            print("Obrigado por utilizar o planejamento financeiro!")
            break
        else:
            limpar_tela()
            print("Opção inválida. Por favor, digite um número de 1 a 5.")
            input("Pressione ENTER para continuar...")
           
if __name__ == "__main__":
    planejamento_financeiro()