# RSEF 

Este script ejecuta RSEF con el campo "url" de cada una de las entradas del bib. 

Hay que tener en cuenta que para que funcione correctamente esta url deberia ser directa a un pdf.


## Uso


El script RESEF.py necesita dos argumentos de entrada:

 1 Ruta al fichero.bib
 
 2 Carpeta donde se va a guardar la salida de RSEF (en este caso si no existe se crea)
 
	python RSEF.py <archivo.bib> <carpeta_salida>
	
En los ejemplos vamos a ejecutar los siguientes comandos:

- Si lo ejecutamos desde la carpeta Codigo:
	
	python RSEF.py ../Pruebas/BibTex/conjuntoBIB.bib ../Pruebas/SalidaRSEFBasica
		
	python RSEF.py ../Pruebas/BibTex/garijo.bib ../Pruebas/SalidaRSEFCompleta