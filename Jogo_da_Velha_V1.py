import random
jogo_da_velha = [['', '', ''], ['', '', ''], ['', '', '']]
jogo = 1

def mostrar_jogo_da_velha(valores):
  print(f"""
  {(valores[0][0]).center(3)} : {(valores[0][1]).center(3)} : {(valores[0][2]).center(3)}
  ----+-----+----
  {(valores[1][0]).center(3)} : {(valores[1][1]).center(3)} : {(valores[1][2]).center(3)}
  ----+-----+----
  {(valores[2][0]).center(3)} : {(valores[2][1]).center(3)} : {(valores[2][2]).center(3)}""")

def jogada_da_maquina():
  a = random.randrange(0, 3)
  b = random.randrange(0, 3)
  if '' in jogo_da_velha[0] or '' in jogo_da_velha[1] or '' in jogo_da_velha[2]:
    if jogo_da_velha[a][b] == '':
      posicao1 = a
      posicao2 = b
      return posicao1, posicao2
    else:
      return jogada_da_maquina()
  else:
    return 'acabou'

def jogada_player():
  c = int(input('Digite o número da linha onde quer fazer sua jogada: ')) - 1
  d = int(input('Digite o número da coluna onde quer fazer sua jogada: ')) - 1
  if jogo_da_velha[c][d] == '':
    posicao1 = c
    posicao2 = d
    return posicao1, posicao2
  else:
    print("A posição escolhida já está ocupada, escolha outro lugar")
    return jogada_player()

def verificar_vencedor():
  jogar = 1
  ganhador = "Empate"
  if jogo_da_velha[0] == ['O', 'O', 'O'] or jogo_da_velha[1] == ['O', 'O', 'O'] or jogo_da_velha[2] == ['O', 'O', 'O']:
    ganhador = "CPU venceu"
    jogar = 0
  elif jogo_da_velha[0] == ['X', 'X', 'X'] or jogo_da_velha[1] == ['X', 'X', 'X'] or jogo_da_velha[2] == ['X', 'X', 'X']:
    ganhador = "Jogador venceu"
    jogar = 0
  elif jogo_da_velha[0][0] == jogo_da_velha[1][0] == jogo_da_velha[2][0]:
    if jogo_da_velha[0][0] == 'O':
      ganhador = 'CPU venceu'
      jogar = 0
    elif jogo_da_velha[0][0] == 'X':
      ganhador = 'Jogador venceu'
      jogar = 0
    elif jogo_da_velha[0][0] == '':
      ganhador = 'Empate'
      jogar = 1
  elif jogo_da_velha[0][1] == jogo_da_velha[1][1] == jogo_da_velha[2][1]:
    if jogo_da_velha[0][1] == 'O':
      ganhador = 'CPU venceu'
      jogar = 0
    elif jogo_da_velha[0][1] == 'X':
      ganhador = 'Jogador venceu'
      jogar = 0
    elif jogo_da_velha[0][1] == '':
      ganhador = 'Empate'
      jogar = 1
  elif jogo_da_velha[0][2] == jogo_da_velha[1][2] == jogo_da_velha[2][2]:
    if jogo_da_velha[0][2] == 'O':
      ganhador = 'CPU venceu'
      jogar = 0
    elif jogo_da_velha[0][2] == 'X':
      ganhador = 'Jogador venceu'
      jogar = 0
    elif jogo_da_velha[0][2] == '':
      ganhador = 'Empate'
      jogar = 1
  elif jogo_da_velha[0][0] == jogo_da_velha[1][1] == jogo_da_velha[2][2]:
    if jogo_da_velha[0][0] == 'O':
      ganhador = 'CPU venceu'
      jogar = 0
    elif jogo_da_velha[0][0] == 'X':
      ganhador = 'Jogador venceu'
      jogar = 0
    elif jogo_da_velha[0][0] == '':
      ganhador = 'Empate'
      jogar = 1
  elif jogo_da_velha[0][2] == jogo_da_velha[1][1] == jogo_da_velha[2][0]:
    if jogo_da_velha[0][2] == 'O':
      ganhador = 'CPU venceu'
      jogar = 0
    elif jogo_da_velha[0][2] == 'X':
      ganhador = 'Jogador venceu'
      jogar = 0
    elif jogo_da_velha[0][2] == '':
      ganhador = 'Empate'
      jogar = 1
  return ganhador, jogar

while jogo == 1:

  mostrar_jogo_da_velha(jogo_da_velha)
  jogador = jogada_player()
  jogo_da_velha[jogador[0]][jogador[1]] = 'X'
  CPU = jogada_da_maquina()
  if CPU != 'acabou':
    jogo_da_velha[CPU[0]][CPU[1]] = 'O'
  resultado = verificar_vencedor()
  jogo = resultado[1]
  vencedor = resultado[0]

  if '' not in jogo_da_velha[0] and '' not in jogo_da_velha[1] and '' not in jogo_da_velha[2]:
    jogo = 0
    if vencedor != 'Jogador venceu' and vencedor != 'CPU venceu':
      vencedor = 'Empate'

print(f'O resultado da partida foi: {vencedor}')
mostrar_jogo_da_velha(jogo_da_velha)