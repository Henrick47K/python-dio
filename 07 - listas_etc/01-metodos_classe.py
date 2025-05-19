# lista = []

# lista.append(1)
# lista.append("Python")
# lista.append([40, 30, 20])

# print(lista)

## []. CLEAR

# lista = [1, "Python", [40, 30, 20]]

# print(lista) # [1, "Python", [40, 30, 20]]

# lista.clear()

# print(lista)

## []. COPY

# lista = [1, "Python", [40, 30, 20]]

# l2 = lista.copy()

# print(id(l2), id(lista))

# l2[0] = 2

# print(l2)
# print(lista)

## []. COUNT

# cores = ["vermelho", "azul", "amarelo", "verde"]

# print(cores.count("vermelho"))
# print(cores.count("amarelo"))
# print(cores.count("laranja"))

## [].EXTEND

# linguagens = ["Python", "Java", "C"]
# print(linguagens)

# linguagens.extend(["PHP", "Swift"])
# print(linguagens)

## [].INDEX

# linguagens = ["Python", "Java", "C", "JS", "Kotlin"]
# print(linguagens.index("Python"))
# # print(linguagens.index("C"))

## [].POP

# linguagens = ["python", "js", "c", "java", "csharp"]

# linguagens.pop()
# linguagens.pop()
# linguagens.pop(0)

# print(linguagens)

## [].REMOVE

# linguagens = ["Java", "Swift", "C", "Python", "Go"]

# linguagens.remove("C")

# print(linguagens)

## [].REVERSE

# linguagens = ["Java", "Swift", "C", "Python", "Go"]

# linguagens.reverse()

# print(linguagens)

## [].SORT

# linguagens = ["java", "swift", "c", "python", "go", "csharp"]
# linguagens.sort()
# print(linguagens)

# linguagens.sort(reverse=True)
# print(linguagens)

# linguagens.sort(key=lambda x: len(x))
# print(linguagens)

# linguagens.sort(key=lambda x: (x), reverse=True)
# print(linguagens)

## LEN

# linguagens = ["java", "swift", "c", "python", "go", "csharp"]

# print(len(linguagens))

## SORTED

linguagens = ["java", "swift", "c", "python", "go", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))

print(sorted(linguagens, key=lambda x: len(x), reverse=True))