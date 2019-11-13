#Aula 6 - 13/11/2019
#Listas

#Inicialização de uma variável tipo lista vazia
lista1 = []
#inicializaçãõ de uma variável lista, com elementos
lista2 = ["Marcelo", 'Nicole', 'Matheus']
#Inicialização de uma variável lista, com inteiros
lista3 = [1,2,3,4,5]
#Lista de tipos diferentes
lista4 = [1, 'Maykon', 12.5]


#Impressão das listas criadas
print(lista1)
print(lista2)
print(lista3)

#Adicionando elementos em uma lista ja criada
lista1.append(lista2)
lista1.append(lista3) 

#Impressão das listas modificadas
print(lista1)
print(lista2)
print(lista3)

#Criação de lista com dados vindos da função input
lista_perguntas= [input('Digite seu artista favorito'), input('Digite seu guitarrista favorito')]
print(lista_perguntas)

#Recuperando o dado de uma posição especifica da lista
posicao = int(input('Digite a posição: '))
print(lista2[posicao-1])

