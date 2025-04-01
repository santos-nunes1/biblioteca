import numpy as np
import pandas as pd

def estatistica_descritiva(a):
    print(a)
    pandas_a =  pd.Series(a)

    #media
    media = np.mean(a)
    print ('Media: ', media)

    #mediana
    mediana = np.median(a)
    print ('Mediana: ', mediana)

    #amplitude: 
    amplitude = max(a) - min(a)
    print ('Amplitude: ', amplitude)

    #quantis:
    print("QUANTIS: ")
    q1 = pandas_a.quantile(q=0.25)
    print('q1: ', q1)

    q2 = pandas_a.quantile(q=0.50)
    print('q2: ', q2)

    q3 = pandas_a.quantile(q=0.75)
    print('q3: ', q3)

    #variancia:
    variancia = pandas_a.var()
    print('Variancia: ', variancia)

    #desvio padrão: 
    desvio_padrao = pandas_a.std()
    print('Desvio Padrão: ', desvio_padrao)

    #coeficiente de variação
    coeficiente_variacao = desvio_padrao/media
    print('Coeficiente de Variação: ', coeficiente_variacao)

a = [5,4,7,8,3,4,2,7,9,7,6,18]
estatistica_descritiva(a)