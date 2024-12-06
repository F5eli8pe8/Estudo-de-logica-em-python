print("Bem-Vindos a Pizzaria do Valdenilson Felipe Souza Silva")

print("________________________Cardapio________________________")
print("Tamanhos: P, M, G \n")
print("Pizzas Salgadas (PS):\n  P - R$30,  M - R$45,  G - R$60")
print("Pizzas Doces (PD):\n  P - R$34,  M - R$48,  G - R$66")

valorTotal = 0

while True:
     
    sabor = input("\nEscolha o sabor (PS para Pizza Salgada, PD para Pizza Doce): ").upper()  # coloquei o upper pra deixar as letras maiúsculas no momento de input
    if sabor != "PS" and sabor != "PD":                                                         
        print("Sabor inválido. Tente novamente.")  
        continue  

    
    tamanho = input("Escolha o tamanho (P, M, G): ").upper() #Aqui tambem, o input fica maiusculo automatico. 
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente.")  
        continue  


    if sabor == "PS":  # Pizza salgada
        if tamanho == "P":
            valor_pedido = 30
        elif tamanho == "M":
            valor_pedido = 45
        else:
            valor_pedido = 60
    elif sabor == "PD":  # Pizza doce
        if tamanho == "P":
            valor_pedido = 34
        elif tamanho == "M":
            valor_pedido = 48
        else:
            valor_pedido = 66

    # Adiciona o valor do pedido ao total
    valorTotal += valor_pedido 

   
    print(f"Você escolheu uma Pizza {('Salgada' if sabor == 'PS' else 'Doce')} tamanho {tamanho}. Valor: R$ {valor_pedido:.2f}")

    # Aqui pergunta se o cliente quer fazer mais algum pedido.
    mais_pedidos = input("Deseja pedir mais alguma coisa? (S/N): ").upper()  
    if mais_pedidos == "N":
        break  #Aqui o Break para sair do loop 


print(f"\nO valor total do seu pedido é: R$ {valorTotal:.2f}")# Coloquei 2f pra caso precise monstrar alguma casa decimal
print("Obrigado por comprar na Pizzaria do Valdenilson Felipe Souza Silva!")
