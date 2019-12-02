# 1 - Faça um menu interativo que tenha: Cadastro de banda, cadastro do album, cadastri da musica, Sair.
#O menu deve ser executado até que se escolha a opção sair.
#Cada opção deve ser mostrada
#Quando selecionado a opção sair, deverá aparecer na tela as informações das bandas cadastradas,albuns e muscias.




lista_banda = []
lista_album = []
lista_musica = []



menu = '''

    
    1 - Nome banda
    2 - Nome album
    3 - Nome musica
    4 - Sair
    Digite a opçao desejada: '''


while True:
    opcao = input(menu)

    if opcao == '1':
        lista_banda.append(input('Digite sua banda: '))
    elif opcao == '2':
        lista_album.append(input('Digite o album: '))
    elif opcao == '3':
        lista_musica.append(input('Digite a musica: '))
    elif opcao == '4':
        print(f'Banda: {lista_banda} - Albuns {lista_album} - Musicas {lista_musica}')
        break
    else: 
        print('Comando invalido')
         

