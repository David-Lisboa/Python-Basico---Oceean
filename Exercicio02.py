# Exercício 2: "Quem é você?" - Interação com o usuário, tipos de variáveis e operações matemáticas
from turtledemo.chaos import f

nome = input("Digite o seu nome: ").title()
idade = int(input("Digite a sua idade: "))
genero = input("Digite o seu genero: ").title()

if idade < 2:
    ano = "ano"
else:
    ano = "anos"

print(f"Olá {nome}, você possui {idade} {ano} e é do genero {genero}.")
print(f"Já pensou no que você fara no seu aniversario de {idade+1} anos?")

