from livro import Livro

livro_o_iluminado = Livro('O Iluminado', 'Stephen King', 1980)
livro_orgulho_e_preconceito = Livro('Orgulho e Preconceito', 'Jane Austin', 1850)
livro_dom_casmurro = Livro('Dom Casmurro', 'Machado de Assim', 1900)

livro_o_iluminado.emprestar()
livro_dom_casmurro.emprestar()
livro_o_iluminado.devolver()

ano_especifico = 1980
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")


def main():
    Livro.listar_livros()


if __name__ == '__main__':
    main()