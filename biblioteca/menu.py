def exibir_menu():
    print("===== Menu Principal =====")
    print("1. Adicionar Livro")
    print("2. Exibir Livros")
    print("3. Pesquisar Livros")
    print("4. Marcar Livro como Emprestado")
    print("5. Remover Livro")
    print("6. Sair")

    while True:
        opcao = input("Escolha uma opção: ")
        if opcao.isdigit() and 1 <= int(opcao) <= 6:
            return opcao
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 6.")

