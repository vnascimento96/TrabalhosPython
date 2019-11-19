# Aula 9 - 19/11/2019
# Web2 
# Crie um programa que: 
# 1 - Leia dois numeros inteiros
# 2 - Calcule as 5 operações matematicas

from operacoes import soma, subtracao, multiplicacao, divisao, divisao_fracionada, resto, raiz

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))


print(f'Soma dos dois numeros: {soma(numero1,numero2)}', '\n')
print(f'Subtração dos dois numeros: {subtracao(numero1, numero2)}', '\n')
print(f'Multiplicação dos dois numeros: {multiplicacao(numero1, numero2)}', '\n')
print(f'Divisão dos dois numeros: {divisao(numero1, numero2)}','\n' )
print(f'Fração dos dois numeros: {divisao_fracionada(numero1, numero2)}', '\n')
print(f'Resto dos dois numeros: {resto(numero1, numero2)}', '\n')
print(f'Raiz dos dois numeros: {raiz(numero1, numero2)}', '\n')


