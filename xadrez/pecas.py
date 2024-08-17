'''
Cada método vai retornar uma lista de tuplas que representam as posições onde as peças podem se movimentar

[
        ['tb1','bb1','cb1','rb1','ab1', 'cb2','bb2', 'tb2'],
        ['pb1','pb2','pb3','pb4','pb5', 'pb6','pb7', 'pb8'],
        ['   ','   ','   ','   ','   ', '   ','   ', '   '],
        ['   ','   ','   ','   ','   ', '   ','   ', '   '],
        ['   ','   ','   ','   ','   ', '   ','   ', '   '],
        ['   ','   ','   ','   ','   ', '   ','   ', '   '],
        ['pp1','pp2','pp3','pp4','pp5', 'pp6','pp7', 'pp8'],
        ['tp1','bp1','cp1','rp1','ap1', 'cp2','bp2', 'tp2']
    ]

'''

class Pecas:
    def piao(cls, posicao):
        pass
    
    @classmethod
    def torre(cls, posicao):
        cls.movimentos = []
        for linha in range(8):
            if linha != posicao[0]:
                cls.movimentos.append((linha, posicao[1]))

        for coluna in range(8):
            if coluna != posicao[1]:
                cls.movimentos.append((posicao[0], coluna))

        return cls.movimentos

    def cavalo(cls, posicao):
          # Movimentos possíveis de um cavalo em relação à sua posição atual
        movimentos_possiveis = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        x_inicial, y_inicial = posicao
        posicoes_validas = []

        # Calcula as novas posições
        for movimento in movimentos_possiveis:
            x_novo = x_inicial + movimento[0]
            y_novo = y_inicial + movimento[1]

            # Verifica se a nova posição está dentro dos limites do tabuleiro de xadrez
            if 1 <= x_novo <= 8 and 1 <= y_novo <= 8:
                posicoes_validas.append((x_novo, y_novo))

        return posicoes_validas

    def bispo(cls, posicao):
        pass

    def rei(cls, posicao):
        pass

    def rainha(cls, posicao):
        pass

    def movimento_valido(cls, tabuleiro):
        '''
        Verifica se vai ser possivel concluir o movimento devido a algum impedimento no caminho
        '''
        pass


movimentos = Pecas.torre((0,0))

print(movimentos)


'''

'''