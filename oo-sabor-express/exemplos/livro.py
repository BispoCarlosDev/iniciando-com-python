class Livro:
     
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | {self._disponivel}'

    @classmethod
    def listar_livros(cls):
        print(f'{'Título do Livro'.ljust(25)} | {'Autor'.ljust(25)} | {'Ano Publicação'.ljust(25)} | Status')
        for livro in cls.livros:
            print(f'{livro._titulo.ljust(25)} | {livro._autor.ljust(25)} | {str(livro._ano_publicacao).ljust(25)} | {livro.disponivel}')

    @property
    def disponivel(self):
        return 'Disponível' if self._disponivel else 'Indisponível'

    def emprestar(self):
        self._disponivel = not self._disponivel

    def devolver(self):
        self._disponivel = not self._disponivel

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis
    