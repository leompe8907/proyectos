frase = input("diga una frase: ")
contar = 0
for i in frase:
    if i != " ":
        contar += 1

print(f"tu frase tiene {contar} letras")
        