# Exercicio 2 = Dicionários
# Escreva um programa que leia os dados de 11 jogadores
# Jogador: Nome, Posição, Numero, PernaBoa
# Crie um dicionario para armazenar os dados
# Crie um dicionario para armazenar os dados
# Imprima todos os jogadores e seus dados


lista_jogadores = []
for i in range(0,11):

    dicionario_jogador = {'Nome': '', 'Posicao': '', 'Numero': '', 'PernaBoa': ''}
    dicionario_jogador['Nome'] = input('Nome do jogador: ')
    dicionario_jogador['Posicao'] = input('Posição do jogador: ')
    dicionario_jogador['Numero'] = int(input('Numero: '))
    dicionario_jogador['PernaBoa'] = input('Perna boa: ')
    lista_jogadores.append(dicionario_jogador)

for dicionario_jogador in lista_jogadores:
    print(f'{dicionario_jogador["Nome"]} - {dicionario_jogador["Posicao"]} - {dicionario_jogador["Numero"]} - {dicionario_jogador["PernaBoa"]}')

    


