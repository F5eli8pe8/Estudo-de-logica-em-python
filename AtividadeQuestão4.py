
print("Bem vindos a lista de contatos do Valdenilson Felipe Souza Silva")


lista_contatos = []
id_global = 4963097   # Substitui pelo meu RU

# Essa função é para cadastrar um contato
def cadastrar_contato(id_):
    
    nome = input("\nInforme o nome do contato: ")
    atividade = input("Informe a atividade do contato: ")
    telefone = input("Informe o telefone do contato: ")
    

    contato = {
        "id": id_,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }
    
    lista_contatos.append(contato.copy())
    print(f"Contato {nome} cadastrado com sucesso!")

# Função para consultar contatos
def consultar_contatos():
    while True:
        print("\nConsulta de Contatos:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Atividade")
        print("4. Retornar ao menu principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            # Aqui podemos ver todos os contatos
            print("\nLista de Todos os Contatos:")
            for contato in lista_contatos:
                print(f"ID: {contato['id']}, Nome: {contato['nome']}, Atividade: {contato['atividade']}, Telefone: {contato['telefone']}")
        
        elif opcao == "2":
            # Consultar por ID
            id_ = int(input("Informe o ID do contato: "))
            encontrado = False
            for contato in lista_contatos:
                if contato["id"] == id_:
                    print(f"\nContato foi encontrado!: ID: {contato['id']}, Nome: {contato['nome']}, Atividade: {contato['atividade']}, Telefone: {contato['telefone']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Contato não encontrado.")
        
        elif opcao == "3":
            # Consultar por Atividade
            atividade = input("Digite a atividade: ")
            encontrados = [contato for contato in lista_contatos if contato["atividade"].lower() == atividade.lower()]
            
            if encontrados:
                print(f"\nContatos foi encontrado! '{atividade}':")
                for contato in encontrados:
                    print(f"ID: {contato['id']}, Nome: {contato['nome']}, Telefone: {contato['telefone']}")
            else:
                print("Nenhum contato encontrado com essa atividade.")
        
        elif opcao == "4":
            # Retorna ao menu principal
            return
        else:
            print("Opção inválida. Tente novamente.")

# Função para remover um contato
def remover_contato():
    while True:
        id_ = int(input("\nInforme o ID do contato a ser removido: "))
        contato_removido = None
        for contato in lista_contatos:
            if contato["id"] == id_:
                contato_removido = contato
                break
        
        if contato_removido:
            lista_contatos.remove(contato_removido)
            print(f"Contato de ID {id_} removido com sucesso!")
            break
        else:
            print("Id inválido. Tente novamente.")


def main():
    global id_global  
    
    while True:
        print("\nMenu Principal:")
        print("1. Cadastrar Contato")
        print("2. Consultar Contato")
        print("3. Remover Contato")
        print("4. Encerrar Programa")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            
            id_global += 1
            cadastrar_contato(id_global)
        
        elif opcao == "2":
            
            consultar_contatos()
        
        elif opcao == "3":
            
            remover_contato()
        
        elif opcao == "4":
            
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")


main()
