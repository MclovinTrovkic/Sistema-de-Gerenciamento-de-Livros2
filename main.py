import menu
import adicionar
import exibir
import pesquisar
import marcar_emprestado
import remover

def main():
    biblioteca = []

    while True:
        escolha = menu.exibir_menu()

        try:
            if escolha == "1":
                adicionar.adicionar_livro(biblioteca)
            elif escolha == "2":
                exibir.exibir_livros(biblioteca)
            elif escolha == "3":
                pesquisar.pesquisar_livros(biblioteca)
            elif escolha == "4":
                marcar_emprestado.marcar_livro_emprestado(biblioteca)
            elif escolha == "5":
                remover.remover_livro(biblioteca)
            elif escolha == "6":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
    import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'biblioteca')))

    