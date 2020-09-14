# -- --------------------------------------------------------------------------------------------------- -- #
# -- project:¿Qué estrategia de inversión propondrías si tu trabajo fuera administrar 1 Millón de pesos? -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: Irenereval                                                                                  -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository:https://github.com/irenereval/Myst_if705239                                              -- #
# -- --------------------------------------------------------------------------------------------------- -- #

# -- ------------------------------------------------------------------------------------------Librerias -- #
import data as datamain
import functions as functionmain
import pandas as pd
import numpy as np
# -- -------------------------------------------------------------------------------------------paso 1.1 -- #
#-- Lista de archivos a leer
archivosmain = datamain.archivos
# -- -------------------------------------------------------------------------------------------paso 1.2 -- #
#Leer todos los archivos y guaradarlos en un diccionario
data_archivos_main = datamain.data_archivos
#Crear un diccionario para todos los dato
fechasmain = functionmain.funcion_fechas(archivos=archivosmain)
print(fechasmain['t_fechas'][0:5])
# -- -------------------------------------------------------------------------------------------paso 1.3 -- #
#Construir el vector de formas apartir del vector nombre de archivos
# -- -------------------------------------------------------------------------------------------paso 1.4 -- #
#Construir el vector de tickets utilizando yahoo finance
global_tickers_main = functionmain.funcion_tickers(archivos=archivosmain,data_archivos=data_archivos_main)
print(global_tickers_main[0:5])
# -- -------------------------------------------------------------------------------------------paso 1.5 -- #
#Descargar y acomodar todos los datos
total_preciosmain = functionmain.funcio_descargar(global_tickers= global_tickers_main,fechas= fechasmain)

# -- -------------------------------------------------------------------------------------------paso 1.6 -- #
#Iniciar con Pasiva

# -- -------------------------------------------------------------------------------------------paso 1.7 -- #

# -- -------------------------------------------------------------------------------------------paso 1.8 -- #

# -- -------------------------------------------------------------------------------------------paso 1.9 -- #
