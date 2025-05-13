# Union de la información principal

Este script una la siguiente información:

- url_search_output.json correspondiente a cada documento

- Entrada correspondiente del bib

- Campo "file_html" con una futa relativa al html creado por pdf2html

## Uso

El script unir.py necesita tres argumentos de entrada:

 1 Ruta el bib para coger la informacion de la entrada correspondiente
 
 2 Ruta de la carpeta raiz 
 
 3 Ruta de la carpeta de salida donde se va a guardar el fichero json completo 

	python unir.py <ruta bib> <carpeta_raiz> <carpeta_salida>
	
En los ejemplos vamos a ejecutar los siguientes comandos:

- Si lo ejecutamos desde la carpeta Codigo:

	python unir.py ../Pruebas/BibTex/conjuntoBIB.bib ../Pruebas/SalidaRSEFBasica ../Pruebas/PaginaWebBasica
		
	python unir.py ../Pruebas/BibTex/garijo.bib ../Pruebas/SalidaRSEFCompleta ../Pruebas/PaginaWebCompleta