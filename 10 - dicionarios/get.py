contatos = {
    "henrique@gmail.com": {"nome": "Henrique", "telefone": "3333-2221"}
}

contatos["chave"] # KeyError

contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("henrique@gmail.com", {}) # {"henrique@gmail.com": {"nome": "Henrique", "telefone": "3333-2221"}}