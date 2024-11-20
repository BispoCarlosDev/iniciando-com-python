class Musica:

    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

tempo_perdido = Musica('Tempo Perdido', 'Legião Urbana', 229)
Je_Te_Laisserai_des_Mots = Musica('Je_Te_Laisserai_des_Mots', 'Patrick Watson', 161)
She = Musica('She', 'Elvis Costello', 189)

Musica.listar_musicas()