from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet', '40028922', 'Rua Maringá')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana', '40028922', 'Rua Maringá')
restaurante_japones = Restaurante('Japa', 'Japonesa', '40028922', 'Rua Maringá')

restaurante_japones.alterar_estado()

restaurante_praca.receber_avaliacao('Carlos', 10)
restaurante_praca.receber_avaliacao('Pedro', 9)
restaurante_praca.receber_avaliacao('João', 8)

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()