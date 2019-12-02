def cadastro_cliente(numero_funcao):
    dados_cliente = ['Codigo_cliente', 'CPF', 'nome_completo', 'data_de_nascimento', 'estado', 'cidade', 'cep']

    lista = []
    

    
    for j in range(numero_funcao):
        dicionario = {}

        for i in dados_cliente:
            dicionario[i] = input(f'{i}: ')

        lista.append(dicionario)
    return lista

numero = int(input('Digite um numero de cadastro: '))
lista_cadastro = cadastro_cliente(numero)


# Criar uma fução para salvar em arquivo:

arquivo = open('cliente.txt', 'a')
for cliente in arquivo:
    cliente_chave = list    
    for cliente in arquivo:
        salvar = f'{cliente['Codigo_cliente'];}'

arquivo.write()


arquivo.close()