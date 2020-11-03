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
