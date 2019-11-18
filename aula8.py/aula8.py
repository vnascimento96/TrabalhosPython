# Aula 8 - 18/11/2019
# Tuplas

numeros = [1,4,6]   #Lista
usuario = {'nome' : 'user', 'senha' : 12345}   #Dicionario
pessoa = ('Vitor' , 'Nascimento' , 0, 26.7, numeros)     #Tuplas

print(numeros)
print(usuario)
print(pessoa)

numeros[1] = 5
usuario['senha'] = 54321
print(pessoa[4][1])
lista_pessoas = []
lista_pessoas.append(pessoa)

