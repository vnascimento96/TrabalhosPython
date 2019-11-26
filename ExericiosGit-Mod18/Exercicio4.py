def porc():
    if salario <=1000.00:
        contribuicao = salario * 0.010
        print(f'Contribuição no valor de {contribuicao}, salario no valor de {salario - contribuicao}')
    elif salario >= 1000.01 and salario <= 3000.00:
        contribuicao = salario * 0.015
        print(f'Contribuição no valor de {contribuicao}, salario no valor de {salario - contribuicao}')
    elif salario >= 3000.01 and salario <= 6000.00:
        contribuicao = salario * 0.02
        print(f'Contribuição no valor de {contribuicao}, salario no valor de {salario - contribuicao}')
    elif salario >= 6000.01:
        contribuicao = salario * 0.025
        print(f'Contribuição no valor de {contribuicao}, salario no valor de {salario - contribuicao}')
    else:
        print('Valor invalido!')

salario = float(input('Digite o seu salario: '))
porc()