# Main

Este script ejecuta todos los anteriores.

## Uso

El script main.py necesita cuatro argumentos de entrada:

 1 Ruta del bib 
 
 2 Ruta de la carpeta raiz 
 
 3 Ruta de la carpeta de salida para los html
 
 4 Ruta de la carpeta de salida donde se va a guardar el fichero json completo
 
	python main.py <archivo.bib> <carpetaSalidaRSEF> <carpetaSalidaHTMLs> <carpetaSalidaConjuntoJSON+CodigoPaginaWeb>

En los ejemplos vamos a ejecutar los siguientes comandos:

- Si lo ejecutamos desde la carpeta Codigo:
	
	python main.py ../Pruebas/BibTex/conjuntoBIB.bib ../Pruebas/SalidaRSEFBasica ../Pruebas/PaginaWebBasica/html ../Pruebas/PaginaWebBasica

**Página web:** https://raaquel09.github.io/Articulos-HTML-Enlazado/Pruebas/PaginaWebBasica/paginaWeb.html
		
	python main.py ../Pruebas/BibTex/garijo.bib ../Pruebas/SalidaRSEFCompleta ../Pruebas/PaginaWebCompleta/html ../Pruebas/PaginaWebCompleta

 **Página web:** https://raaquel09.github.io/Articulos-HTML-Enlazado/Pruebas/PaginaWebCompleta/paginaWeb.html