valor = int(input('\nDigite um número inteiro: '))

if valor%2 == 0:
    print('O valor escolhido é par.')
else:
    print('O valor escolhido é ímpar.')

idade = int(input('\nDigite a sua idade: '))

if idade < 13:
    print('\nVocê é Criança, já pra casa!')
elif idade >= 13 and idade < 18:
    print('Você é adolescente.')
else:
    print('Você é adulto, pode entrar Sr. e Sra.')

nome_padrao = 'Lalita Chilena'
senha_padrao = '40028922'

nome_usuario = input('\nPor favor, informe seu nome de usuário: ')
senha = input('\nPor favor, informe sua senha de acesso: ')

if nome_usuario == nome_padrao and senha == senha_padrao:
    print(f'Bem vindo {nome_usuario}')
else:
    print('Acesso negado, impostor!')

x = float(input('\nPor favor, me informe a coordenada x: '))
y = float(input('\nPor favor, me informe a coordenada y: '))

if x > 0 and y > 0:
    print('As coordenadas apontam para o Primeiro Quadrante.')
elif x < 0 and y > 0:
    print('As coordenadas apontam para o Segundo Quadrante.')
elif x < 0 and y < 0:
    print('As coordenadas apontam para o Terceiro Quadrante.')
elif x > 0 and y < 0:
    print('As coordenadas apontam para o Quarto Quadrante.')
else:
    print('O ponto está posicionado no eixo ou origem.')