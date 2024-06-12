def adicionar_livro(biblioteca):
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    ano_publicacao = input("Digite o ano de publicação: ")
    status = "disponível"

    livro = {"titulo": titulo, "autor": autor, "ano_publicacao": ano_publicacao, "status": status}
    biblioteca.append(livro)

    print("Livro adicionado com sucesso!")
