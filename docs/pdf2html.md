# Pdf2htmlEX

Este script ejecuta pdf2htmlEX con el pdf que se encuentra en subcarpeta2 que corresponde a la carpeta PDFs que crea RSEF cuando se ejecuta.

Convertimos el pdf en html y lo copiamos en la carpeta de html, ahi van a estar todos los html correspondientes para poder verlos despues correctamente en la pagina web con una ruta relativa

## Uso

El script pdf2html.py necesita dos argumentos de entrada:

 1 Ruta de la carpeta raiz 
 
 2 Ruta de la carpeta de salida para los html
 
	python pdf2html.py <carpeta_raiz> <carpeta_salida>
	
En los ejemplos vamos a ejecutar los siguientes comandos:

- Si lo ejecutamos desde la carpeta Codigo:
	
	python pdf2html.py ../Pruebas/SalidaRSEFBasica ../Pruebas/PaginaWebBasica/html
		
	python pdf2html.py ../Pruebas/SalidaRSEFCompleta ../Pruebas/PaginaWebCompleta/html
	
	