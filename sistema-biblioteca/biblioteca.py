from gerenciamento import Gerenciamento

class Biblioteca:
    #Cadastrar Livro
    @classmethod
    def cadastrar_livro(cls, info_livros):
        info_necessarias = ["id", "titulo", "autor", "ano_publicacao","disponivel", "genero", "exemplares"]   
        Gerenciamento.inserir_dados('livros', info_necessarias, info_livros, -1)

    #Cadastrar Usuario
    @classmethod
    def cadastrar_usuario(cls, info_usuario):
        info_necessarias = ["id", "nome", "tipo", "departamento" if info_usuario[2] == 'professor' else 'curso',"historico"]       
        Gerenciamento.inserir_dados('usuarios', info_necessarias, info_usuario, -1)

    #emprestar livro
    @classmethod
    def emprestar_livro(cls, info_emprestimo):
        info_necessarias = ["id", "livro_id", "usuario_id", "data-emprestimo","data-devolucao-prevista", "data-devolucao"]   
        Gerenciamento.inserir_dados('emprestimos', info_necessarias, info_emprestimo, -1)

    #Livros emprestados
    @classmethod
    def livros_emprestados():
        dados = Gerenciamento.mostrar_dados('emprestimos')
        print(dados)
    
    #Devolver livros
    @classmethod
    def devolver_livro(cls, id_emprestimo, data_devolucao):
        dados_emprestimo = Gerenciamento.mostrar_dados('emprestimos')
        for indice, emprestimo in enumerate(dados_emprestimo):
            if emprestimo['id'] == id_emprestimo:
                parametros_emprestimo = []
                info_emprestimo = []
                for parametros, info in emprestimo.items():
                    parametros_emprestimo.append(parametros)
                    info_emprestimo.append(info)
                indice_emprestimo = indice

        info_emprestimo[-1] = data_devolucao

        Gerenciamento.excluir_dados('emprestimos', indice_emprestimo)
        Gerenciamento.inserir_dados('emprestimos', parametros_emprestimo, info_emprestimo , indice_emprestimo)
       


'''1,2,3,5'''
Biblioteca.devolver_livro(1, '13-08-2024')



        


