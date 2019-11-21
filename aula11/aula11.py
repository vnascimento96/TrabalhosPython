# Aula 11 - 21/11/2019
# Prova

#--- 1- Crie um programa que calcule o imposto ISS de um serviço de desenvolvimento de software Utilizar metodos
#--- 2-Crie um programa que calcule a rentabilidade anual de um investimento baseando-se em sua rentabilidade mensal(juros compostos) 
    #a rentabilidade deve ser apresentada em % e R$
    # Utilisar metodos 
#--- 3-
#--- 4-
#--- 5-
from calculo import*
 
nomeEmpresa = input('Digite o nome da sua empresa: ')
valorServico =  float(input('Digite o valor do serviço: '))

print(f'Empresa: {nomeEmpresa} Imposto do serviço (ISS): {ISS(valorServico)}')
