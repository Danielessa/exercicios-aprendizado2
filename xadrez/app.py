import numpy as np 
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
        if peca[1] == 'b':
            cor = True
        else:
            cor = False

        return cor 

    @classmethod
    def vez(cls):
        cls.vez = not cls.vez

    @classmethod
    def mover(cls, peca, posicao):
        pass

