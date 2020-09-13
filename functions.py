
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project:¿Qué estrategia de inversión propondrías si tu trabajo fuera administrar 1 Millón de pesos? -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: Irenereval                                                                                  -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository:https://github.com/irenereval/Myst_if705239                                              -- #
# -- --------------------------------------------------------------------------------------------------- -- #

# -- ------------------------------------------------------------------------------------------Librerias -- #
import pandas as pd
import numpy as np
import time as time
import yfinance as yf
import data as dataa
from data import archivos

# -- -------------------------------------------------------------------------------------------paso 1.1 -- #
#--Lista de archivos a leer
# -- -------------------------------------------------------------------------------------------paso 1.2 -- #
#Leer todos los archivos y guaradarlos en un diccionario
#Crear un diccionario para todos los dato
# -- -------------------------------------------------------------------------------------------paso 1.3 -- #
#Construir el vector de formas apartir del vector nombre de archivos
def funcion_fechas(archivos):
    # Etiquetas para data frame y Yfinance
    t_fechas = [i.strftime('%d-%m-%y') for i in sorted([pd.to_datetime(i[8:]).date() for i in archivos])]

    # Llista con fechas ordenadas
    i_fechas = [i.strftime('%d%m%y') for i in sorted([pd.to_datetime(i[8:]).date() for i in archivos])]
    t_i_fechas = {'i_fechas': i_fechas, 't_fechas':t_fechas}
    #variable que retorna para usar en main
    return t_i_fechas

# -- -------------------------------------------------------------------------------------------paso 1.4 -- #
#Construir el vector de tickets utilizando yahoo finance
def funcion_tickers(archivos,data_archivos):
    tickers = []
    for i in archivos:
        # i = archivos[0]
        l_tickers = list(data_archivos[i]['Ticker'])
        [tickers.append(i + '.MX') for i in l_tickers]

    global_tickers = np.unique(tickers).tolist()

    # Ajustes de tickers
    global_tickers = [i.replace('GFREGIOO.MX', 'RA.MX') for i in global_tickers]
    global_tickers = [i.replace('MEXCHEM.MX', 'ORBIA.MX') for i in global_tickers]
    global_tickers = [i.replace('LIVEPOLC.1.MX', 'LIVEPOLC-1.MX') for i in global_tickers]

    # Eliminar entradas de efectivo MXN, USD
    [global_tickers.remove(i) for i in ['MXN.MX', 'USD.MX', 'KOFL.MX']]
    return global_tickers
# -- -------------------------------------------------------------------------------------------paso 1.5 -- #
#Descargar y acomodar todos los datos
def funcio_descargar(global_tickers,fechas):
    inicio = time.time()
    data_yf = yf.download(global_tickers, start='2017-08-21', end='2020-08-22', actions=False,
                          group_by='close', interval='1d', auto_adjust=False, prepost=False, threads=True)
    print('se tardo', time.time() - inicio, 'segundos')

    # Convertir columnas de fechas
    data_close = pd.DataFrame({i: data_yf[i]['Close'] for i in global_tickers})
    # Tomar solo las fechas de interes

    ic_fechas = sorted(list(set(data_close.index.astype(str).tolist()) & set(fechas['i_fechas'])))
    # encontrar los precios
    total_precios = data_close.iloc[[int(np.where(data_close.index == i)[0]) for i in ic_fechas]]

    # Ordenar columnas lexicograficamente
    total_precios = total_precios.reindex(sorted(total_precios.columns), axis=1)
    #print para debuguear esta corriendo hasta el final de la funcion
    print("hola")
    return total_precios

# -- -------------------------------------------------------------------------------------------paso 1.6 -- #
#Obtener posiciones historicas
# -- -------------------------------------------------------------------------------------------paso 1.7 -- #

# -- -------------------------------------------------------------------------------------------paso 1.8 -- #

# -- -------------------------------------------------------------------------------------------paso 1.9 -- #