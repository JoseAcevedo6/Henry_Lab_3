# Se importa pandas para el etl de la data.
import pandas as pd

# Se asigna el token de la API a una variable. Acceso al token mediante url='https://datosabiertos.enacom.gob.ar/developers/'.
auth_key = 'VLfOEIZ6ycFUpYvmE9Qr6edhHbeZ5MEPRCKnudf9'

# Se asigna las URL's de la data seleccionada a variables
accseso_por_100_hogares = f'http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/PENET-DEL-INTER-FIJO-51614/data.csv/?auth_key={auth_key}'
velocidad_bajada_por_rangos = f'http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/ACCES-A-INTER-FIJO-23248/data.csv/?auth_key={auth_key}'
velocidad_media_de_bajada = f'http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/VELOC-PROME-DE-BAJAD-DE/data.csv/?auth_key={auth_key}'
acceso_por_tecnologias = f'http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/ACCES-A-INTER-FIJO-POR/data.csv/?auth_key={auth_key}'

# Se crea el dataframe indicando que los decimales estan expresados con ',' y las unidades de mil con '.'.
# Se crea una columna 'id' auxiliar que servira para el merge de los dataframes ya que estos estan relacionados.
accseso_por_100_hogares = pd.read_csv(accseso_por_100_hogares, decimal=',', thousands='.')
accseso_por_100_hogares['id'] = accseso_por_100_hogares['Año'].astype('str') + accseso_por_100_hogares['Trimestre'].astype('str') + accseso_por_100_hogares['Provincia']

# Se crea una lista para el remplazo del nombre de columnas para evitar redundancias.
# Se dropean columnas innecesarias y repetidas en los otros dataframes.
columns = ['Año', 'Trimestre', 'Provincia', '-0.512 Mbps', '0.512 - 1 Mbps', '1 - 6 Mbps', '6 - 10 Mbps', '10 - 20 Mbps', '20 - 30 Mbps', '+30 Mbps', 'OTROS', 'Total']
velocidad_bajada_por_rangos = pd.read_csv(velocidad_bajada_por_rangos, decimal=',', thousands='.', header=0, names=columns)
velocidad_bajada_por_rangos['id'] = velocidad_bajada_por_rangos['Año'].astype('str') + velocidad_bajada_por_rangos['Trimestre'].astype('str') + velocidad_bajada_por_rangos['Provincia']
velocidad_bajada_por_rangos.drop(['Año', 'Trimestre', 'Provincia', 'OTROS', 'Total'], axis=1, inplace=True)

velocidad_media_de_bajada = pd.read_csv(velocidad_media_de_bajada)
velocidad_media_de_bajada['id'] = velocidad_media_de_bajada['Año'].astype('str') + velocidad_media_de_bajada['Trimestre'].astype('str') + velocidad_media_de_bajada['Provincia']
velocidad_media_de_bajada.drop(['Año', 'Trimestre', 'Provincia'], axis=1, inplace=True)

# Se eliminan errores en la data.
acceso_por_tecnologias = pd.read_csv(acceso_por_tecnologias, skipfooter=1, engine='python', decimal=',', thousands='.')
acceso_por_tecnologias.replace({r' \*': ''}, regex=True, inplace=True)
acceso_por_tecnologias['id'] = acceso_por_tecnologias['Año'] + acceso_por_tecnologias['Trimestre'] + acceso_por_tecnologias['Provincia']
acceso_por_tecnologias.drop(['Año', 'Trimestre', 'Provincia', 'Otros', 'Total'], axis=1, inplace=True)

# Se combinan los dataframe usando el id auxiliar.
# Se remplazan los valores de Trimestre por el numero de mes con el que inicia dicho trimestre.
# Se crea una columna date para optimizar los filtros en la herramienta de visualización.
acceso_a_internet = accseso_por_100_hogares.merge(velocidad_bajada_por_rangos, on='id')
acceso_a_internet = acceso_a_internet.merge(velocidad_media_de_bajada, on='id')
acceso_a_internet = acceso_a_internet.merge(acceso_por_tecnologias, on='id')
acceso_a_internet['Trimestre'].replace({4: '10', 3: '07', 2: '04', 1: '01'}, inplace=True)
acceso_a_internet['Date'] = (acceso_a_internet['Año'].astype('str') + '-' + acceso_a_internet['Trimestre'] + '-01').astype('datetime64')
acceso_a_internet.drop(['Año', 'Trimestre', 'id'], axis=1, inplace=True)
