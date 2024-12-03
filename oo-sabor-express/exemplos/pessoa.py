class Pessoa:
    pessoas = []

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'Meu nome é {self.nome}, tenho {self.idade} anos e minha profissão é {self.profissao}.'
    
    @classmethod
    def listar_pessoas(cls):
        for pessoa in cls.pessoas:
            print(f'Meu nome é {pessoa.nome}, tenho {pessoa.idade} anos e minha profissão é {pessoa.profissao}.')

    def aniversario(self):
        self.idade += 1

    @classmethod
    def saudacao(cls):
        for pessoa in cls.pessoas:
            print(f'Saudações {pessoa.profissao} {pessoa.nome}')

pessoa01 = Pessoa('Carlos', 23, 'Técnico de Futebol')
pessoa02 = Pessoa('Pedro', 32, 'Engenheiro')
pessoa03 = Pessoa('João', 20, 'Corretor')

Pessoa.listar_pessoas()
Pessoa.saudacao()
pessoa01.aniversario()
pessoa03.aniversario()

Pessoa.listar_pessoas()
Pessoa.saudacao()