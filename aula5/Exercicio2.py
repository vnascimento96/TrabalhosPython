nomeFuncionario = input('Nome do funcionario: ')
idade = int(input('Idade: '))

if idade >= 18:
    print('Pode comprar produtos alcoólicos')
else:
    print('Não pode consumir bebidas alcoólicas')


produto = input('Digite o produto que deseja comprar: ')
categoria = int(input('Alcoólico ou não alcoólico? 1-Sim / 2-Não: '))

print('####################################')

if idade >=18 and categoria == 1:
    print(f'Funcionário: {nomeFuncionario} Produto: {produto}')
elif idade < 18 and categoria == 1:
    print('Bebida inválida')
elif idade <=18 and categoria == 2:
    print(f'Funcionario: {nomeFuncionario} Produto: {produto}')
elif idade < 18 and categoria == 2:
    print(f'Funcionario: {nomeFuncionario} Produto: {produto}')