# Definir as alíquotas de IR para CDB com base no número de dias investido
def calcular_aliquota_ir(dias_investidos):
    if dias_investidos <= 180:
        return 22.5 / 100
    elif dias_investidos <= 360:
        return 20 / 100
    elif dias_investidos <= 720:
        return 17.5 / 100
    else:
        return 15 / 100

# Solicitar informações do usuário
print("Tipos de Investimento:")
print("1 - CDB")
print("2 - LCI")
print("3 - LCA")

tipo_investimento = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

# Validar tipo de investimento
if tipo_investimento not in [1, 2, 3]:
    print("Investimento inválido! Por favor, escolha 1 para CDB, 2 para LCI ou 3 para LCA.")
else:
    valor_resgate = float(input("Digite o valor a ser resgatado: R$ "))
    dias_investidos = int(input("Digite o número de dias que o valor permaneceu investido: "))

    # Cálculo para CDB
    if tipo_investimento == 1:
        aliquota = calcular_aliquota_ir(dias_investidos)
        valor_ir = valor_resgate * aliquota
        valor_liquido = valor_resgate - valor_ir
        print("\nResumo do Resgate - CDB")
        print(f"Valor Resgatado: R$ {valor_resgate:.2f}")
        print(f"Alíquota de IR: {aliquota * 100:.1f}%")
        print(f"Valor do Imposto de Renda (IR): R$ {valor_ir:.2f}")
        print(f"Valor Líquido após IR: R$ {valor_liquido:.2f}")

    # Cálculo para LCI e LCA (isentos de IR)
    elif tipo_investimento == 2 or tipo_investimento == 3:
        print("\nResumo do Resgate - LCI/LCA (Isento de IR)")
        print(f"Valor Resgatado: R$ {valor_resgate:.2f}")
        print("Este investimento é isento de Imposto de Renda.")
