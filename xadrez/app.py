import numpy as np 
import pecas
'''
2 - torre
4 - cavalo
6 - bispo
8 - rei
10 - rainha
12 - pião
0 - espaços livres

1 - torre
3 - cavalo
5 - bispo
7 - rei
9 - rainha
11 - pião
0 - espaços livres
'''
class Xadrez:
    vez = True
    cor = True
    tabuleiro = [
        ['tb1','bb1','cb1','rb1','ab1', 'cb2','bb2', 'tb2'],
        ['pb1','pb2','pb3','pb4','pb5', 'pb6','pb7', 'pb8'],
        ['   ','   ','   ','   ','   ', '   ','   ', '   '],
        ['   ','   ','   ','   ','   ', '   ','   ', '   '],
        ['   ','   ','   ','   ','   ', '   ','   ', '   '],
        ['   ','   ','   ','   ','   ', '   ','   ', '   '],
        ['pp1','pp2','pp3','pp4','pp5', 'pp6','pp7', 'pp8'],
        ['tp1','bp1','cp1','rp1','ap1', 'cp2','bp2', 'tp2']
    ]

    @classmethod
    def preto_ou_branco(cls, peca):
        if cls.vez:
            if peca[1] == 'b':
                cls.cor = True
            else:
                cls.cor = False
        else:
            if peca[1] == 'p':
                cls.cor = True
            else:
                cls.cor = False 

    @classmethod
    def vez(cls):
        cls.vez = not cls.vez

    @classmethod
    def movimento_cada_peca(cls, peca, posicao_peca:tuple):
        '''Vai servir apenas pra chamar cada metodo especifico da classe pecasa baseada na peça que foi escolhida pra
        ser movimentada'''
        pass

    @classmethod
    def movimento_valido(cls):
        '''vai servir pra verificar se a peça realmente vai poder realmente ir em todas as  casas que o metodo movimento 
        cada peça disse que ia poder'''
        pass

    @classmethod
    def check(cls):
        '''Server para verificar se o movimento pode ser o rei está em check e se o movimoento pode ser efetuado'''
        pass

    @classmethod
    def mover(cls, peca, posicao):
        cls.preto_ou_branco(peca)
        if cls.cor:
            for  linha in cls.tabuleiro:
                if peca in linha:
                    posicao_peca = (cls.tabuleiro.index(linha), linha.index(peca))
            


        else:
            print(f'É a vez das peças {'brancas' if cls.vez else 'pretas'}')
            cls.jogada()

    @classmethod
    def jogada(cls):
        peca = input('Qual peça deseja movimentar?\n')
        posicao = input('Para qual posição vai movimentar a peça')
        cls.mover(peca, posicao)



