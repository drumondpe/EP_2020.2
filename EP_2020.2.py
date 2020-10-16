# -*- coding: utf-8 -*-

# Projeto EP - Insper 2020.2
# Pedro Gomes de Sá Drumond - 1B.2


import random
import math
from math import floor

def jogo():
    
    fichas = 100 

    jogando = True
    quantidade_suficiente = True
    outra_carta = False

    ############ Funções ############ 

    def verifica_necessidade(soma_jogador, soma_banco, outra_carta):
        if soma_jogador < 8:
            outra_carta = True
                
        if soma_banco < 8:
            outra_carta = True
        return outra_carta

    def distribui_mais_carta(soma_jogador, soma_banco, outra_carta): #distribui mais uma carta caso não alcance 5
        if soma_jogador <= 5:
            #distribui mais uma carta para o jogador
            carta_jogador_3 = baralho[4]
            fatia = carta_jogador_3[0:2]
            valor_carta_jogador_3 = dic_valores_cartas[fatia] #atribui o valor da carta buscando no dic lá de cima
            soma_jogador += valor_carta_jogador_3 #recalcula a nova soma p/ jogador
            print('O jogador recebeu a carta {} '.format(baralho[4]))
            print('A somatória do jogador deu: {}'.format(soma_jogador))

        if soma_banco <= 5:
            #distribui mais uma carta para o banco
            carta_banco_3 = baralho[5]
            fatib = carta_banco_3[0:2]
            valor_carta_banco_3 = dic_valores_cartas[fatib] #atribui o valor da carta buscando no dic lá de cima
            soma_banco += valor_carta_banco_3 #recalcula a nova soma p/ banco
            print('O banco recebeu a carta {} '.format(baralho[5]))
            print('A somatória do banco deu: {}'.format(soma_banco))

        return soma_jogador, soma_banco

    def verifica_vencedor(soma_jogador, soma_banco): #rever pois deve ser quem chagar mais perto de 9

        if soma_jogador > soma_banco:
            vencedor_jogo = 'jogador'                                                     

        elif soma_banco > soma_jogador:
            vencedor_jogo = 'banco'

        else:
            vencedor_jogo = 'empate'

        return vencedor_jogo



    def paga_aposta(vencedor_jogo, fichas):
                
        if vencedor_jogo == vencedor_aposta: #jogador acertou quem ganhou

            if vencedor_jogo == 'jogador': #paga quantia de jogador
                fichas += valor_aposta
                    
            elif vencedor_jogo == 'banco': #paga quantia de banco
                paga_banco = valor_aposta * 0.95
                arredonda = floor(paga_banco) #arredonda para baixo
                fichas += arredonda
                    
            elif vencedor_jogo == 'empate': #paga quantia de empate
                fichas += valor_aposta * 8


        else:
            #perde o que apostou
            fichas -= valor_aposta
                
        return fichas
