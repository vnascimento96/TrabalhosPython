# Aula 20 - 05-12-2019
# Lista com for e metodos

# Com esta lista:

lista = [
         ['codigo','produto','valor','quantidade'],
         [1,'Cevada',15.00,10],
         [2,'Lupulo',150.50,200],
         [3,'Malte',57.80,5000],
         [4,'Levedura 1',10.65,500],
         [5,'Extrato de Levedura',15.00,60],
         [6,'Levedura 2',15.50,87]
        ]

# 2.1 - Faça uma função que pegue esta lista e retorne uma lista com dicionario.

# 2.2 - Faça outra função para consultar o preço através do código passado
# por parametro. Esta função deve printar o nome do produto, a quantidade
# e o preço.
# Execute esta função dentro do while e quando digitar qualquer código que 
# não tenha produto cadastrado o programa se encerra.
#

cabecalho = lista[0]
#print(cabecalho)

dados = lista[1:]
#print(dados)
lista_dic = []


for produtos in dados:
    #[1,'Cevada',15.00,10]
    dicionario = {cabecalho[0]: produtos[0], cabecalho[1]: produtos[1], cabecalho[2]: produtos[2], cabecalho[3]: produtos[3]}
    lista_dic.append(dicionario)

for i in lista_dic:
    print(i)


#2.2



    
    
        

