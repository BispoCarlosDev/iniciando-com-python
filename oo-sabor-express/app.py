from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet', '40028922', 'Rua Maringá')
restaurante_japa = Restaurante('japa', 'japonesa', '40028922', 'Rua Maringá')
restaurante_mexicano = Restaurante('mexicano', 'mexicana', '40028922', 'Rua Maringá')

restaurante_praca.receber_avaliacao('Carlos', 9)
restaurante_praca.receber_avaliacao('Pedro', 3)
restaurante_praca.receber_avaliacao('João', 5)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()