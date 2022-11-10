# Tarea-1-Algoritmos-Metahuristicos
## Problema Berlin 52 con colonia de hormigas
### El programa presenta una solución para el problema de Berlin 52, que consiste en recorrer 52 puntos de la ciudad de berlin recorriendo la menor distancia posible, para esto se utilizara el algoritmo de colonia de hormigas. Para el correcto funcionamiento de este programa se deben considerar los siguientes puntos:

## Programas utilizados 

* [GitHub Desktop](https://desktop.github.com/) - Herramienta para tener los repositorios en la nube y mantener las versiones.
* [Visual Studio Code](https://visualstudio.microsoft.com/es/) - IDE y editor para la creación del Algoritmo.

## Instalación
* La versión utilizada para python será [3.10.7](https://www.python.org/downloads/).
* Se necesitara instalar la libreria [numpy](https://numpy.org/) en la IDE que se este trabajando con el siguiente código:
 ```
 pip install numpy
 ```
 * Se necesitara instalar la libreria [pandas](https://pandas.pydata.org/) en la IDE que se este trabajando con el siguiente código:
 ```
 pip install pandas
 ```
 * Para bajar el programa haga click en el siguiente [Link](https://github.com/GustavoSepul/Tarea-2-Algoritmos-Metaheuristicos/archive/refs/heads/main.zip)

## Ejecución del programa

- Para ejecutar el codigo se debe ejecutar el siguiente comando: 
```
python ./n-reinas.py Seed Tamaño_colonia Número_Iteraciones Tasa_evaporación Factor_euristica Probabilidad_exploración Archivo_entrada
```


- Donde:
    - ***Seed***, el cuál sera un número real randomico mayor a 0.
    - ***Tamaño_colonia***, el cuál sera un número entero mayor que 1.
    - ***Número_Iteraciones***, el cuál sera un número entero a criterio del usuario.
    - ***Tasa_evaporación***, el cuál sera un número entero entre 0 y 100 (10%).
    - ***Factor_euristica***, el cuál sera un número real entre 2 y 5 (2,5).
    - ***Probabilidad_exploración***, el cuál sera un número real entre 0 y 100 (90%).
    - ***Archivo_entrada***, nombre del archivo con las coordenadas de los puntos (berlin52.txt).




## Ejemplo
```
python.exe .\Colonia_hormigas.py 1 100 500 10 2.5 90 berlin52.txt
```
## Resultados
```
Generacion:  15
Mejor solucion:
[41  6  1 29 22 19 49 28 15 45 43 33 34 35 38 39 36 37 47 23  4 14  5  3
 24 11 27 26 25 46 12 13 51 10 50 32 42  9  8  7 40 18 44 31 48  0 21 30
 17  2 16 20]
Mejor costo:  7544.3659
Tiempo de busqueda:  5.884 segundos
```
### Autores
* Diego Araneda Hidalgo - daranedah@ing.ucsc.cl
* Gustavo Sepulveda Ocampo - gsepulvedao@ing.ucsc.cl
* Javier Victoriano Rivas - jvictoriano@ing.ucsc.cl
