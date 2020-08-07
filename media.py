#media, mediana e moda
'''
JEITO FACIL DE CALCULAR A MEDIA, MEDIANA E MODA DE UM VETOR:
from statistics import *

mean(vetor) #calcula a media
median(vetor) #calcula a mediana
mode(vetor) #calcula a moda

'''

#JEITO DIFICIL KKK:

def media(vetor):
	#media = mean(vetor)
	media = sum(vetor)/len(vetor)
	return media

def mediana(vetor):
	#mediana = median(vetor)
	vetor_ordenado = sorted(vetor)
	tamanho = len(vetor)
	#descobrir se eh par ou impar
	if tamanho % 2 == 0:
		mediana = (vetor_ordenado[int(tamanho/2)]+vetor_ordenado[int((tamanho/2)-1)])/2
	elif tamanho % 2 != 0:
		mediana = vetor_ordenado[int((tamanho/2))]
	return mediana

def moda(vetor):
	#moda = mode(lista)
	vetor_dic = {}
	for l in vetor:
		if l not in vetor_dic:
			vetor_dic[l] = 1
		else:
			vetor_dic[l] += 1

	maior_repeticao = max(vetor_dic.values())

	for i in vetor_dic:
		if vetor_dic[i] == maior_repeticao:
			moda = i

	return moda