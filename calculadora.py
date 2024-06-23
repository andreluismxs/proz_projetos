def calculadora(numero1, numero2, escolha):
  if escolha == 1:
    return numero1 + numero2
  elif escolha == 2:
    return numero1 - numero2
  elif escolha == 3:
    return numero1 * numero2
  elif escolha == 4:
    return numero1 / numero2
  else:
    return 0
  
  escolha1 = calculadora(20, 4, 1)
  escolha2 = calculadora(20, 4, 2)
  escolha3 = calculadora(20, 4, 3)
  escolha4 = calculadora(20, 4, 4)
  escolha5 = calculadora(20, 4, 5)

  print(escolha1)
  print(escolha2)
  print(escolha3)
  print(escolha4)
  print(escolha5)
  
  
