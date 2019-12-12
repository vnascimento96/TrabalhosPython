#  1) O que uma pessoa tem? Quais as características?
####### Atributos --- variáveis
#nome
#idade
#telefone
#genero

# 2) O que uma pessoa faz?
# metodos (função/procedimento)

#respira 
#dorme 
#corre
#bebe
#come
#multiplica ####


# 3) Como a pessoa está agora?
# Atributos de estado - Variáveis
#divida
#cansada
#viva
#fome
#sede

class Pessoa:
    '''
    Esta classe é uma demonstração para aula 
    '''
    def __init__(self, nome1, idade1, telefone1, sexo1):
        '''
        O __init__ é o motor que irá inicir as variáveis da classe
        O self é o que ira conecta toda classe
        '''

        ## Atributos #####
        self.nome = nome1
        self.idade = idade1
        self.telefone = telefone1
        self.sexo = sexo1
        #
    
        self.divida = None
        self.cansada = 'não'    
        self.viva = True
        self.fome = 'não'
        self.sede = 'não'
        #
        
        ### Metodos
    def respira(self, respirar):
        if self.viva == True:
            if respirar == True:
                self.viva = True
            else:
                self.viva = False
    def corre(self, distancia):
        if self.viva:
            if distancia < 100:
                self.cansada = 'pouco'
                self.sede = 'pouco'
                self.fome = 'pouco'
            elif distancia >= 100 and distancia <200:
                self.cansada = 'medio'
                self.sede = 'medio'
                self.fome = 'medio'
            elif distancia >= 200:
                self.cansada = 'muito'
                self.sede = 'muito'
                self.fome = 'muito'  


    def dorme(self):
        if self.viva:
             self.cansada = 'não'
             self.come()
             self.bebe()   
    
    def bebe(self):
        if self.viva:
            self.bebe = 'não'
        pass
    def come(self):
        if self.viva:
            self.fome = 'não'
        pass
    def multiplica(self):
        pass # Outra hora


p = Pessoa('Vitor', 23, '47 991661560', 'm')


#p.respira(True)

p.corre(350)
p.dorme()

print(f'Nome é {p.nome}')
print(f'Está vivo? {p.viva}')
print(f'Está com fome? {p.fome}')
print(f'Está com sede? {p.sede}')
print(f'Está cansado? {p.cansada}')