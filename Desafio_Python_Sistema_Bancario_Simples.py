from os import system

saldo = 0
LIMITE_QTDE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500
extrato = []

def depositar():
    global saldo, extrato
    system("cls")
    print("================ DEPÓSTIO =================")
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    input("\nPressione qualquer teclado para continuar...")

def sacar():
    global saldo, LIMITE_QTDE_SAQUES, extrato
    system("cls")
    print("================ SAQUE =================")
    valor = float(input("Digite o valor do saque: "))
    if LIMITE_QTDE_SAQUES > 0:
        if valor <= LIMITE_VALOR_SAQUE:
            if valor <= saldo:
                saldo -= valor
                extrato.append(f"Saque: R$ {valor:.2f}")
                LIMITE_QTDE_SAQUES -= 1
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente.")
        else:
            print(f"Limite de saque excedido. O limite é de R$ {LIMITE_VALOR_SAQUE:.2f} por saque.")
    else:
        print("Limite diário de saques atingido.")
    input("\nPressione qualquer teclado para continuar...")

def exibir_extrato():
    global saldo, extrato
    system("cls")
    print("================ EXTRATO =================")
    if extrato:
        print("Extrato:")
        for movimento in extrato:
            print(movimento)
        print(f"Saldo: R$ {saldo:.2f}")
    else:
        print("Não foram realizadas movimentações.")
    input("\nPressione qualquer teclado para continuar...")

while True:
    system("cls")
    print("\nEscolha a operação:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        depositar()
    elif opcao == "2":
        sacar()
    elif opcao == "3":
        exibir_extrato()
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")

print("Sistema encerrado.")