nome = input('Digite seu nome: ')
sobreNome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))
salarioBase = float(input('Digite seu salário base: '))
comissao = float(input('Digite sua comissão: '))
salarioFinal =  salarioBase + comissao

print(f'Nome: {nome} {sobreNome} Idade: {idade} Salário: {salarioFinal}')

if idade < 18:
    print('Não pode usar mercado Tech, para o que presta')
else:
    print('pode usar mercado Tech e chapar')
        


