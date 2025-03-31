from os import system

# Variáveis globais
saldo = 0
LIMITE_QTDE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500
extrato = []
numero_saques = 0
usuarios = []
contas = []
numero_conta_sequencial = 1

def depositar(saldo, valor, extrato, /):
    system("cls")
    print("================ DEPÓSITO =================")
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    input("\nPressione qualquer tecla para continuar...")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    system("cls")
    print("================ SAQUE =================")
    if numero_saques < limite_saques:
        if valor <= limite:
            if valor <= saldo:
                saldo -= valor
                extrato.append(f"Saque: R$ {valor:.2f}")
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente.")
        else:
            print(f"Limite de saque excedido. O limite é de R$ {limite:.2f} por saque.")
    else:
        print("Limite diário de saques atingido.")
    input("\nPressione qualquer tecla para continuar...")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    system("cls")
    print("================ EXTRATO =================")
    if extrato:
        print("Extrato:")
        for movimento in extrato:
            print(movimento)
        print(f"Saldo: R$ {saldo:.2f}")
    else:
        print("Não foram realizadas movimentações.")
    input("\nPressione qualquer tecla para continuar...")

def criar_usuario(usuarios):
    system("cls")
    print("================ CRIAR USUÁRIO =================")
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    cpf = input("CPF (somente números): ")
    endereco = input("Endereço (logradouro, número, bairro, cidade/sigla estado): ")

    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("CPF já cadastrado!")
            input("\nPressione qualquer tecla para continuar...")
            return usuarios

    # Adiciona o novo usuário à lista
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")
    input("\nPressione qualquer tecla para continuar...")
    return usuarios

def criar_conta_corrente(contas, usuarios, numero_conta_sequencial):
    system("cls")
    print("================ CRIAR CONTA CORRENTE =================")
    cpf = input("CPF do usuário: ")

    # Verifica se o usuário existe
    usuario = None
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
            break

    if usuario is None:
        print("Usuário não encontrado!")
        input("\nPressione qualquer tecla para continuar...")
        return contas, numero_conta_sequencial

    # Cria a nova conta corrente
    conta = {"agencia": "0001", "numero_conta": numero_conta_sequencial, "usuario": usuario}
    contas.append(conta)
    numero_conta_sequencial += 1
    print("Conta corrente criada com sucesso!")
    input("\nPressione qualquer tecla para continuar...")
    return contas, numero_conta_sequencial

def listar_contas(contas):
    system("cls")
    print("================ LISTAR CONTAS =================")
    if contas:
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}")
    else:
        print("Nenhuma conta encontrada.")
    input("\nPressione qualquer tecla para continuar...")

def menu():
    global saldo, extrato, numero_saques, usuarios, contas, numero_conta_sequencial
    while True:
        system("cls")
        print("\nEscolha a operação:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Criar Usuário")
        print("5 - Criar Conta Corrente")
        print("6 - Listar Contas")
        print("7 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            valor_deposito = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)
        elif opcao == "2":
            valor_saque = float(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor_saque, extrato=extrato, limite=LIMITE_VALOR_SAQUE, numero_saques=numero_saques, limite_saques=LIMITE_QTDE_SAQUES)
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            usuarios = criar_usuario(usuarios)
        elif opcao == "5":
            contas, numero_conta_sequencial = criar_conta_corrente(contas, usuarios, numero_conta_sequencial)
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "7":
            break
        else:
            print("Opção inválida.")
            input("\nPressione qualquer tecla para continuar...")

    print("Sistema encerrado.")

# Executa o menu principal
menu()
