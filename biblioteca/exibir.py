def exibir_livros(biblioteca):
    if not biblioteca:
        print("Nenhum livro cadastrado.")
    else:
        print("===== Livros Cadastrados =====")
        for i, livro in enumerate(biblioteca, start=1):
            print(f"{i}. Título: {livro['titulo']}, Autor: {livro['autor']}, Ano de Publicação: {livro['ano_publicacao']}, Status: {livro['status']}")
