import os

restaurantes = [{'Nome':'Garden', 'Categoria':'Pizzaria', 'Ativo': False},
                {'Nome':'Don Andi', 'Categoria':'Anburgueria', 'Ativo': True},
                {'Nome':'Nook', 'Categoria':'Cafeteria', 'Ativo': True}]

def exibir_nome_do_sistema():
    '''Essa função Exibe o nome do sistema'''
    print("""
    
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
    """)

def exibir_subtitulo(texto):
    '''Essa função exibe o subtítulo'''
    os.system('cls')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)

def exibir_opcoes():
    '''Essa função exibe as opções do Menu'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar Status do Restaurante')
    print('4. Sair\n')

def voltar_ao_menu():
    '''Essa função volta ao menu'''
    input('\nPressione alguma tecla para voltar ao menu:')
    main()

def opcao_invalida():
    '''Essa função informa quando uma opção é inválida'''
    print('\nOpção Inválida!')
    voltar_ao_menu()

def finalizar_app():
    '''Essa função finaliza o app'''
    exibir_subtitulo('Finalizando o programa!')

def cadastrar_restaurantes():
    '''Essa função cadastra Novos Restaurantes
    
    Inputs:
    Nome do Restaurante
    Categoria do Restaurante

    Outputs:
    O Restaurante foi cadastrado com sucesso.
    '''
    exibir_subtitulo('Cadastrando novos Restaurantes:')
    nome_restaurante = input('Digite aqui o nome do Restaurante: ')
    categoria_restaurante = input(f'Digite aqui a categoria do Restaurante {nome_restaurante}: ')
    dados_restaurante = {'Nome':nome_restaurante, 'Categoria':categoria_restaurante, 'Ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    '''Essa função lista os restaurantes
    
    Outputs:
    Nome, Categoria e Status do Restaurante
    '''
    exibir_subtitulo('Listando os Restaurantes:')

    print(f'\n{'Nome do Restaurante'.ljust(22)}|{'Categoria'.ljust(20)}|{'Status'}')
    for restaurante in restaurantes:
        nome = restaurante['Nome']
        categoria = restaurante['Categoria']
        ativo = 'Ativo' if restaurante['Ativo'] else 'Inativo'
        print(f'* {nome.ljust(20)}|{categoria.ljust(20)}|{ativo}')

    voltar_ao_menu()

def alterar_status_restaurante():
    '''Essa função altera o status dos Restaurantes
    
    Inputs:
    Nome do Restaurante a ser alterado o status

    Outputs:
    Confirmação de Alteração do Status
    Informação de que o Restaurante não foi encontrado
    '''
    exibir_subtitulo('Alterando Status do Restaurante')

    nome_restaurante = input(f'Digite aqui o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            if restaurante['Ativo'] == True:
                mensagem = f'Restaurante {nome_restaurante} Ativado com Sucesso!'
            else:
                mensagem = f'Restaurante {nome_restaurante} Desativado com Sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado!')

    voltar_ao_menu()

def escolher_opcao():
    '''Essa função é usada para o usuário escolher a opção desejada
    
    Inputs:
    Número da Opção desejada
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        # match opcao_escolhida:
        #     case 1:
        #         print('Cadastrar Restaurante')
        #     case 2:
        #         print('Listar Restaurantes')
        #     case 3:
        #         print('Ativar Restaurante')
        #     case 4:
        #         finalizar_app()

        if opcao_escolhida == 1:
            cadastrar_restaurantes()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função é a função que inicia o programa'''
    os.system('cls')
    exibir_nome_do_sistema()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()