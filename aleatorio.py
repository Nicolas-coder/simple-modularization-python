import random

def geraListaInt(tam):
	vetor = []
	for i in range(tam):
		vetor.append(random.randint(0, tam))
	return vetor