#para este practica he trabajado con la distribucion anaconda 3.7 https://www.anaconda.com/distribution/
#y las pruebas del codigo python las he realizado en Spyder, que se instala conjuntamente con anaconda.
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.meteored.com.ec/")
soup = BeautifulSoup(page.content, "html.parser")

elementos = soup.find_all(class_="li-top-prediccion")#esta clase siempre será la que se repita
#print(elementos[0])
#print(elementos[1])
#print(elementos[2])

#probando las clases
#print(elementos[0].find(class_="anchors").get_text())
#print(elementos[0].find(class_="cMax changeUnitT").get_text()) 
#print(elementos[0].find(class_="cMin changeUnitT").get_text()) 
ciudad =[elemento.find(class_="anchors").get_text() for elemento in elementos]
t_maxima =[elemento.find(class_="cMax changeUnitT").get_text() for elemento in elementos]
t_minima =[elemento.find(class_="cMin changeUnitT").get_text() for elemento in elementos]
 

#print(ciudad)
#print(t_maxima)
#print(t_minima)

lider = pd.DataFrame(
        {
         "Ciudad":ciudad,
         "Temperatura maxima":t_maxima,
         "Temperatura minima":t_minima
         
        })
print(lider)
#el archivo csv se guarda por defecto en la carpeta donde se almacena su fichero.py
lider.to_csv("datos_metereologicos.csv")   