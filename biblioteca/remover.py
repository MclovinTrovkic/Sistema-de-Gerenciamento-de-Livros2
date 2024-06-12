def remover_livro(biblioteca):
    titulo = input("Digite o título do livro a ser removido: ")

    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():
            biblioteca.remove(livro)
            print("Livro removido com sucesso!")
            return

    print("Livro não encontrado na biblioteca.")

# Testando a função
if __name__ == "__main__":
    biblioteca = [
        {"titulo": "Python for Beginners", "autor": "John Smith", "ano_publicacao": "2020", "status": "disponível"},
        {"titulo": "Introduction to Machine Learning", "autor": "Jane Doe", "ano_publicacao": "2019", "status": "disponível"},
    ]
    remover_livro(biblioteca)
    print("Biblioteca atualizada:", biblioteca)
