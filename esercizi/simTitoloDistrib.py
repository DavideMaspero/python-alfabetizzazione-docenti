import numpy as np
import matplotlib.pyplot as plt


def estraiPiu(valoreTitolo):
    rndNumero = np.random.random()
    # print "\t", rndNumero
    if rndNumero < 0.5:
        valoreTitolo *= 1.03
    elif rndNumero < 0.8:
        valoreTitolo *= 0.99
    else:
        valoreTitolo *= 1.0
    return valoreTitolo


def estraiMeno(valoreTitolo):
    rndNumero = np.random.random()
    # print "\t", rndNumero
    if rndNumero < 0.3:
        valoreTitolo *= 1.02
    elif rndNumero < 0.5:
        valoreTitolo *= 0.98
    else:
        valoreTitolo *= 1.0
    return valoreTitolo


def estraiUguale(valoreTitolo):
    rndNumero = np.random.random()
    # print "\t", rndNumero
    if rndNumero < 0.5:
        valoreTitolo *= 1.01
    else:
        valoreTitolo *= .99
    return valoreTitolo


def simulazioneTitolo(serieTitolo):
    serieTitolo[1] = estraiUguale(serieTitolo[0])
    for lancio in xrange(2, lanci):
        segno = serieTitolo[lancio - 2] - serieTitolo[lancio - 1]
        if segno < 0.0:
            serieTitolo[lancio] = estraiMeno(serieTitolo[lancio - 1])
        elif segno > 0.0:
            serieTitolo[lancio] = estraiPiu(serieTitolo[lancio - 1])
        else:
            serieTitolo[lancio] = estraiUguale(serieTitolo[lancio - 1])


lanci = input('inserire il numero di giorni ')
simulazioni = input('inserire il numero di simulazioni ')

serieValori = np.empty(simulazioni)
simTitolo = np.empty(lanci)
simTitolo[0] = 1.0

for sim in xrange(simulazioni):
    simulazioneTitolo(simTitolo)
    serieValori[sim] = simTitolo[lanci - 1]

# costruzione istogramma e relativo grafico
istogramma, intervalli = np.histogram(serieValori, bins=100)
print istogramma.size, intervalli.size

plt.grid()
plt.xlabel('valore')
plt.ylabel('frequenza')
plt.plot(istogramma, '-')
plt.show()

# grafico istogramma sfruttando matplotlib
# plt.hist(serieValori, bins=100)
# plt.xlabel('valore')
# plt.ylabel('frequenza')
# plt.show()
