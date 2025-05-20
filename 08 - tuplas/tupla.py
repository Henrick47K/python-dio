# frutas = ("laranja", "pera", "uva", "maça")

# letras = tuple("python")
# print(letras)

# numeros = tuple([1, 2, 3,4])
# print(numeros)

# pais = ("Brasil",)
# print(pais)

# print(frutas[0]) # laranja
# print(frutas[2])

## TUPLAS NEGATIVAS

# print(frutas[-1]) # maça
# print(frutas[-3]) # pera

## TUPLAS ANINHADAS

## MATRIZ TUPLAS

# matriz = (
#     (1, "a", 2),
#     ("b", 3, 4),
#     (6, 5, "c"),
# )

# print(matriz[0]) # (1, "a", 2)
# print(matriz[0][0]) # 1
# print(matriz[0][-1]) # 2
# print(matriz[-1][-1]) # "c"

## FATIAMENTO

# tupla = ("p", "y", "t", "h", "o", "n")

# print(tupla[2:]) # ("t", "h", "o", "n")
# print(tupla[:2])
# print(tupla[1:3])
# print(tupla[0:3:2])
# print(tupla[::])
# print(tupla[::-1])

# carros = ("gol", "celta", "palio",)

# for carro in carros:
#     print(carro)

# for indice, carro in enumerate(carros):
#     print(f"{indice}: {carro}")

## COUNT

# cores = ("vermelho", "amarelo", "azul", "azul",)

# print(cores.count("vermelho"))
# print(cores.count("azul"))
# print(cores.count("amarelo"))

# linguagens = ("python", "js", "c", "java", "csharp")

# print(linguagens.index("java"))
# print(linguagens.index("python"))

# print(len(linguagens))

 carros = ("gol") 
print(isinstance(carros, tuple))