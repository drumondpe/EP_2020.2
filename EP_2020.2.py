# -*- coding: utf-8 -*-

# Projeto EP - Insper 2020.2
# Pedro Gomes de Sá Drumond - 1B.2

# -*- coding: utf-8 -*-

# Projeto EP - Insper 2020.2
# Pedro Gomes de Sá Drumond - 1B.2

#FALTA FAZER:
#

import ramdom
import math
from math import floor

def jogo():
    
    fichas = 100 

    jogando = True
    quantidade_suficiente = True

    resposta = input('Você quer jogar (sim/não)? ') #pergunta ao jogador se ele quer jogar
    resposta = resposta.lower()
    if resposta == 'não': #se a resposta for 'não', deve parar o jogo
        jogando = False

    while(jogando): #começa o loop do jogo
        print('Você começou a jogar!')  
        print('Você tem {} fichas'.format(fichas))

        valor_aposta = int(input('Quanto você deseja apostar? (você possui {} fichas)'.format(fichas))) #aposta a quantia de fichas
        if valor_aposta > fichas:
            valor_aposta = int(input('Você apostou uma quantia que não possui. Quanto você deseja apostar? (você possui {} fichas)'.format(fichas)))

        vencedor_aposta = input('Em quem você aposta? (jogador/banco/empate') #aposta em quem será o vencedor da rodada
        vencedor_aposta = vencedor_aposta.lower()

        ###################### BARALHO #########################

        #BARALHO = [cartas]
        cartas = [] #possuirá as cartas A - K
        naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
        realeza = ['J', 'Q', 'K', 'A']
        baralho = []

        for i in range(2, 11): #talvez mudar para 1
            cartas.append(str(i)) #adiciona numeros de 2-10, convertendo-os para strings
        
        for j in range(4):
            cartas.append(realeza[j]) #vai colocar as cartas de realeza na lista de cartas

        for p in range(4):
            for m in range (13):
                carta = (cartas[m] + 'de' + naipes[p]) #passa por todas as cartas 4x que irão receber os 4 naipes
                baralho.append(carta)

        random.shuffle(baralho) #embaralha as o baralho

        ############## BARALHO #############

        dic_valores_cartas = { #valores das cartas
            'A ' : 1,
            '2 ' : 2,
            '3 ' : 3,
            '4 ' : 4,
            '5 ' : 5,
            '6 ' : 6,
            '7 ' : 7,
            '8 ' : 8,
            '9 ' : 9,
            '10' : 0,
            'J ' : 0,
            'Q ' : 0,
            'K ' : 0
            }

        carta_jogador_1 = baralho[0] #distribui as cartas para os jogadores
        carta_jogador_2 = baralho[1]
        carta_banco_1 = baralho[2]
        carta_banco_2 = baralho[3]

        cartas_distribuidas = [carta_jogador_1, carta_jogador_2, carta_banco_1, carta_banco_2] #faz uma lista com as cartas distribuidas
        valores_cartas_distribuidas = []
        
        for distribuidas in cartas_distribuidas: #atribui os valores das cartas 
            fatiamento = distribuidas[0:2]
            valor_carta_jogador = dic_valores_cartas[fatiamento]
            valores_cartas_distribuidas.append(valor_carta_jogador) #faz uma lista com as cartas distribuidas e seus respectivos valores

        soma_jogador = valores_cartas_distribuidas[0] + valores_cartas_distribuidas[1] #soma a pontuação do jogador
        soma_banco = valores_cartas_distribuidas[2] + valores_cartas_distribuidas[3] #soma a pontuação do banco


        ############ VERIFICAÇÕES ############
        
        ####### Soma deu 8 ou 9
        if soma_jogador == 8 or soma_jogador == 9 or soma_banco == 8 or soma_jogador == 9: #verifica se alguém venceu
            #jogo termina e as apostas são pagas
            if vencedor_aposta == 'jogador' and soma_jogador == 8 or soma_jogador == 9:
                #paga vencedor aposta
                fichas += valor_aposta
            
            elif vencedor_aposta == 'banco' and soma_banco == 8 or soma_banco == 9:
                #paga banco aposta
                paga_banco = valor_aposta * 0.95
                arredonda = floor(paga_banco) #arredonda para baixo
                fichas += arredonda

            elif vencedor_aposta == 'empate' and soma_banco == 8 and soma_jogador == 8 or vencedor_aposta == 'empate' and soma_banco == 9 and soma_jogador == 9 or vencedor_aposta == 'empate' and soma_banco == 9 and soma_jogador == 8 or vencedor_aposta == 'empate' and soma_banco == 8 and soma_jogador == 9 or
                #paga o empate
                #####o empate conta como 9 e 8?
                fichas += valor_aposta * 8

            else:
                #perde o que apostou
                fichas -= valor_aposta

        ####### Soma deu 6 ou 7
        if soma_jogador == 6 or soma_jogador == 7:
            soma_jogador = soma_jogador


        if soma_banco == 6 or soma_banco == 7:                  #if em tudo pois tem que verificar todas as entradas
            soma_jogador = soma_jogador                         #verificar se if e elif estão sendo usados corretamente

        #como continuar a partir daqui também!

        ####### Soma deu menor ou igual a 5
        if soma_jogador <= 5:
            #distribui mais uma carta para o jogador
            carta_jogador_3 = baralho[4]
            fatia = carta_jogador_3[0:2]
            valor_carta_jogador_3 = dic_valores_cartas[fatia] #atribui o valor da carta buscando no dic lá de cima
            soma_jogador += valor_carta_jogador_3 #recalcula a nova soma p/ jogador


        if soma_banco <= 5:
            #distribui mais uma carta para o banco
            carta_banco_3 = baralho[5]
            fatib = carta_banco_3[0:2]
            valor_carta_banco_3 = dic_valores_cartas[fatib] #atribui o valor da carta buscando no dic lá de cima
            soma_banco += valor_carta_banco_3 #recalcula a nova soma p/ banco


        ### Como continuar com esses dois ifs? tem que juntar de algum jeito?