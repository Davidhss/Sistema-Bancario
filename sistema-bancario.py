# Deve ser possível depositar valores positivos para a conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato

# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato

# O extrato lista todos os depósitos e saques realizados na conta. no fim da listagem deve ser exibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ xxx.xx

menu = """
Bem-Vindo ao David's Bank
O que gostaria de fazer:

1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("Depósito")

        valor_deposito = float(input("Valor: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Saldo atual: {saldo:.2f}")
        else:
            print("Operação falhou, valor inválido!")
        
    elif opcao == 2:
        if numero_saques < 3:
            print("Saque")

            valor_saque = float(input("Valor: "))
        
            if valor_saque > limite:
                print(f"Limite de saque  = R${limite:.2f}")
            elif valor_saque > saldo:
                print("Saldo insuficiente!")
            else:
                saldo -= valor_saque
                numero_saques += 1
                print(f"Saldo atual: R$ {saldo:.2f}")
                extrato += f"Saque: R$ {valor_saque:.2f}\n"

        else:
            print("Limite de Saques atingido!")

    elif opcao == 3:
        print(" Extrato ".center(21, "#"))
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("".center(21, "#"))
    elif opcao == 4:
        break
    else:
        print("Operação inválida, por favor, selecione novamente a operação desejada.")