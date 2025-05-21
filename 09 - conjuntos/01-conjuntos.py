# set[(1, 2, 3, 1, 3, 4)] # {1, 2, 3, 4}

# set("abacaxi") # {"b", "a", "c", "x", "i"}

# set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}

# linguagens = {"python", "java", "python"}
# print(linguagens)

## CONVERTENDO SET PARA LISTA  

# numeros = {1, 2, 3, 2}

# numeros = list(numeros)

# print(numeros[0])

## FOR 

# carros = {"palio", "chevrolet", "mitsubishi"}

# for carro in carros:
#     print(carro)

## FUNÇÃO ENUMERATE

# for indice, carro in enumerate(carros):
#     print(f"{indice}: {carro}")

## RECURSOS SET {}.UNION

# conjunto_a = {1, 2}
# conjunto_b = {3, 4}

# resultado = conjunto_a.union(conjunto_b) # {1, 2, 3, 4}
# print(resultado)

## {}.INTERSECTION

# conjunto_a = {1, 2, 3}
# conjunto_b = {2, 3, 4}

# resultado = conjunto_a.intersection(conjunto_b)
# print(resultado)

## {}. DIFFERENCE

# conjunto_a = {1, 2, 3} # {1}
# conjunto_b = {2, 3, 4} # {4}

# a = conjunto_a.difference(conjunto_b)
# b = conjunto_b.difference(conjunto_a)

# print(a)
# print(b)

# conjunto_a = {1, 2, 3}
# conjunto_b = {2, 3, 4}

# resultado = conjunto_a.symmetric_difference(conjunto_b) # {1, 4}
# print(resultado)

## {}.ISSUBSET

# conjunto_a = {1, 2, 3}
# conjunto_b = {4, 1, 2, 5, 6, 3}

# a = conjunto_a.issubset(conjunto_b) # True
# b = conjunto_b.issubset(conjunto_a) # False

# print(a)
# print(b)

## {}.ISDISJOINT

# conjunto_a = {1, 2, 3, 4, 5}
# conjunto_b = {6, 7, 8, 9}
# conjunto_c = {1, 0}

# resultado1 = conjunto_a.isdisjoint(conjunto_b) # True
# resultado2 = conjunto_a.isdisjoint(conjunto_c) # False

# print(resultado1)
# print(resultado2)

## {}.ADD

# sorteio = {1, 23}

# sorteio.add(25) # {1, 23, 25}
# sorteio.add(42) # {1, 23, 25, 42}
# sorteio.add(25) # {1, 23, 25, 42}

# print(sorteio)

## CLEAR

# sorteio = {1, 23}
# print(sorteio)
# sorteio # {1, 23}
# sorteio.clear()
# print(sorteio)
# sorteio # {}

## COPY
# print(sorteio)
# sorteio # {1, 23}
# sorteio.copy()
# print(sorteio)

# {}.DISCARD

# numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# numeros #{1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
# numeros.discard(1)
# print(numeros)
# numeros.discard(45)
# print(numeros)
# numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}

# numeros =  {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# numeros # {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
# numeros.pop() # 0
# numeros.pop() # 1
# print(numeros)
# numeros # {2, 3, 4, 5, 6, 7, 8, 9}

## {}.REMOVE

# numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# numeros.remove(0)
# print(numeros)
# numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9}

## LEN

# numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# quantidade = len(numeros) # 10
# print(quantidade)

## IN

# numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# a = 1 in numeros # True
# b = 10 in numeros # False

# print(a)
# print(b)