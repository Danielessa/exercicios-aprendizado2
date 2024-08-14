import requests
from datetime import datetime


url_livros = 'https://raw.githubusercontent.com/Danielessa/Json-para-treino/main/sistema-biblioteca/livros.json'
url_emprestimos = 'https://raw.githubusercontent.com/Danielessa/Json-para-treino/main/sistema-biblioteca/emprestimos.json'
url_usuarios = 'https://raw.githubusercontent.com/Danielessa/Json-para-treino/main/sistema-biblioteca/usuarios.json'

now = datetime.now()

livros = requests.get(url_livros).json()
emprestimos = requests.get(url_emprestimos).json()
usuarios = requests.get(url_usuarios).json()

class Gerenciamento:
    dados = {'livros':livros, 'emprestimos':emprestimos, 'usuarios':usuarios}
    
    @classmethod
    def inserir_dados(cls, funcao, parametros, dados_parametros, posicao):
        entrada ={}
        posicao = posicao if posicao != -1 else len(cls.dados[funcao])
        for indice,parametro in enumerate(parametros):
            entrada[parametro] = dados_parametros[indice]
        
        cls.dados[funcao].insert(posicao, entrada)

    @classmethod 
    def mostrar_dados(cls, funcao):
        return cls.dados[funcao]
    
    @classmethod
    def excluir_dados(cls, funcao, indice):
        cls.dados[funcao].pop(indice)

    









