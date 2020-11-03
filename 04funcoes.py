# indentação e formatação dos blocos

def teste():
    print(1)
    print(2)


teste()

if True:
    print(1)
else:
    print(2)

nome = "paulo"
sobrenome = "salvatore"
print("paulo".upper())
print("paulo".lower())
print(nome.capitalize())

nome_completo = nome + ' ' + sobrenome
print("total de caracteres do nome= ", len(nome_completo))

nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")
nome_completo = nome + ' ' + sobrenome
print(f"total de caracteres do nome {nome_completo.capitalize()} é ", len(nome_completo))

# 2ª forma
print("paulo".upper())
print("NOME EM MINÚSCULO".lower())

frase = "essa é uma frase".capitalize()
print(frase)

nome = "paulo".capitalize()
sobrenome = "salvatore".capitalize()

qtde_caracteres = len(nome) + len(sobrenome) + 1

print(f"{nome} {sobrenome} possui {qtde_caracteres} caracteres.")

frase_titulo = "texto qualquer frase".title()
print(frase_titulo)

# Para pegar a quantidade de caracteres, utilizamos o len()

# Capitalize -> Apenas a primeira letra da string maiúscula
# "paulo salvatore" vira "Paulo salvatore"
# "salvatore" vira "Salvatore"

# Title -> Todas as primeiras letras de cada palavra em uma frase viram maiúsculas
# "paulo salvatore" vira "Paulo Salvatore"

nome = "paulo".capitalize()
sobrenome = "salvatore".capitalize()

print(nome, len(nome))
print(sobrenome, len(sobrenome))

nome_completo = nome + " " + sobrenome

total = len(nome_completo)

print(nome_completo, total)