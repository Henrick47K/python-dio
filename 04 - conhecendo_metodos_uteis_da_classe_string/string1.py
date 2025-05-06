nome = "HenRiqUe"

print(nome.upper())
print(nome.lower())
print(nome.title())

# STRIP

texto = "  Olá, mundo!    "

print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

#CENTER

menu = "python"

print(menu.center(14, "#"))
print("-".join(menu))

for letra in menu:
    print(letra, end="-")