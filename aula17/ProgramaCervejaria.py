# Aula 17 - 02/12/2019
# Programa Cerveja Ituroró

menu = '''
######################################################################################################################################
#                                           I Festival de Cerveja em Ituroró                                                         #
######################################################################################################################################


1  - Cadastro cliente 
2 - Ver Clients Cadastrados
3 - Cadastro de Produtos
4 - Ver Produtos Cadastrados
5 - Vendas
6 - Relatório de Vendas 
7 - Sair

Digite a opção desejada: ''' 


while True:
    opcao = input(menu)
    if opcao == '1': 
        print('Cadastro de Cliente')
    elif  opcao == '2':
        print('Ver Cliente Cadastrado')
    elif opcao == '3':
        print('Cadastro Produto')
    elif opcao == '4':
        print('Ver produtos cadastrados')
    elif opcao == '5':
        print('Vendas')
    elif opcao == '6':
        print('Relatorio de Vendas')
    elif opcao == '7':
        print('Sair')
        break
    else:
        print('Valor Inválido')
    
