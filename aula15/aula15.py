# Aula 15 - 28-11-2019
# Manipulação de arquivos


#arquivo = open ('aula15.txt', 'a')
#arquivo.write('Vitor Nascimento \n')
#arquivo.close()

#arquivo = open('aula15.txt', 'r')
#for linha in arquivo:
 #   print(linha)
#arquivo.close()

def salvar(pessoa_dicionario):
    arquivo = open('aula15.txt' , 'a')
    arquivo.write(f"{pessoa_dicionario['nome']};{pessoa_dicionario['sobrenome']};{pessoa_dicionario['idade']}\n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('aula15.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        pessoa = {'nome': lista_linha[0], 'sobrenome': lista_linha[1], 'idade': lista_linha[2]}
        lista.append(pessoa)
    arquivo.close()
    return lista




nome = input('Nome: ')
sobrenome = input('Digite o sobrenome: ')
idade = int(input('Digite a sua idade: '))

pessoa = {'nome': nome , 'sobrenome': sobrenome , 'idade': idade}
salvar(pessoa)



for p in ler():
    print(f"Nome: {p['nome']}  Sobrenome: {p['sobrenome']} - Idade: {p['idade']}")