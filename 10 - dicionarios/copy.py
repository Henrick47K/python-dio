contatos = {
    "henrique@gmail.com": {"nome": "Henrique", "telefone": "3333-4545"}
}

copia = contatos.copy()
copia["henrique@gmail.com"] = {"nome": "rick"}

print(contatos["henrique@gmail.com"]) # {"nome": "Henrique", "telefone": "3333-4545"}

print(copia["henrique@gmail.com"]) # {"nome": "rick"}