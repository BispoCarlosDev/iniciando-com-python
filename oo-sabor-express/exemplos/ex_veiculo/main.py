from carro import Carro
from moto import Moto

carro_corolla = Carro('Toyota', 'Corolla', 4)
carro_classic = Carro('Chevrolet', 'Classic', 4)
carro_strada = Carro('Fiat', 'Strada', 2)

moto_fan = Moto('Honda', 'Fan', 'Casual')
moto_factor = Moto('Yamaha', 'Factor', 'Casual')
moto_XRE = Moto('Yamaha', 'XRE', 'Esportiva')


def main():
    print(carro_corolla)
    print(carro_classic)
    print(carro_strada)
    print(moto_fan)
    print(moto_factor)
    print(moto_XRE)

