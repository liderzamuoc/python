# Web Scraping con python

En esta práctica, se ha podido extraer los datos climáticos de la pagina https://www.meteored.com.ec/ de las ciudadades más importantes del Ecuador.
los datos que se extraen son nombre de la ciudad, temperatura máxima y temperatura mínima.

Para ejecutar el script es necesario instalar la siguientes bibliotecas:

pip install pandas

pip install requests

pip install beautifulsoup4 (sino se instala esta libreria se puede probar asi pip install bs4)

En esta web vemos que podemos realizar web scraping, ya que nos da los permisos para hacerlo.
podemos verificar el archivo robots.txt en https://www.meteored.com.ec/robots.txt como podemos tambien acceder a su API
https://www.meteored.com.ec/api/#/login.

Tenemos la facilidad de generar un archivo csv con los datos climaticos de otros paises. 
Se ha trabajado con un dataset tipo DataFrame.
