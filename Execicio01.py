# Exercicio 1 - "E os 10% do garçom?"
"""
Defina uma variável para o valor de uma refeição que custou R$ 42,54; Defina uma variável para o valor da taxa de
serviço que é de 10%; Defina uma variável que calcula o valor total da conta e exiba-o no console (sem formatação,
por enquanto, apenas o valor do resultado).
"""

conta = float(input("Digite o valor da conta:"))
taxa = float(input("Digite a taxa de serviço:"))

total = conta + (conta * taxa / 100)

print("Conta= %.2f R$" % conta)
print("Taxa= %.2f" % taxa, '''%''')
print("Total= %.2f R$" % total)

"""
2ª forma
valor_refeicao = 42.54
taxa_servico = 10

total_conta = valor_refeicao + valor_refeicao * 10 / 100

# print("R$ " + str(total_conta))

# Formatação

print(f"Sua refeição custou R$ {valor_refeicao}, mais a taxa de serviço de {taxa_servico}%.")
print(f"O valor total ficou de R$ {total_conta:.2f}.")

# Curiosidade, substituindo ponto de decimal por vírgula
total_com_virgula = f"R$ {total_conta:.2f}".replace(".", ",")
print(total_com_virgula)
"""


