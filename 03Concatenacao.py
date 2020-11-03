# Exercicio 1 - "E os 10% do garçom?"
"""
Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% de comissão para o garçom. Crie um
algoritmo em PYTHON que leia o valor gasto com despesas realizadas em um restaurante e imprima o valor da gorjeta e o
valor total com a gorjeta.
"""

conta = float(input("Digite o valor da conta:"))
taxa = float(input("Digite a taxa de serviço:"))

total = conta + (conta * taxa / 100)
total_com_virgula = f"{total:.2f}R$".replace(".", ",") # format de "." para virgula

print("Conta= %.2f R$" % conta)
print("Taxa= %.2f" % taxa, '''%''')
print("Total= %.2f R$" % total)
print("total= " + str(total) + "R$")
print("Total=", total_com_virgula)

# Formatação

valor_refeicao = 42.54
taxa_servico = 10

total_conta = valor_refeicao + valor_refeicao * 10 / 100

print(f"Sua refeição custou R$ {valor_refeicao}, mais a taxa de serviço de {taxa_servico}%.")
print(f"O valor total ficou de R$ {total_conta:.2f}.")

# Curiosidade, substituindo ponto de decimal por vírgula
total_com_virgula = f"R$ {total_conta:.2f}".replace(".", ",")
print(total_com_virgula)