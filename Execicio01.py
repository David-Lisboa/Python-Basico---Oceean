# Exercicio 1 - "E os 10% do garçom?"
"""
Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% de comissão para o garçom. Crie um
algoritmo em PYTHON que leia o valor gasto com despesas realizadas em um restaurante e imprima o valor da gorjeta e o
valor total com a gorjeta.
"""

conta = float(input("Digite o valor da conta:"))
taxa = float(input("Digite a taxa de serviço:"))

total = conta + (conta * taxa / 100)

print("Conta= %.2f R$" % conta)
print("Taxa= %.2f" % taxa, '''%''')
print("Total= %.2f R$" % total)


