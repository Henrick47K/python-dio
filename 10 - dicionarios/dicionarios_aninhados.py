contatos = {
    "henrique@gmail.com": {"nome": "Henrique", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melanine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a":1}},
}

print(contatos["giovanna@gmail.com"]["telefone"]) #3443-2121

extra = contatos["melanine@gmail.com"]["extra"]["a"]

print(extra)