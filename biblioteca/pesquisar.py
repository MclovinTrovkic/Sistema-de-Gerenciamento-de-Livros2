def pesquisar_livros(biblioteca):
    termo = input("Digite o título ou autor do livro a ser pesquisado: ")
    resultados = []

    for livro in biblioteca:
        if termo.lower() in livro['titulo'].lower() or termo.lower() in livro['autor'].lower():
            resultados.append(livro)

    if not resultados:
        print("Nenhum livro encontrado com o termo de pesquisa fornecido.")
    else:
        print("===== Resultados da Pesquisa =====")
        for i, livro in enumerate(resultados, start=1):
            print(f"{i}. Título: {livro['titulo']}, Autor: {livro['autor']}, Ano de Publicação: {livro['ano_publicacao']}, Status: {livro['status']}")

# Testando a função
if __name__ == "__main__":
    biblioteca = [
        {"titulo": "Python for Beginners", "autor": "John Smith", "ano_publicacao": "2020", "status": "disponível"},
        {"titulo": "Introduction to Machine Learning", "autor": "Jane Doe", "ano_publicacao": "2019", "status": "disponível"},
    ]
    pesquisar_livros(biblioteca)