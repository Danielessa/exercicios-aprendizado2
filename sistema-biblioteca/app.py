import requests
from fastapi import FastAPI, Query

app = FastAPI()


app.get('/api/emprestar-livro')
def emprestar_livro():
    pass

app.get('/api/devolver-livro')
def devolver_livro():
    pass

app.get('/livros-emprestado')
def livros_emprestados():
    pass

app.get('/api/cadastrar-livro')
def cadastrar_livro():
    pass

app.get('api/cadastrar-usuario')
def cadastrar_usuario():
    pass





'''

emprestar livro
devolver livro
cadastrar livro
listar livros
livros emprestados
alterar dados livros
'''