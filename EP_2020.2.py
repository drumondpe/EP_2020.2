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

