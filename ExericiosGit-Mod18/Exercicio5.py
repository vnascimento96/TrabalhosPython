def menu():
    if opcao == 0:
        print('Usuário realizou o logoff')
    elif opcao == 1:
        print('Cadastro de usuários')
    elif opcao == 2:
        print('Lista de usuários cadastrados')
    else:
        print('Opção invalida.')

    

opcao = int(input('''
0 - Sair
1 - Cadastrar
2 - Listar
Digite o numero da opção que desejar: '''))
menu()