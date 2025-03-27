# saldo = 2000.0
# saque = float(input("Informe o valor do saque: "))
# restante = ""

# if saldo >= saque:
#     restante = (saldo - saque)
#     print("Realizando saque!")
#     print(f"saldo atual:", restante)

# if saldo <= saque:
#     print("Saldo insuficiente!")

## ESTRUTURA ELSE

# saldo = 2000.0
# saque = float(input("Informe o valor do saque: "))
# restante = ""

# if saldo >= saque:
#     print("Realizando saque...")
#     restante = (saldo - saque)
#     print(f"Saldo Atual:", restante)
# else:
#     print("Saldo insuficeinte!")

## ESTRUTURA ELIF

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato ...")
else:
    sys.exit("opção inválida")

