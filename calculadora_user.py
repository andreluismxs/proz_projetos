def calculadora_user():
    while True:
        print("\nOlá, qual operação você quer utilizar? (Digite o número correspondente)")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        try:
            escolha = int(input("Digite o número com base na operação escolhida: "))
        except ValueError:
            print("A opção escolhida é inválida! Tente novamente.")
            continue

        if escolha == 0:
            print("Programa encerrado!")
            break
        elif escolha in {1, 2, 3, 4}:
            try:
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Opção inválida. Por favor, digite um número válido.") 
                continue

            if escolha == 1:    
                resultado = numero1 + numero2
                print(f"O resultado da operação é: {resultado}")
            elif escolha == 2:
                resultado = numero1 - numero2
                print(f"O resultado da operação é: {resultado}")
            elif escolha == 3:
                resultado = numero1 * numero2
                print(f"O resultado da operação é: {resultado}")
            elif escolha == 4:
                if numero2 != 0:
                    resultado = numero1 / numero2
                    print(f"O resultado da operação é: {resultado}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("O número escolhido é inválido, pois não se refere a nenhuma operação.")

calculadora_user()


