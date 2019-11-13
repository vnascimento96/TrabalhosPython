#Escreva um programa que leia as notas (4) de 3 alunos
#armazene as notas e os nomes em listas
#imprima: 
    #1- nome dos alunos
    #2- media do aluno
    #3- resultado(aprovado>=7)


nome = []
media = []
resultado = []

for i in range (0,2):
    nome.append(input('Digite seu nome: '))
    nota = 0
    for i in range(0,4):
        nota += int(input(f'Digite {i + 1} nota: '))
    media.append(nota/4)

for i in range (0,2):
    if media[i] >= 7:
        resultado.append('Aprovado')
    else:
        resultado.append('Reprovado')

for i in range(0,2):
    print(f'Nome: {nome[i]} Média: {media[i]} Resultado: {resultado[i]}')


    



