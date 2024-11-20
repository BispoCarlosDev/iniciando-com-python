class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria, telefone, rua):
        self.nome = nome
        self.categoria = categoria
        self.telefone = telefone
        self.rua = rua
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.telefone} | {self.rua}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.telefone} | {restaurante.rua} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet', '40028922', 'Rua Curitiba')
restaurante_pizza = Restaurante('Conteiner Pizzas', 'FastFood', '70707070', 'Rua Maringá')

Restaurante.listar_restaurantes()