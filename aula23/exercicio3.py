class Cadastro:
    def __init__(self):
        self.lista = []
        self.ler() 

    def ler(self):
        try:
            arquivo = open('aula23/cadastro2.txt','r')
            for pessoa in arquivo:
                pessoa = pessoa.strip().split(';')
                dic = {'codigo': pessoa[0], 'nome': pessoa[1], 'idade':pessoa[2], 'sexo':pessoa[3], 'email': pessoa[4],'telefone': pessoa[5]}
                self.lista.append(dic)




        finally:
            arquivo.close()   

    def salvar(self):
        try:
            arquivo = open('aula23/cadastro_novo.txt','a')
            for pessoa in self.lista:
                texto = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['idade']};{pessoa['sexo']};'{pessoa['email']};{pessoa['telefone']}\n" 
                arquivo.write(texto)
            
        finally:
            arquivo.close()

    def cadastrar(self):
        nome = input('Digite o nome do cliente: ')
        idade = int(input('Digite a idade: '))
        sexo = input('Digite o sexo: ')
        email = input('Digite o email: ')
        telefone = input('Digite o telefone: ')

        codigo =   int(self.lista[-1]['codigo']) + 1

        texto = f'{codigo};{nome};{idade};{sexo};{email};{telefone}
        

    def consulta(self, codigo):
        for pessoa in self.lista:
            if int(pessoa['codigo']) == codigo:
                print(f'''
                    Codigo: {pessoa['codigo']}
                    Nome: {pessoa['nome']}
                    Idade: {pessoa['idade']}
                    Sexo: {pessoa['sexo']}
                    Email: {pessoa['email']}
                    Telefone: {pessoa['telefone']} ''')

                break

    def atualizar(self):
        for pessoa in self.lista:
            if int(pessoa['codigo']) == codigo:
                nome = input('Digite o nome do cliente: ')
                idade = int(input('Digite a idade: '))
                sexo = input('Digite o sexo: ')
                email = input('Digite o email: ')
                telefone = input('Digite o telefone: ')



p = Cadastro()

p.consulta(1)
p.cadastrar()
p.salvar()
