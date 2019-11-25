def calculoRaiz():
    if raiz == 1:
        calculo = numero ** 0.5
        print(f'Raiz quadrada de {numero} é : {calculo}')
    elif raiz == 2:
        calculo = numero ** (1/3)
        print(f'Raiz cubica de {numero} é : {calculo}')
    else:
        print('Comando inválido') 
        

raiz = int(input('Você desejar calcular raiz quadrada = 1 ou raiz cubica = 2: '))
numero = float(input('Digite o numero que vc deseja calcular a raiz: '))
calculoRaiz()