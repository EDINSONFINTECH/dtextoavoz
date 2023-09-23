# Texto a Voz ***
# La idea de este proyecto es convertir un artículo existente en un archivo de audio 
# reproducible en formato mp3. Para ello puedes hacer uso de bibliotecas existenes 
# como nltk (kit de herramientas de lenguaje natural), newspaper3k y gtts 
# (puedes seguir las instrucciones de instalación de pip).
# Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para
# luego manejar la conversión de texto a voz.

""" El programa que se necesita hacer consiste en convertir un artículo existente en un 
archivo de audio reproducible en formato mp3. Para ello, 
vamos a hacer uso de las siguientes bibliotecas """


"""- newspaper3k: Es una biblioteca que nos  permite descargar y 
analizar artículos de noticias de diferentes fuentes.(https://www.nltk.org/) """

"""- gtts: Es una biblioteca que nos permite convertir texto a voz usando 
la API de Google Translate. Puedemos usarla para generar un archivo de audio en mp3 
con la voz que se  elija, y también para reproducirlo o guardarlo."""

# Les dejare mencionados los pasos que creo que se pueden realizar para una posible solucion
""" - Pedir al usuario que introduzca la URL del artículo que quiere convertir a voz.
- Usar newspaper3k para crear un objeto "Article" con la URL y descargar el contenido del 
artículo.
- Usar nltk para procesar el texto del artículo y obtener la información relevante,
como el título, el autor, la fecha, el resumen, las palabras clave, etc. 
También puedes usar nltk para dividir el texto en oraciones y aplicar algunas 
correcciones o normalizaciones si es necesario.
- Usar gtts para crear un objeto gTTS con el texto del artículo y el idioma que quieras. 
También puedes elegir otras opciones como la velocidad o la calidad del audio.
- Usar el método save del objeto gTTS para guardar el archivo de audio en mp3 en
la carpeta que quieras.
- Usar el módulo os para reproducir el archivo de audio con el reproductor predeterminado
de tu sistema operativo.
"""

# El código podría ser algo así:

# Importar las bibliotecas necesarias
from newspaper import Article
import nltk
from gtts import gTTS
import os

# Pedir al usuario que introduzca la URL del artículo
url = input("Introduce la URL del artículo que quieres convertir a voz: ")

# Crear un objeto Article con la URL y descargar el contenido
article = Article(url)
article.download()

# Procesar el texto del artículo con nltk
article.parse()
nltk.download('punkt')
article.nlp()

# Obtener la información relevante del artículo
title = article.title
author = article.authors
date = article.publish_date
summary = article.summary
keywords = article.keywords

# Mostrar la información por pantalla
print(f"Título: {title}")
print(f"Autor: {author}")
print(f"Fecha: {date}")
print(f"Resumen: {summary}")
print(f"Palabras clave: {keywords}")

# Dividir el texto en oraciones
sentences = nltk.sent_tokenize(article.text)

# Aplicar algunas correcciones o normalizaciones al texto si es necesario
# Por ejemplo, puedes reemplazar algunos símbolos o abreviaturas por su forma completa

# Unir las oraciones en un solo texto
text = " ".join(sentences)

# Crear un objeto gTTS con el texto y el idioma que quieras
# También puedes elegir otras opciones como la velocidad o la calidad del audio
tts = gTTS(text=text, lang='es', slow=False)

# Guardar el archivo de audio en mp3 en la carpeta que quieras
tts.save("article.mp3")

# Reproducir el archivo de audio con el reproductor predeterminado
os.system("start article.mp3")

""" Espero les funcione este ejemplo para los compañeros de CONQUERX, ya lo comprobe y funciona perfecto."""


