#Aula 4
# Fazer um programa que leia 2 numeros
# Realize as 4 operações matematicas
# Imprima o resultado das operações
# Diga qual numero é o maior dos dois numeros


numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))

somaFinal = numero1 + numero2

subtracaoFinal = numero1 - numero2

divisaoFinal = numero1 / numero2

multiplicacaoFinal = numero1 * numero2

print(f'Soma: {somaFinal} Subtração: {subtracaoFinal} Divisão: {divisaoFinal} Multiplicação: {multiplicacaoFinal}')


if numero1 > numero2:
    print('Numero maior: ', numero1)
if numero1 == numero2:
    print('Os números são iguais: ', numero1)
else: 
    print('Número maior: ', numero2)        







    
