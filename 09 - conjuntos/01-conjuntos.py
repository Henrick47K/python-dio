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

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

a = conjunto_a.issubset(conjunto_b) # True
b = conjunto_b.issubset(conjunto_a) # False

print(a)
print(b)