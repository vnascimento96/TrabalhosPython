#Aula 8 - 18/11/2019
#Web

from flask import Flask
app = Flask(__name__)
@app.route('/')
def inicio():
    return 'Bem vindo ao mundo real meus queridos'

app.run()