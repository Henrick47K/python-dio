MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("informe seu ano de nascimento: "))

## APENAS IF
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH. ")

## COM ELSE
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
else:
    print("Ainda não pode tirar a CNH.")

##COM ELIF
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")