# Solicita o valor da dívida ao usuário
valor_divida = float(input("Digite o valor da dívida: R$ "))

# Define os juros para cada quantidade de parcelas
tabela_juros = {
    1: 0,
    3: 10,
    6: 15,
    9: 20,
    12: 25
}

# Imprime o cabeçalho da tabela
print("\nTabela de pagamento:")
print(f"{'Valor da Dívida (R$)':<20} {'Valor do Juros (R$)':<20} {'Quantidade de Parcelas':<25} {'Valor da Parcela (R$)':<20}")

# Calcula e imprime os valores para cada quantidade de parcelas
for parcelas, juros in tabela_juros.items():
    valor_juros = valor_divida * (juros / 100)  # Calcula o valor dos juros
    valor_total = valor_divida + valor_juros  # Calcula o valor total da dívida com juros
    valor_parcela = valor_total / parcelas  # Calcula o valor de cada parcela
    print(f"{valor_total:<20.2f} {valor_juros:<20.2f} {parcelas:<25} {valor_parcela:<20.2f}")

