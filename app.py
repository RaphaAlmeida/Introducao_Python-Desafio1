'''Nesse desafio desenvolveremos uma agenda para salvar, editar, deletar e marcar um contato como 
favorito. O resultado da aplicação deve ser apresentado no terminal, 
assim como foi visto no módulo “Introdução ao Python”'''

def view_contatos(_agenda):
    '''Tem a função de mostrar as informações dos contatos que estão na lista'''
    for indice,_contato in enumerate(_agenda):
        print(f"\n- Informaões do Contato #{indice+1}: \nNome: {_contato['Nome']}"
              f"\nTelefone: {_contato['Telefone']}\nEmail: {_contato['Email']}"
              f"\nFavorito: {_contato['Favorito']}"
        )



def add_contato(_agenda, _nome_contato, _tel, _email, _favorito):
    '''Função para add um novo contato na agenda: 
    (nome, telefone, email, favorito (para marcar o contato como favorito))'''
    status = "[✓]" if _favorito == "S" else "[ ]"
    contato = {
        "Nome": _nome_contato, 
        "Telefone": _tel, 
        "Email": _email, 
        "Favorito": status
        }

    _agenda.append(contato) # Add os contatos com o append
    print(f"O contato {nome_contato} foi adicionado a sua agenda") # escrevendo

def edit_contatos(_agenda, _nome_contato, _tel, _email, _favorito, _edit_choice):
    '''Função para editar um contato na agenda: 
    (nome, telefone, email, favorito (para marcar o contato como favorito))'''
    edit_status = "[✓]" if _favorito == "S" else "[ ]"
    _agenda[_edit_choice-1] = {
        "Nome": _nome_contato, 
        "Telefone": _tel, 
        "Email": _email, 
        "Favorito": edit_status
    }

def del_contatos(_agenda, _edit_choice):
    '''Função para apagar um contato da agenda'''
    _agenda.pop(_edit_choice - 1)
    return print("\nO contato foi apagado")

def fav_contatos(_agenda, _favorito):
    '''Função para alterar o contato como favorito'''
    _agenda[_favorito - 1]["Favorito"] = "[✓]"
    _nome_contato = _agenda[_favorito - 1]["Nome"]
    return print(f"\nO contato {_nome_contato} foi marcado como favorito")

agenda = []

valid_choice = ["1", "2", "3", "4", "5"]

while True:
    try:
        print("\n***Agenda de Contatos***\n")
        view_contatos(agenda)
        print("\n1. Salvar um novo contato")
        print("2. Editar um contato salvo")
        print("3. Apagar um contato salvo")
        print("4. Marque um contato como seu favorito")
        print("5. Fechar a agenda")
        
        # Escolha do User
        choice = input("\nDigite o número da opção: ")

        if choice not in valid_choice:
            raise ValueError("\nOpção inválida, por favor escolha uma opção válida")

        if choice == "1":
            nome_contato = input("Nome do Contato: ")
            tel = input("Telefone: ")
            email = input("Email:")
            while True:
                favorito = input("\nSalvar contato como favorito? (S/N): ").upper()
                if favorito in {"S", "N"}: # Simplificando o if valor1 or valor2
                    break
                print(f"Você digitou {favorito}, use apenas 'S' ou 'N'")
            add_contato(agenda,nome_contato, tel, email, favorito)

        elif choice == "2": # Editar um contato salvo
            edit_choice = int(input("Digite o numero do contato que gostaria de editar: "))
            nome_contato = input("Nome do Contato: ")
            tel = input("Telefone: ")
            email = input("Email:")
            while True:
                favorito = input("\nSalvar contato como favorito? (S/N): ").upper()
                if favorito in {"S", "N"}: # Simplificando o if valor1 or valor2
                    break
                print(f"Você digitou {favorito}, use apenas 'S' ou 'N'")
            edit_contatos(agenda,nome_contato, tel, email, favorito, edit_choice)

        elif choice == "3": # Apagar contato
            edit_choice = int(input("Digite o número do contato que gostaria de apagar: "))
            del_contatos(agenda, edit_choice)

        elif choice == "4": # Marcar um contato como favorito
            while True:
                favorito = int(input("\nDigite o número do contato que deseja salvar como favorito: "))
                if agenda[favorito - 1]["Favorito"] == "[✓]": # Simplificando o if valor1 or valor2
                    print("O contato selecionado já esta marcado como favorito, escolha um contato válido")
                else:
                    break
            fav_contatos(agenda, favorito)

        elif choice == "5":
            break

    except ValueError as e:
        print(e)
print("Programa Finalizado")
