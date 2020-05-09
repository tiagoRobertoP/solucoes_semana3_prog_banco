# This Python file uses the following encoding: utf-8
import os, sys, math, string

voltas = 3
corredores = 2
dicionario = {}

def volta():
    listaA = []
    for i in range(voltas):
        listaA.append((input()))
    return listaA 

while corredores > 0:
  nome = input('Digite o nome do corredor:')
  dicionario[nome] = volta()
  corredores -= 1

intervalo, nomes, i = [], [], 0
menorTempo = [10000, 0, '']
print(menorTempo[0])
for jogador in dicionario:
  aux = []
  for i in range(len(dicionario[jogador])):
    if i != 0:
      tempo1 = dicionario[jogador][i]
      tempo2 = dicionario[jogador][i-1]
      if int(menorTempo[0]) > int(tempo1) - int(tempo2):
        menorTempo[0] = dicionario[jogador][i] - dicionario[jogador][i-1]
        menorTempo[1] = i+1
        menorTempo[2] = jogador
      aux.append(dicionario[jogador][i] - dicionario[jogador][i-1]) 
  i += 1
  intervalo += [aux]
  nomes.append(jogador)

print('\nMelhor volta: ')
print('Corredor:', menorTempo[2])
print('Volta:', menorTempo[1])
print('Tempo:', menorTempo[0], 'segundos\n')

#Melhor corredor:
print('Melhor tempos:')
total = []
i = 0
for interv in intervalo:
  total.append([sum(interv), nomes[i]])
  i+= 1

total.sort()
for corredores in total:
  print(corredores[1], ':', corredores[0], 'segundos')