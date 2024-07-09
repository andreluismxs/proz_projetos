print("\nQuer descobrir que idade terá em 2022?")
print("Escolha uma das opções: ")
print("1 - Sim")
print("2 - Sair")

while True:
    try:
        escolha = int(input("Digite o número com base na opção escolhida: "))
        if escolha == 1:
            ano = int(input("Qual o ano que você nasceu? "))
            idade = 2022 - ano
            print(f"Sua idade será de {idade} anos em 2022!")
            break
        elif escolha == 2:
            print("O programa está sendo encerrado...")
            break
        else:
            print("A opção escolhida é inválida! Tente novamente.")
    except ValueError:
        print("A opção escolhida é inválida! Tente novamente.")

         

