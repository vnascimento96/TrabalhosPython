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

class Cliente:

    def __init__(self):

        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None

    def receber_dados(self):
        self.codigo = 1
        self.nome = 'Vitor'
        self.idade = 23
        self.sexo = 'm'
        self.email = 'Vitor.nascimentosilva@gmail.com'
        self.telefone = 991661560

    
  
       
    
dados = Cliente()
dados.receber_dados()
print(f'codigo: {dados.codigo}')   
print(f'Nome: {dados.nome}')
print(f'idade: {dados.idade}')
print(f'sexo: { dados.sexo}')
print(f'email: {dados.email}')
print(f'telfone: {dados.telefone}')
    





        


    
    
        