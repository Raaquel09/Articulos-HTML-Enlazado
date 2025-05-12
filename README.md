[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15390107.svg)](https://doi.org/10.5281/zenodo.15390107)

# Conversión de Artículos en HTML Enlazado


## Descripción

El objetivo de este proyecto es transformar la bibliografía de un investigador en una serie de páginas enlazadas para que sea mas sencillo de consultar y más accesible para aquellos que necesiten consultarlo.


## Requisitos

Para que este proyecto funcione hay que instalarse lo siguiente:

1. **Entorno Python**:

 Un entorno de python para ejecutar los scripts y comprobar que funciona.

2. **Las librerías correspondientes**:

 bibtexparser

3. **Instalar RSEF**:

 https://github.com/SoftwareUnderstanding/RSEF 

4. **Ejecutar pdf2htmlEX**:

 https://github.com/pdf2htmlEX/pdf2htmlEX


## Estructura:

	Codigo
	|	RESEF.py
	|	pdf2html.py
	|	unir.py
	|	main.py
	|	paginaWeb.html
	Pruebas
		BibTex
		|	nombrebib.bib 
		carpeta_raiz (SalidaRSEF)
		|	subcarpeta1 (carpetaBIB1)
		|	|	subcarpeta2 (PDFs)
		|	|		nombrepdf1.pdf
		|	subcarpeta1 (carpetaBIB2)
		|	|	subcarpeta2 (PDFs)
		|	|		nombrepdf2.pdf
		|	subcarpeta1 (carpetaBIB3)
		|		subcarpeta2 (PDFs)
		|			nombrepdf3.pdf
		PaginaWeb 
			conjuntoJSON.json
			paginaWeb.html
			html
				nombrehtml1.html
				nombrehtml2.html
				nombrehtml2.html


## Entrada y salida del proceso

**Entrada**: Fichero bib con la informacion de cada documento de investigacion

**Salida**: Fichero json con la informacion de cada documento de investigacion + la pagina web


## Código:

### 1 Tenemos el fichero bib (obligatorio)

Ejecutamos RSEF con el campo "url" de cada una de las entradas del bib.

Hay que tener en cuenta que para que funcione correctamente esta url deberia ser directa a un pdf.

El script RESEF.py necesita dos argumentos de entrada:

 1 Ruta al fichero.bib
 
 2 Carpeta donde se va a guardar la salida de RSEF (en este caso si no existe se crea)
 
	python RSEF.py <archivo.bib> <carpeta_salida>
	
En los ejemplos vamos a ejecutar los siguientes comandos:

- Si lo ejecutamos desde la carpeta Codigo:

	
	python RSEF.py ../Pruebas/BibTex/conjuntoBIB.bib ../Pruebas/SalidaRSEFBasica
		
	python RSEF.py ../Pruebas/BibTex/garijo.bib ../Pruebas/SalidaRSEFCompleta
	
### 2 Pasamos el pdf descargado por RSEF a un HTML

Segun la estructura que tenemos arriba el pdf se encuentra en subcarpeta2 que corresponde a la carpeta PDFs que crea RSEF cuando se ejecuta.
Convertimos el pdf en html y lo copiamos en la carpeta de html, ahi van a estar todos los html correspondientes para poder verlos despues correctamente en la pagina web con una ruta relativa

El script pdf2html.py necesita dos argumentos de entrada:

 1 Ruta de la carpeta raiz 
 
 2 Ruta de la carpeta de salida para los html
 
	python pdf2html.py <carpeta_raiz> <carpeta_salida>
	
En los ejemplos vamos a ejecutar los siguientes comandos:

- Si lo ejecutamos desde la carpeta Codigo:

	
	python pdf2html.py ../Pruebas/SalidaRSEFBasica ../Pruebas/PaginaWebBasica/html
		
	python pdf2html.py ../Pruebas/SalidaRSEFCompleta ../Pruebas/PaginaWebCompleta/html
	
### 3 Unimos la informacion siguiente en un mismo fichero.json

url_search_output.json correspondiente a cada documento
Entrada correspondiente del bib
Campo "file_html" con una futa relativa al html creado por pdf2html

El script unir.py necesita tres argumentos de entrada:

 1 Ruta el bib para coger la informacion de la entrada correspondiente
 
 2 Ruta de la carpeta raiz 
 
 3 Ruta de la carpeta de salida donde se va a guardar el fichero json completo
 

	python unir.py <ruta bib> <carpeta_raiz> <carpeta_salida>
	
En los ejemplos vamos a ejecutar los siguientes comandos:

- Si lo ejecutamos desde la carpeta Codigo:


	python unir.py ../Pruebas/BibTex/conjuntoBIB.bib ../Pruebas/SalidaRSEFBasica ../Pruebas/PaginaWebBasica
		
	python unir.py ../Pruebas/BibTex/garijo.bib ../Pruebas/SalidaRSEFCompleta ../Pruebas/PaginaWebCompleta
	
### 4 Tenemos un main que ejecuta todos los scripts anteriores

El script unir.py necesita cuatro argumentos de entrada:

 1 Ruta del bib 
 
 2 Ruta de la carpeta raiz 
 
 3 Ruta de la carpeta de salida para los html
 
 4 Ruta de la carpeta de salida donde se va a guardar el fichero json completo
 
	python main.py <archivo.bib> <carpetaSalidaRSEF> <carpetaSalidaHTMLs> <carpetaSalidaConjuntoJSON+CodigoPaginaWeb>

En los ejemplos vamos a ejecutar los siguientes comandos:

- Si lo ejecutamos desde la carpeta Codigo:

	
	python main.py ../Pruebas/BibTex/conjuntoBIB.bib ../Pruebas/SalidaRSEFBasica ../Pruebas/PaginaWebBasica/html ../Pruebas/PaginaWebBasica
		
	python main.py ../Pruebas/BibTex/garijo.bib ../Pruebas/SalidaRSEFCompleta ../Pruebas/PaginaWebCompleta/html ../Pruebas/PaginaWebCompleta