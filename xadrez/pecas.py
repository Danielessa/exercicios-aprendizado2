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
        cls.movimentos = []

        # Calcula as novas posições
        for movimento in movimentos_possiveis:
            x_novo = x_inicial + movimento[0]
            y_novo = y_inicial + movimento[1]

            # Verifica se a nova posição está dentro dos limites do tabuleiro de xadrez
            if 0 <= x_novo <= 7 and 0 <= y_novo <= 7:
                cls.movimentos.append((x_novo, y_novo))

        return cls.movimentos

    @classmethod
    def bispo(cls, posicao):
        cls.movimentos = []
        x_inicial, y_inicial = posicao
        y_inverso = 7 - y_inicial
        
        if x_inicial >= y_inicial:
            x_referencia, y_referencia = x_inicial - y_inicial, 0
            cls.movimentos.append((x_referencia, y_referencia))

        else:
            x_referencia, y_referencia = 0, y_inicial - x_inicial
            cls.movimentos.append((x_referencia, y_referencia)) 
        
        
        if x_inicial >= y_inverso:
            x_referencia_inversa, y_referencia_inversa = x_inicial - y_inverso, 0
            y_referencia_inversa = 7 - y_referencia_inversa


            cls.movimentos.append((x_referencia_inversa, y_referencia_inversa))

        else:
            x_referencia_inversa, y_referencia_inversa = 0, y_inverso - x_inicial
            y_referencia_inversa = 7 - y_referencia_inversa

            cls.movimentos.append((x_referencia_inversa, y_referencia_inversa)) 
        
        
        
        for cont in range(8):
                x_referencia += 1
                y_referencia += 1
                x_referencia_inversa += 1
                y_referencia_inversa -= 1
                if 0 <= x_referencia <= 7 and 0 <= y_referencia <= 7 and (x_referencia != x_inicial or y_referencia != y_inicial):
                    cls.movimentos.append((x_referencia, y_referencia))
                
                if 0 <= x_referencia_inversa <= 7 and 0 <= y_referencia_inversa <= 7 and (x_referencia_inversa != x_inicial or y_referencia_inversa != y_inicial):
                    cls.movimentos.append((x_referencia_inversa, y_referencia_inversa))
                
        return cls.movimentos


    def rei(cls, posicao):
        movimentos = [(-1, -1), (-1, 0) , (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]

        for c in range(3):
            
        

    @classmethod
    def rainha(cls, posicao):
        cls.movimentos = []

        for linha in range(8):
            if linha != posicao[0]:
                cls.movimentos.append((linha, posicao[1]))

        for coluna in range(8):
            if coluna != posicao[1]:
                cls.movimentos.append((posicao[0], coluna))

        x_inicial, y_inicial = posicao
        y_inverso = 7 - y_inicial
        
        if x_inicial >= y_inicial:
            x_referencia, y_referencia = x_inicial - y_inicial, 0
            cls.movimentos.append((x_referencia, y_referencia))

        else:
            x_referencia, y_referencia = 0, y_inicial - x_inicial
            cls.movimentos.append((x_referencia, y_referencia)) 
        
        
        if x_inicial >= y_inverso:
            x_referencia_inversa, y_referencia_inversa = x_inicial - y_inverso, 0
            y_referencia_inversa = 7 - y_referencia_inversa


            cls.movimentos.append((x_referencia_inversa, y_referencia_inversa))

        else:
            x_referencia_inversa, y_referencia_inversa = 0, y_inverso - x_inicial
            y_referencia_inversa = 7 - y_referencia_inversa
            cls.movimentos.append((x_referencia_inversa, y_referencia_inversa)) 
        
        
        
        for cont in range(8):
                x_referencia += 1
                y_referencia += 1
                x_referencia_inversa += 1
                y_referencia_inversa -= 1
                if 0 <= x_referencia <= 7 and 0 <= y_referencia <= 7 and (x_referencia != x_inicial or y_referencia != y_inicial):
                    cls.movimentos.append((x_referencia, y_referencia))
                
                if 0 <= x_referencia_inversa <= 7 and 0 <= y_referencia_inversa <= 7 and (x_referencia_inversa != x_inicial or y_referencia_inversa != y_inicial):
                    cls.movimentos.append((x_referencia_inversa, y_referencia_inversa))
                
        return cls.movimentos

    def movimento_valido(cls, tabuleiro):
        '''
        Verifica se vai ser possivel concluir o movimento devido a algum impedimento no caminho
        '''
        pass


movimentos = Pecas.rainha((5,2))

print(movimentos)


'''

'''