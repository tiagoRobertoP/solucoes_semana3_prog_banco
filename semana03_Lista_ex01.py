# This Python file uses the following encoding: utf-8
import os, sys, math

lista_a = [3,6,4,7,8]
lista_b = [3,6,4,7,8]

for i in range(len(lista_a)):
    if lista_b[i] == lista_a[i]:
        continue
    else:
        print('As listas são diferentes')
        exit()
print('As listas são iguais')