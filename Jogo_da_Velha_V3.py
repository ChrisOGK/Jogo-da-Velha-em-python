jogo_da_velha = {1 : '', 2 : '', 3 : '', 4 : '', 5 : '', 6 : '', 7 : '', 8 : '', 9 : ''}
jogo = 1

# Gerador de pontos baseado nas possíveis jogadas
def verificar_jogadas_possiveis(tabuleiro):
  jogada_pontos = {}
  for a in range(1, 10):

    if a == 1:
      if tabuleiro[1] == '':
        pontos = 1
        if tabuleiro[2] == 'O' or tabuleiro[3] == 'O':
          pontos += 2
        if tabuleiro[4] == 'O' or tabuleiro[7] == 'O':
          pontos += 2
        if tabuleiro[5] == 'O' or tabuleiro[9] == 'O':
          pontos += 2 
        if tabuleiro[2] == 'X' or tabuleiro[3] == 'X':
          pontos -= 1
        if tabuleiro[4] == 'X' or tabuleiro[7] == 'X':
          pontos -= 1
        if tabuleiro[5] == 'X' or tabuleiro[9] == 'X':
          pontos -= 1
        if (tabuleiro[2] == 'O' and tabuleiro[3] == 'O') or (tabuleiro[4] == 'O' and tabuleiro[7] == 'O') or (tabuleiro[5] == 'O' and tabuleiro[9] == 'O'):
          pontos += 100
        if (tabuleiro[2] == 'X' and tabuleiro[3] == 'X') or (tabuleiro[4] == 'X' and tabuleiro[7] == 'X') or (tabuleiro[5] == 'X' and tabuleiro[9] == 'X'):
          pontos += 50
        jogada_pontos[1] = pontos
    
    if a == 2:
      if tabuleiro[2] == '':
        pontos = 0
        if tabuleiro[1] == 'O' or tabuleiro[3] == 'O':
          pontos += 3
        if tabuleiro[5] == 'O' or tabuleiro[8] == 'O':
          pontos += 3
        if tabuleiro[1] == 'X' or tabuleiro[3] == 'X':
          pontos -= 1
        if tabuleiro[5] == 'X' or tabuleiro[8] == 'X':
          pontos -= 1
        if (tabuleiro[1] == 'O' and tabuleiro[3] == 'O') or (tabuleiro[5] == 'O' and tabuleiro[8] == 'O'):
          pontos += 100
        if (tabuleiro[1] == 'X' and tabuleiro[3] == 'X') or (tabuleiro[5] == 'X' and tabuleiro[8] == 'X'):
          pontos += 50
        jogada_pontos[2] = pontos

    if a == 3:
      if tabuleiro[3] == '':
        pontos = 1
        if tabuleiro[2] == 'O' or tabuleiro[1] == 'O':
          pontos += 2
        if tabuleiro[6] == 'O' or tabuleiro[9] == 'O':
          pontos += 2
        if tabuleiro[5] == 'O' or tabuleiro[7] == 'O':
          pontos += 2 
        if tabuleiro[2] == 'X' or tabuleiro[1] == 'X':
          pontos -= 1
        if tabuleiro[6] == 'X' or tabuleiro[9] == 'X':
          pontos -= 1
        if tabuleiro[5] == 'X' or tabuleiro[7] == 'X':
          pontos -= 1
        if (tabuleiro[2] == 'O' and tabuleiro[1] == 'O') or (tabuleiro[6] == 'O' and tabuleiro[9] == 'O') or (tabuleiro[5] == 'O' and tabuleiro[7] == 'O'):
          pontos += 100
        if (tabuleiro[2] == 'X' and tabuleiro[1] == 'X') or (tabuleiro[6] == 'X' and tabuleiro[9] == 'X') or (tabuleiro[5] == 'X' and tabuleiro[7] == 'X'):
          pontos += 50
        jogada_pontos[3] = pontos
    
    if a == 4:
      if tabuleiro[4] == '':
        pontos = 0
        if tabuleiro[5] == 'O' or tabuleiro[6] == 'O':
          pontos += 3
        if tabuleiro[1] == 'O' or tabuleiro[7] == 'O':
          pontos += 3
        if tabuleiro[5] == 'X' or tabuleiro[6] == 'X':
          pontos -= 1
        if tabuleiro[1] == 'X' or tabuleiro[7] == 'X':
          pontos -= 1
        if (tabuleiro[5] == 'O' and tabuleiro[6] == 'O') or (tabuleiro[1] == 'O' and tabuleiro[7] == 'O'):
          pontos += 100
        if (tabuleiro[5] == 'X' and tabuleiro[6] == 'X') or (tabuleiro[1] == 'X' and tabuleiro[7] == 'X'):
          pontos += 50
        jogada_pontos[4] = pontos

    if a == 5:
      if tabuleiro[5] == '':
        pontos = 3
        if tabuleiro[4] == 'O' or tabuleiro[6] == 'O':
          pontos += 2
        if tabuleiro[2] == 'O' or tabuleiro[8] == 'O':
          pontos += 2
        if tabuleiro[1] == 'O' or tabuleiro[9] == 'O':
          pontos += 2 
        if tabuleiro[4] == 'X' or tabuleiro[6] == 'X':
          pontos -= 1
        if tabuleiro[2] == 'X' or tabuleiro[8] == 'X':
          pontos -= 1
        if tabuleiro[1] == 'X' or tabuleiro[9] == 'X':
          pontos -= 1
        if (tabuleiro[4] == 'O' and tabuleiro[6] == 'O') or (tabuleiro[2] == 'O' and tabuleiro[8] == 'O') or (tabuleiro[1] == 'O' and tabuleiro[9] == 'O'):
          pontos += 100
        if (tabuleiro[4] == 'X' and tabuleiro[6] == 'X') or (tabuleiro[2] == 'X' and tabuleiro[8] == 'X') or (tabuleiro[1] == 'X' and tabuleiro[9] == 'X'):
          pontos += 50

        jogada_pontos[5] = pontos
    
    if a == 6:
      if tabuleiro[6] == '':
        pontos = 0
        if tabuleiro[4] == 'O' or tabuleiro[5] == 'O':
          pontos += 3
        if tabuleiro[3] == 'O' or tabuleiro[9] == 'O':
          pontos += 3
        if tabuleiro[4] == 'X' or tabuleiro[5] == 'X':
          pontos -= 1
        if tabuleiro[3] == 'X' or tabuleiro[9] == 'X':
          pontos -= 1
        if (tabuleiro[4] == 'O' and tabuleiro[5] == 'O') or (tabuleiro[3] == 'O' and tabuleiro[9] == 'O'):
          pontos += 100
        if (tabuleiro[4] == 'X' and tabuleiro[5] == 'X') or (tabuleiro[3] == 'X' and tabuleiro[9] == 'X'):
          pontos += 50
        jogada_pontos[6] = pontos

    if a == 7:
      if tabuleiro[7] == '':
        pontos = 1
        if tabuleiro[8] == 'O' or tabuleiro[9] == 'O':
          pontos += 2
        if tabuleiro[4] == 'O' or tabuleiro[1] == 'O':
          pontos += 2
        if tabuleiro[5] == 'O' or tabuleiro[3] == 'O':
          pontos += 2 
        if tabuleiro[8] == 'X' or tabuleiro[9] == 'X':
          pontos -= 1
        if tabuleiro[4] == 'X' or tabuleiro[1] == 'X':
          pontos -= 1
        if tabuleiro[5] == 'X' or tabuleiro[3] == 'X':
          pontos -= 1
        if (tabuleiro[8] == 'O' and tabuleiro[9] == 'O') or (tabuleiro[4] == 'O' and tabuleiro[1] == 'O') or (tabuleiro[5] == 'O' and tabuleiro[3] == 'O'):
          pontos += 100
        if (tabuleiro[8] == 'X' and tabuleiro[9] == 'X') or (tabuleiro[4] == 'X' and tabuleiro[1] == 'X') or (tabuleiro[5] == 'X' and tabuleiro[3] == 'X'):
          pontos += 50
        jogada_pontos[7] = pontos
    
    if a == 8:
      if tabuleiro[8] == '':
        pontos = 0
        if tabuleiro[7] == 'O' or tabuleiro[9] == 'O':
          pontos += 3
        if tabuleiro[5] == 'O' or tabuleiro[2] == 'O':
          pontos += 3
        if tabuleiro[7] == 'X' or tabuleiro[9] == 'X':
          pontos -= 1
        if tabuleiro[5] == 'X' or tabuleiro[2] == 'X':
          pontos -= 1
        if (tabuleiro[7] == 'O' and tabuleiro[9] == 'O') or (tabuleiro[5] == 'O' and tabuleiro[2] == 'O'):
          pontos += 100
        if (tabuleiro[7] == 'X' and tabuleiro[9] == 'X') or (tabuleiro[5] == 'X' and tabuleiro[2] == 'X'):
          pontos += 50
        jogada_pontos[8] = pontos
        
    if a == 9:
      if tabuleiro[9] == '':
        pontos = 1
        if tabuleiro[7] == 'O' or tabuleiro[8] == 'O':
          pontos += 2
        if tabuleiro[6] == 'O' or tabuleiro[3] == 'O':
          pontos += 2
        if tabuleiro[5] == 'O' or tabuleiro[1] == 'O':
          pontos += 2 
        if tabuleiro[7] == 'X' or tabuleiro[8] == 'X':
          pontos -= 1
        if tabuleiro[6] == 'X' or tabuleiro[3] == 'X':
          pontos -= 1
        if tabuleiro[5] == 'X' or tabuleiro[1] == 'X':
          pontos -= 1 
        if (tabuleiro[7] == 'O' and tabuleiro[8] == 'O') or (tabuleiro[6] == 'O' and tabuleiro[3] == 'O') or (tabuleiro[5] == 'O' and tabuleiro[1] == 'O'):
          pontos += 100
        if (tabuleiro[7] == 'X' and tabuleiro[8] == 'X') or (tabuleiro[6] == 'X' and tabuleiro[3] == 'X') or (tabuleiro[5] == 'X' and tabuleiro[1] == 'X'):
          pontos += 50
        jogada_pontos[9] = pontos
  return jogada_pontos

#Verifica as pontuações e decide qual a melhor jogada
def verificar_pontos(dicionario):
  valor = 0
  if jogo_da_velha[7] == 'X' and jogo_da_velha[3] == 'X' and jogo_da_velha[4] == '':
    return 4
  elif jogo_da_velha[1] == 'X' and jogo_da_velha[9] == 'X' and jogo_da_velha[6] == '':
    return 6
  elif jogo_da_velha[5] == 'X' and jogo_da_velha[1] == 'X' and jogo_da_velha[7] == '':
    return 7
  else:
    for jogada, pontos in dicionario.items():
      if valor <= pontos:
        valor = pontos
        chave_jogada = jogada

  return chave_jogada

#Função para escolha de quem vai jogar primeiro
def escolha_primeiro():
  escolha = input('Escolha quem vai ir primeiro:\n1.Máquina\n2.Você\n')
  if escolha == '1' or escolha == '2':
    return escolha
  else:
    print('Escolha inválida tente de novo')
    return escolha_primeiro()

#Mostra o tabuleiro do jogo
def mostrar_jogo_da_velha(valores):
  print(f""" Tabuleiro Real
  {(valores[7].center(3))} : {(valores[8]).center(3)} : {(valores[9].center(3))} 
  ----+-----+----
  {(valores[4]).center(3)} : {(valores[5]).center(3)} : {(valores[6].center(3))} 
  ----+-----+----
  {(valores[1]).center(3)} : {(valores[2]).center(3)} : {(valores[3]).center(3)}""")

#Verificar se ainda existe jogadas possíveis para serem feitas
def verificar_tabuleiro():
  jogar = 0
  if '' in jogo_da_velha.values():
    jogar = 1
  return jogar

#Jogada da máquina
def jogada_da_maquina():
  jogar = verificar_tabuleiro()
  if jogar == 1:
    dic = verificar_jogadas_possiveis(jogo_da_velha)
    chave = verificar_pontos(dic)
    return chave

#Jogada do jogador
def jogada_player():
  jogada = int(input('Digite onde quer jogar: '))
  if jogo_da_velha[jogada] == '':
    chave = jogada
    return chave
  else:
    print("A posição escolhida já está ocupada, escolha outro lugar")
    return jogada_player()

#Verifica se alguém venceu
def verificar_vencedor():
  jogar = 1
  ganhador = "Empate"
  if (jogo_da_velha[7] == jogo_da_velha[8] == jogo_da_velha[9] == 'X') or (jogo_da_velha[4] == jogo_da_velha[5] == jogo_da_velha[6] == 'X') or (jogo_da_velha[1] == jogo_da_velha[2] == jogo_da_velha[3] == 'X') or (jogo_da_velha[7] == jogo_da_velha[5] == jogo_da_velha[3] == 'X') or (jogo_da_velha[1] == jogo_da_velha[5] == jogo_da_velha[9] == 'X') or (jogo_da_velha[1] == jogo_da_velha[4] == jogo_da_velha[7] == 'X') or (jogo_da_velha[2] == jogo_da_velha[5] == jogo_da_velha[8] == 'X') or (jogo_da_velha[3] == jogo_da_velha[6] == jogo_da_velha[9] == 'X'):
    ganhador = 'Jogador venceu'
    jogar = 0
  elif (jogo_da_velha[7] == jogo_da_velha[8] == jogo_da_velha[9] == 'O') or (jogo_da_velha[4] == jogo_da_velha[5] == jogo_da_velha[6] == 'O') or (jogo_da_velha[1] == jogo_da_velha[2] == jogo_da_velha[3] == 'O') or (jogo_da_velha[7] == jogo_da_velha[5] == jogo_da_velha[3] == 'O') or (jogo_da_velha[1] == jogo_da_velha[5] == jogo_da_velha[9] == 'O') or (jogo_da_velha[1] == jogo_da_velha[4] == jogo_da_velha[7] == 'O') or (jogo_da_velha[2] == jogo_da_velha[5] == jogo_da_velha[8] == 'O') or (jogo_da_velha[3] == jogo_da_velha[6] == jogo_da_velha[9] == 'O'):
    ganhador = 'Máquina venceu'
    jogar = 0
  elif verificar_tabuleiro() == 0:
    ganhador = 'Empate'
    jogar = 0
  return ganhador, jogar


primeiro = escolha_primeiro()

if primeiro == '1':
  while jogo == 1:
    print(f""" Tabuleiro de referência:
    {'7'.center(3)} : {'8'.center(3)} : {'9'.center(3)} 
    ----+-----+----
    {'4'.center(3)} : {'5'.center(3)} : {'6'.center(3)} 
    ----+-----+----
    {'1'.center(3)} : {'2'.center(3)} : {'3'.center(3)}""")
    CPU = jogada_da_maquina()
    jogo_da_velha[CPU] = 'O'
    mostrar_jogo_da_velha(jogo_da_velha)
    resultado = verificar_vencedor()
    if resultado[1] != 0:
      jogador = jogada_player()
      jogo_da_velha[jogador] = 'X'
    jogo = resultado[1]
    vencedor = resultado[0]

elif primeiro == '2':
  while jogo == 1:
    print(f""" Tabuleiro de referência:
    {'7'.center(3)} : {'8'.center(3)} : {'9'.center(3)} 
    ----+-----+----
    {'4'.center(3)} : {'5'.center(3)} : {'6'.center(3)} 
    ----+-----+----
    {'1'.center(3)} : {'2'.center(3)} : {'3'.center(3)}""")
    mostrar_jogo_da_velha(jogo_da_velha)
    jogador = jogada_player()
    jogo_da_velha[jogador] = 'X'
    resultado = verificar_vencedor()
    CPU = jogada_da_maquina()
    if resultado[1] != 0:
      jogo_da_velha[CPU] = 'O'
    resultado = verificar_vencedor()
    jogo = resultado[1]
    vencedor = resultado[0]
    mostrar_jogo_da_velha(jogo_da_velha)

print(f'O resultado da partida foi: {vencedor}')