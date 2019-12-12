# Aula 21 - 09-12-2019

''' Crie uma classe cliente

deve ter como atributos: codigo, cpf, nome, idade, sexo

como metodos: receber salario, comprar, pagar divida

Quando recebe aumenta o dinheiro na carteira

quando compra aumenta os bens e diminui o dinheiro na carteira

se comprar e n tiver dinheiro suficiente deve deiminuir o dinheiro da carteira e aumentar a divida

para pagar a divida tem que ter dinheiro o suficiente na carteira

3) atributos de estado: dinheiro na carteira, divida, bens
'''

class Cliente:

    def __init__(self, codigo, cpf, nome, idade, sexo):

        self.codigo = codigo
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

        self.salario = 0.0
        self.carteira = self.salario
        self.bens = 0.0
        self.divida = 0.0


    def set_salario(self, salario):
        self.carteira += salario


    def set_comprar(self, bens):
        self.bens += bens
        self.carteira -= bens
        if self.carteira < 0:
            self.divida = (self.divida - self.carteira)*1
            self.carteira = 0 
        
        
    def set_divida(self, divida):
        if self.carteira > self.divida:
            self.divida = 'Paga'
        else:
            self.divida = 'Não paga'

        

c = Cliente('1', '968.485.485-57', 'Vitor', 23, 'm')

c.set_salario(2000.00)
c.set_comprar(2500.00)


print(f'Codigo: {c.codigo}')
print(f'Nome: {c.nome}')
print(f'Sexo: {c.sexo}')
print(f'Idade: {c.idade}')
print(f'Seu dinheiro na carteira: R$ {c.carteira}')
print(f'Sua divida esta acumulada em: R$ {c.divida}')
print(f'Total de bens adiquiridos no valor de: R$ {c.bens}')