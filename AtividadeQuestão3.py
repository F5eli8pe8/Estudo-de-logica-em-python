
print("Bem-vindos a Madeireira do Lenhador Valdenilson Felipe Souza Silva.") 

def escolha_tipo():
    while True:  # Laço para garantir escolha válida
        print("\n Tora de Pinho: PIN --- Tora de Peroba: PER --- Tora de Mogno: MOG --- Tora de Ipê: IPE --- Tora de Imbuia: IMB")
        tipo = input("\nEscolha o tipo de madeira (PIN, PER, MOG, IPE, IMB): ").upper()
        if tipo == "PIN":
            return 150.40  
        elif tipo == "PER":
            return 170.20  
        elif tipo == "MOG":
            return 190.90  
        elif tipo == "IPE":
            return 210.10  
        elif tipo == "IMB":
            return 220.70 
        else:
            print("Tipo de madeira inválido. Tente novamente.")  

# Função para definir a quantidade de toras e calcular o desconto
def qtd_toras():
    while True:
        try:
            quantidade = float(input("\nDigite a quantidade de toras (m³): "))
            if quantidade > 2000:
                print("Infelizmente não aceitamos pedidos dessa quantidade, tente novamente.")  
                continue
            elif quantidade >= 1000:
                return quantidade, 0.16 
            elif quantidade >= 500:
                return quantidade, 0.09  
            elif quantidade >= 100:
                return quantidade, 0.04  
            else:
                return quantidade, 0  
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

# Função para definir o transporte e retornar o valor
def transporte():
    while True:
        print("\nValor de transporte: Rodoviário:R$1000 -- Ferroviário:2000 -- Hidroviário: R$2500")
        opcao_transporte = input("\nEscolha o transporte: Rodoviário (1), Ferroviário (2), Hidroviário (3): ")
        if opcao_transporte == "1":
            return 1000  #
        elif opcao_transporte == "2":
            return 2000  
        elif opcao_transporte == "3":
            return 2500  
        else:
            print("Opção de transporte inválida. Tente novamente.")

# Função principal (main) onde o cálculo do total a pagar é realizado
def main():
   
    valor_madeira = escolha_tipo()

   
    quantidade, desconto = qtd_toras()

   
    valor_transporte = transporte()

    # Calculando o valor total
    total = ((valor_madeira * quantidade) * (1 - desconto)) + valor_transporte  # EXIGÊNCIA DE CÓDIGO 5 de 7
    print(f"\nO valor total do seu pedido é: R$ {total:.2f}")
    print("Obrigado por comprar!")
# Executando o programa principal
main()
