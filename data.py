"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project:¿Qué estrategia de inversión propondrías si tu trabajo fuera administrar 1 Millón de pesos? -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: Irenereval                                                                                  -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository:https://github.com/irenereval/Myst_if705239                                              -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
#Importar librerias
from os import listdir, path
from os.path import isfile, join
import pandas as pd
import numpy as np
import time
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
# -- -------------------------------------------------------------------------------------------paso 1.1 -- #
#-- Lista de archivos a leer
#Ruta de donde estan los archivos
abspath = path.abspath('files/NAFTRAC_holdings')
archivos = [f[:-4] for f in listdir(abspath) if isfile(join(abspath, f))]

# -- -------------------------------------------------------------------------------------------paso 1.2 -- #
#Leer todos los archivos y guaradarlos en un diccionario
#Crear un diccionario para todos los datos
data_archivos = {}
# Ordernar archivos por fecha
archivos = sorted(archivos, key=lambda t: datetime.strptime(t[8:], '%d%m%y'))

for i in archivos:
    #Leer los archivos despues del 2do renglon
    data = pd.read_csv('files/NAFTRAC_holdings/' + i + '.csv', skiprows=2, header=None)

    #Renombrar las columnas con el 2do renglon
    data.columns = list(data.iloc[0, :])

    #Eliminar columnas que no son NAN
    data = data.loc[:, pd.notnull(data.columns)]

    #Quitar el primer renglon que se repite
    data = data.iloc[1:-1].reset_index(drop=True, inplace=False)

    #Quitar las comas en la columna de precios
    data['Precio'] = [i.replace(',', '') for i in data['Precio']]

    #Quitar asteriscos en la columna de  Ticker
    data['Ticker'] = [i.replace('*', '') for i in data['Ticker']]

    #Hacer conversion  de tipos de columnas a numericas
    convert_dict = {'Ticker': str, 'Nombre': str, 'Peso (%)': float, 'Precio': float}
    data = data.astype(convert_dict)

    #Convertir a decimal la columna de Peso
    data['Peso (%)'] = data['Peso (%)']/100

    #Guardar en diccionario
    data_archivos[i] = data

# -- -------------------------------------------------------------------------------------------paso 1.3 -- #
#Construir el vector de formas apartir del vector nombre de archivos

# -- -------------------------------------------------------------------------------------------paso 1.4 -- #
#Construir el vector de tickets utilizando yahoo finance

# KOFL pasar a Cash
# -- -------------------------------------------------------------------------------------------paso 1.5 -- #
#Descargar y acomodar todos los precios historicos

# -- -------------------------------------------------------------------------------------------paso 1.6 -- #


