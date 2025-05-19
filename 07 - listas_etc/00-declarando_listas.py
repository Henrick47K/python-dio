# frutas = ["Laranja", "maca", "uva"]
# print(frutas)

# frutas = []
# print(frutas)

# letras = list("python")
# print(letras)

# numeros = list(range(10))
# print(numeros)

# carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

# frutas = ["maça", "laranja", "uva", "pera"]
# print(frutas[0]) #maça
# print(frutas[3]) #pera

# LISTAS NEGATIVAS

# frutas = ["maça", "laranja", "uva", "pera"]
# print(frutas[-1]) # pera
# print(frutas[-3]) # laranja

# LISTAS ANINHADAS

# matriz = [
#     [1, "a", 2],
#     ["b", 3, 4],
#     [6, 5, "c"]
# ]

# print(matriz[0]) # [1, "a", 2]
# print(matriz[0][0]) # 1
# print(matriz[0][-1]) # 2
# print(matriz[-1][-1]) # "c"
# print(matriz[1])

# FATIAMENTO

# lista = ["p", "y", "t", "h", "o", "n"]

# print(lista[2:])
# print(lista[:2])
# print(lista[1:3])
# print(lista[0:3:2])
# print(lista[::])
# print(lista[::-1])

# ITERAR LISTAS

# carros = ["gol", "celta", "palio"]

# for carro in carros:
#     print(carro)

# FUNÇÃO ENUMERATE

# carros = ["gol", "celta", "palio"]

# for indice, carro in enumerate(carros):
#     print(f"{indice}: {carro}")

# times = ["arsenal", "psg", "barcelona", "inter"]

# for indice, time in enumerate(times):
#     print(f"{indice}: {time}")

# LISTA COMPREENSAO

numeros = [1, 2, 30, 21, 2, 9, 65, 34]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    elif numero % 2 == 1:
        impares.append(numero)

print(pares)
print(impares)

# LISTA FILTRO 2 

numeros = [1, 2, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)