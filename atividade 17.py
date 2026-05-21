# Sistema bancário simples utilizando POO (Programação Orientada a Objetos)

# Criação da classe ContaBancaria
class ContaBancaria:

    # Método construtor da classe
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    # Método para depositar dinheiro
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    # Método para sacar dinheiro
    def sacar(self, valor):

        # Verifica se há saldo suficiente
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    # Método para exibir saldo
    def exibir_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R${self.saldo:.2f}")


# Criação da conta bancária
nome = input("Digite o nome do titular: ")

conta = ContaBancaria(nome)

# Menu do sistema
while True:

    print("\n=== SISTEMA BANCÁRIO ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Exibir saldo")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # Opção de depósito
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        conta.depositar(valor)

    # Opção de saque
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        conta.sacar(valor)

    # Opção para exibir saldo
    elif opcao == "3":
        conta.exibir_saldo()

    # Encerrar programa
    elif opcao == "4":
        print("Sistema encerrado.")
        break

    # Caso a opção seja inválida
    else:
        print("Opção inválida.")