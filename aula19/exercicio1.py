# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]


# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com


# 2 - usando o for, imprima todos nomes um abaixo do outro
#
# 3 - Usando a indexação faça uma lista com 3 bibliotecas contendo os dados 
# do Mateus, Paulo # e João contendo
# como chaves: nome, email, idade, telefone (nesta  sequencia)

cabe = cadastroHBSIS[0::2]
nome = cadastroHBSIS[1]
telefone = cadastroHBSIS[3]
email = cadastroHBSIS[5]
idade = cadastroHBSIS[7]




#1
print(f'Nome: {nome[0]} - Telefone: {telefone[0]}')
print(f'Idade de {nome[4]} é {idade[4]}')
print(f'{cabe[2]} de {nome[3]} é {email[3]}')

#2
for nomes in nome:
    print(nomes)

#3

# ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
#                 'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
#                 'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
#                 'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
#                 ]



