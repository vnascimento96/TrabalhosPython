# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)
# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.

class Cliente(dadobruto):

    def __init__(self, dadobruto):
        dados = dado_bruto
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None
        

    def tratamento(self, dadobruto):
        dados = self.dado_bruto
        self.codigo = int(dados[0])
        self.nome = dados[1]
        self.idade = int(dados[2])
        self.sexo = dados[3]
        self.email = dados[4]
        self.telefone = dados[5]

        

    def salvar_dados(self, nome, atributo = 'a'):
        arquivo = open(f'aula23/{nome}.txt', atributo)
        #texto = f'{self.codigo};{self.nome};{self.idade};{self.sexo};{self.email};{self.telefone}'
        texto = f'{self.dado_bruto}\n'
        arquivo.write(texto)
        arquivo.close()

    def atualizar(self):
        #self.codigo = input('Digite o novo nome do cliente: ') CODIGO N SE ATUALIZA!
        self.nome = input('Digite o novo nome do cliente: ')
        self.idade = int(input('Digite a idade do cliente: '))
        self.sexo = input('Digite o sexo do cliente: ')
        self.email = input('Digite o email do cliente: ')
        self.telefone = input('Digite o telefone do cliente: ')
        self.dado_bruto = f'{self.codigo};{self.nome};{self.idade};{self.sexo};{self.email};{self.telefone}'
        self.salvar_dados(arquivo_novo)       


    
    
pessoa = Cliente(dadobruto)

pessoa.tratamento()
pessoa.salvar_dados()

print(f'Codigo: {pessoa.codigo}')
print(f'Nome: {pessoa.nome}')
print(f'Idade: {pessoa.idade}')
print(f'Sexo: {pessoa.sexo}')
print(f'Email: {pessoa.email}')
print(f'Telefone: {pessoa.telefone}')
        
        
    




