# range(stop) -> range object
# range(start, stop[step]) -> range object

# list(range(4))

# UTILIZANDO BULT IN RANGE COM FOR

# for numero in range(0, 11):
#     print(numero, end=" ")

# exibindo a tabuada do 5

# for numero in range(0,73,8 ):
#     print(numero, end=" ")

# WHILE

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Exibir Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando... ")
    elif opcao == 2:
        print("Exibindo o Extrato... ")
    else:
        print("Obrigado por usar nosso sistema bancário, até logo!")
