# saldo = 1000
# saque = 200
# limite = 100

# print(saldo >= saque)

# print(saque <= limite)

# OPERADOR E
 # (saldo >= saque and saque <= limite)
    # False

# OPERADOR OU

# print (saldo >= saque or saque <= limite)
# True

# OPERADOR NOT

# contatos_emergencia = []

# print(not 1000 > 1500)

# print(not contatos_emergencia)

# print(not "saque 1500;")

# print(not "")

saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))



