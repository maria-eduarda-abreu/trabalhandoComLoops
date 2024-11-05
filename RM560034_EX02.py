# Solicita o valor do carro ao usuário
valor_carro = float(input("Digite o valor do carro: R$ "))

# Calcula o preço à vista com 20% de desconto
preco_vista = valor_carro * 0.8

# Define os acréscimos para cada quantidade de parcelas
tabela_acrescimos = {
    6: 3,
    12: 6,
    18: 9,
    24: 12,
    30: 15,
    36: 18,
    42: 21,
    48: 24,
    54: 27,
    60: 30
}

# Imprime a tabela de preços
print("\nTabela de preços:")
print(f"{'Quantidade de Parcelas':<25} {'Preço Final (R$)':<20} {'Valor da Parcela (R$)':<20}")

# Preço à vista
print(f"{'À vista':<25} {preco_vista:<20.2f} {'N/A':<20}")

# Calcula e imprime os preços para cada quantidade de parcelas
for parcelas, acrescimo in tabela_acrescimos.items():
    preco_final = valor_carro * (1 + acrescimo / 100)  # Aplica o acréscimo ao valor inicial
    valor_parcela = preco_final / parcelas  # Calcula o valor de cada parcela
    print(f"{parcelas:<25} {preco_final:<20.2f} {valor_parcela:<20.2f}")
