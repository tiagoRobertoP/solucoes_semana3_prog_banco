# This Python file uses the following encoding: utf-8
import os, sys, math

lista =  [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]
TotalTimeFaltas = []
faltas = []
times = []
i = 0

for partida in lista :
    faltas = partida[2]
    time1 = partida[0]
    time2 = partida[1]

    if time1 in times :
        i = 1
        for time in times : 
            if time == time1 :
                times[i] += faltas[0]
            i += 1
    else : 
        times.append(time1)
        times.append(faltas[0])  

    if time2 in times :
        i = 1
        for time in times : 
            if time == time2 :
                times[i] += faltas[1]
            i += 1
    else : 
        times.append(time2)
        times.append(faltas[1])            
    
print ("Total de faltas: " + str(sum(times[1::2]))) 

mais, menos, i = 0, 1000, 0
paisMenos, paisMais = '', ''
for val in times:
    if(type(val) == type(1)):
        if val < menos:
            menos = val
            paisMenos = times[i-1]
        if val > mais:
            mais = val
            paisMais = times[i-1]
    i += 1
    
print('O time com mais faltas  :  ' + str(paisMais))
print('O time com menos faltas  :  ' + str(paisMenos))
    
    