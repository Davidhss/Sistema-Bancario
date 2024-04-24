import textwrap

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor > limite:
            print(f"Limite de saque  = R${limite:.2f}")
        elif valor > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= valor
            numero_saques += 1
            print(f"Saldo atual: R$ {saldo:.2f}")
            extrato += f"Saque: R$ {valor:.2f}\n"
    else:
        print("Limite de Saques atingido!")

    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Saldo atual: {saldo:.2f}")
    else:
        print("Operação falhou, valor inválido!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(" Extrato ".center(21, "#"))
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("".center(21, "#"))

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado, processo de criação de conta encerrado.")
    return None

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("--" * 50)
        print(textwrap.dedent(linha))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número, bairro, cidade/sigla, estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n\nParabéns, o usuário criado com sucesso!")

def menu():
    menu = """
    Bem-Vindo ao David's Bank
    O que gostaria de fazer:

    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Nova conta
    5 - Listar contas
    6 - Novo usuário
    7 - Sair

    => """
    return input(textwrap.dedent(menu))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 0
    
    while True:
        opcao = menu()

        if opcao == "1":
            print("Depósito")

            valor_deposito = float(input("Valor: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)
        
        elif opcao == "2":
            if numero_saques < 3:
                print("Saque")

                valor_saque = float(input("Valor: "))
                saldo, extrato = sacar(saldo=saldo, extrato=extrato, valor=valor_saque, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            else:
                print("Limite de Saques atingido!")

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "5":
            listar_contas(contas)
        
        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "7":
            break

        else:
            print("Operação inválida, por favor, selecione novamente a operação desejada.")


main()