while True:
    try:

        n1 = int(input('Digite o numero 1: '))
        n2 = int(input('Digite o numero 2: '))

        print(f'A soma entre {n1} + {n2} é {n1 + n2}')
        print(f'A divisão entre {n1} / {n2} é {n1 / n2}')
        print(f'A multiplicação entre {n1} * {n2} é {n1 * n2}')
        print(f'A subtração entre {n1} - {n2} é {n1 - n2}')

        sair = input('Dejesa sair do programa? s/sim e n/não:  ')
        if sair == 's':
            break

    except ValueError:
        print('Você digitou o numero errado, digite um numero inteiro.')

    except ZeroDivisionError:
        print('Divisão por zero. Divida por qualquer outro numero inteiro')
        


