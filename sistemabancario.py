# Variáveis Globais

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R${valor:.2f} realizado com sucesso")
    else:
        print("O valor do depósito deve ser maior que 0")

def sacar(valor):
    global saldo, extrato, numero_saques
    if valor > saldo:
        print(" Saldo insuficiente.")
    elif valor > limite:
        print(f" O limite máximo por saque é R$ {limite:.2f}.")
    elif numero_saques >= LIMITE_SAQUES:
        print(" Você já atingiu o limite de saques diários.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"  
        numero_saques += 1
        print(f" Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print(" O valor do saque deve ser positivo.")

    
def mostrar_extrato():
    global saldo, extrato
    print("\n====== EXTRATO ======")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=====================\n")

# Menu principal
def menu():
    while True:
        print("\n----- MENU -----")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ ").replace(",", "."))
            depositar(valor)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ ").replace(",", "."))
            sacar(valor)

        elif opcao == "3":
            mostrar_extrato()

        elif opcao == "0":
            print("👋 Saindo do sistema bancário...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

# Executa o programa
menu()