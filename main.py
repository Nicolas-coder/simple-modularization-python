#main

import aleatorio as a
import media as m

vetor = a.geraListaInt(10)

media = m.media(vetor)
mediana = m.mediana(vetor)
moda = m.moda(vetor)

print("Meu vetor: ")
ordenado = sorted(vetor)
print(ordenado)

print("A media do vetor eh:", media)
print("A mediana do vetor eh:", mediana)
print("A moda do vetor eh:", moda)