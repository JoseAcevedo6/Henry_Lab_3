![Conexiones](https://resizer.iproimg.com/unsafe/880x/filters:format(webp)/https://assets.iprofesional.com/assets/jpg/2021/09/522982.jpg)


# <h1 align="center">:computer: **`Acceso a Internet`** :computer:</h1>

## **Contexto**
La industria de las telecomunicaciones ha jugado un papel vital en nuestra sociedad, facilitando la información a escala internacional y permitiendo la comunicación continua incluso en medio de una pandemia mundial. La transferencia de datos y comunicación se realiza en su mayoría a través de internet, líneas telefónicas fijas, telefonía móvil, casi en cualquier lugar del mundo. 

En comparación con la media mundial, Argentina está a la vanguardia del desarrollo de las telecomunicaciones, teniendo para el 2020 un total de 62,12 millones conexiones. [Fuente aquí](https://www.datosmundial.com/america/argentina/telecomunicacion.php)
<br></br>

## **Rol a desarrollar**

En este contexto, una empresa prestadora de servicios de telecomunicaciones encarga la realización de un **análisis** completo que permita reconocer el comportamiento de este sector a nivel nacional. Con el fin de monitorear la eficacia de los objetivos de la empresa, se solicita **visualizar 4 KPI's** en un dashboard producto de su análisis.
<br></br>

## **Análisis exploratorio de los datos**
### Datos del ENACOM
- [Acceso a internet por provincia (accesos por cada 100 hogares).](https://datosabiertos.enacom.gob.ar/dataviews/240980/penetracion-del-internet-fijo-por-provincia-accesos-por-cada-100-hogares/)
- [Acceso a internet por rangos de velocidad de bajada y provincia.](https://datosabiertos.enacom.gob.ar/dataviews/240904/acceso-a-internet-fijo-por-rangos-de-velocidad-de-bajada-y-provincia/)
- [Acceso a internet por tecnología y provincia.](https://datosabiertos.enacom.gob.ar/dataviews/240898/acceso-a-internet-fijo-por-tecnologia-y-provincia/)
- [Velocidad media de bajada de Internet por provincia.](https://datosabiertos.enacom.gob.ar/dataviews/245546/velocidad-media-de-bajada-de-internet-fijo-por-provincia/)

Se dispone de 4 datasets relacionados por las dimensiones 'Año', 'Trimestre' y 'Provincia', con 816 registros, sin valores nulos ni duplicados. Se crea una dimensión provisoria 'id' para unir los datasets en uno solo y una dimensión 'date' para graficar la data por períodos de tiempo.

### Descripción de las dimensiones (15) del dataset unificado:
- Provincia: Ubicación donde se realiza el acceso a internet.
- Date: Período trimestral por año expresado en formato de fecha.
- Accesos: Cantidad de accesos a internet por cada 100 hogares.
- -0.512 Mbps: Cantidad de accesos a internet con velocidades inferiores a 512 kbps.
- 0.512 - 1 Mbps: Cantidad de accesos a internet con velocidades entre ambos valores.
- 1 - 6 Mbps: Cantidad de accesos a internet con velocidades entre ambos valores.
- 6 - 10 Mbps: Cantidad de accesos a internet con velocidades entre ambos valores.
- 10 - 20 Mbps: Cantidad de accesos a internet con velocidades entre ambos valores.
- 20 - 30 Mbps: Cantidad de accesos a internet con velocidades entre ambos valores.
- +30 Mbps: Cantidad de accesos a internet con velocidades superiores a 30 Mbps.
- Mbps (Media de bajada): Promedio de velocidad de bajada expresado en Mbps.
- ADSL: Conexión a internet mediante cables de pares simétricos.
- Cablemoden: Conexión a internet mediante cable coaxiales.
- Fibra óptica: Conexión a internet mediante fibra óptica.
- Wireless: Conexión a internet mediante ondas de radio.

### A partir de la data se procede a crear los siguientes KPI's.

*Variación porcentual de acceso a internet por cada 100 hogares*

<img src="src\variacion_porcentual_100_hogares.jpg">

##### Se puede observar que en general, la variación porcentual por cada 100 hogares es positiva a nivel nacional y a través de los años, mismo comportamiento observado a nivel provincial (para visualizar la variación por provincia, revisar el archivo .pbix adjuntado en el repositorio).
<br>

*Acceso a internet por rangos de velocidad de bajada*
<p align="center">
<img src="src\velocidad_bajada_por_rangos.jpg" alt="drawing" width="350">

##### Este gráfico muestra como las velocidades mayores de 30 Mbps se van estandarizando en los últimos 3 años a nivel nacional. Por otra parte, se vuelve a evidenciar el incremento sostenido de los hogares en el acceso a internet.  
<br>

*Velocidad media de bajada de internet*

<img src="src\velocidad_media_bajada.jpg">

##### Cerca de multiplicar por 4 la media de hace 4 años y correlacionándose con la gráfica anterior, el 2022 destaca con una media de velocidad de bajada por encima de los 30 Mbps.
<br>

*Acceso a internet por tecnología*

<img src="src\acceso_por_tecnologia.jpg">

##### Visualmente se puede establecer que la tecnología ADSL está disminuyendo, la tecnología Cable modem y Wireless se mantienen a la vez que la tecnología Fibra Óptica duplica sus valores en el 2022 en relación al 2020.  
<br>

### Conclusiones del EDA
El acceso a internet se ha vuelto una necesidad fundamental en la vida cotidiana de las personas, son numerosas las actividades que se benefician al realizar esta práctica. Es por esto que se puede observar que el crecimiento en la cantidad de accesos es sostenido en el tiempo, que el cambio a ciertas tecnologías puede incrementar las velocidades de acceso a la información.

Es relevante destacar una variación negativa en la cantidad de accesos a finales del 2019 acompañada de una variación positiva a inicios del 2020 que se observa en varias provincias. Esto pudiera corresponder con el cambio de gobierno y la llegada de la pandemia respectivamente. Y es que este último acontecimiento, a pesar de todas sus consecuencias negativas, cambio la forma de cómo se interactúa con el mundo; cambiando aulas de clase y oficinas de trabajo por espacios en el hogar, restaurantes y citas médicas por aplicaciones. 

A pesar de los valores positivos en la cantidad de accesos a nivel nacional, se detecta que varias provincias tienen una velocidad de conexión muy por debajo de la media, ausencia de tecnologías como la fibra óptica y menos de 50 accesos por cada 100 hogares. 

Por tal motivo, sumado la tendencia creciente en los accesos a internet y las nuevas formas de realizar las actividades cotidianas, se sugiere:
- Expandir y mejorar la infraestructura a fin de llegar a nuevas ubicaciones, incrementar las velocidades de conexión y aumentar el ancho de banda.
- Implementar estrategias de marketing en base a las preferencias (Fibra óptica y velocidades de conexión por encima de la media)
- Publicidad para atraer a nuevos clientes y hacer presencia en las nuevas ubicaciones de operación.

## Tecnologías y librerías utilizadas
- Python :snake:
- Pandas :panda_face:
- Power BI :bar_chart: