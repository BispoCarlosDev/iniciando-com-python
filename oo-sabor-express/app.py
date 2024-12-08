from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet', '40028922', 'Rua Maringá')
bebida_suco = Bebida('Suco de Açaí', 13.0, 'Médio')
prato_paozinho = Prato('Paozinho Francês', 2.0, 'Chega a manteiga derrete')

def main():
    print(bebida_suco)
    print(prato_paozinho)


if __name__ == '__main__':
    main()