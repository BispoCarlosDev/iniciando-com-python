class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria, telefone, rua):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._telefone = telefone
        self._rua = rua.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._telefone} | {self._rua}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Telefone'.ljust(20)} | {'Endereço'.ljust(20)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante._telefone.ljust(20)} | {restaurante._rua.ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet', '40028922', 'Rua Curitiba')
restaurante_praca.alterar_estado()
restaurante_pizza = Restaurante('conteiner Pizzas', 'FastFood', '70707070', 'Rua Maringá')

Restaurante.listar_restaurantes()