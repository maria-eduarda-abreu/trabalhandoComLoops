# armazenamento da quantidade de votos
votos = {
    "segunda-feira": 0,
    "terça-feira": 0,
    "quarta-feira": 0,
    "quinta-feira": 0,
    "sexta-feira": 0
}

# Entrada de dados da quantidade de colaboradores que irão participar da votação
quantidade_colaboradores = int(input("Qual é a quantidade de colaboradores: "))

# Coleta de votos
for i in range(0, quantidade_colaboradores):
    print("1 - segunda-feira")
    print("2 - terça-feira")
    print("3 - quarta-feira")
    print("4 - quinta-feira")
    print("5 - sexta-feira")
    # Recebe a entrada do usuário e converte em um valor numérico
    opcao = int(input("Informe o número correspondente ao dia de sua preferência: "))
    
    # Mapeamento do número escolhido para o dia da semana no dicionário `votos`
    if opcao == 1:
        votos["segunda-feira"] += 1
    elif opcao == 2:
        votos["terça-feira"] += 1
    elif opcao == 3:
        votos["quarta-feira"] += 1
    elif opcao == 4:
        votos["quinta-feira"] += 1
    elif opcao == 5:
        votos["sexta-feira"] += 1
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 5.")

 ##Se houver mais de um dia com o mesmo número máximo de votos, há um empate
    if len(dias_com_max_votos) > 1:
        print("Ops! A votação empatou. Refazendo a votação...\n")
        # Reinicia os votos para refazer a votação
        votos = {dia: 0 for dia in votos}
        continue  # Reinicia o loop para nova votação
    else:
        # Identifica o dia mais votado usando a função `max` e a chave `votos.get`
        dia_mais_votado = max(votos, key=votos.get)
        # Exibe o resultado e sai do loop
        print("O dia escolhido pelos colaboradores é:", dia_mais_votado)
        break  # Sai do loop se não houve empate
