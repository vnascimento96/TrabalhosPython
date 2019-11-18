# Aula 7 - 14/11/2019
# Listas

lista = []
dicionario = { 'Nome': 'Vitor', 'Sobrenome': 'Nascimento'}
print(dicionario)
print(dicionario['Sobrenome'])

nome = 'Vitor'
lista_notas = [10,20,50,70]
media = sum(lista_notas)/len(lista_notas)
situacao = 'Reprovado'
if media >=7:
    situacao = 'Aprovado'

dicionario_alunos = {'Nome': nome, 'Lista_notas': lista_notas, 'Media': media, 'Situação': situacao }

print(f'{dicionario_alunos["Nome"]} - {dicionario_alunos["Situação"]}')

dicionario_bandas = {'Nome' : ''}
dicionario_bandas['Nome'] = 'Calipso'
dicionario_bandas['Nome'] = 'Dejavu'

print(dicionario_bandas)

dicionario = {'Nome': 'Vitor', 'Sobrenome': 'Nascimento'}
dicionario['Sobrenome'] = 'Silva'
dicionario['CPF'] = '096.555.666-75'

print(dicionario)

dicionario_pessoa = {'Nome': '', 'Sobrenome': '', 'CPF': '', 'RG': ''}
lista_pessoas = []
for i in range(1,11):
    dicionario_pessoa['Nome'] = input('Digite o nome: ')
    dicionario_pessoa['Sobrenome'] = input('Digite o sobrenome: ')
    dicionario_pessoa['CPF'] = input('Digite o CPF: ')
    dicionario_pessoa['RG'] = input('Digite o RG: ')
    lista_pessoas.append(dicionario_pessoa)

    