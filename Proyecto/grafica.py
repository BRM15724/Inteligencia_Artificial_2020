# Libreria para mostrar graficos
import matplotlib.pyplot as plt
# Libreria para diseñar la grafica (pip install numpy==1.19.3)
import numpy as np
# Libreria para generar num random
import random

# Defino el largo del eje x y las separaciones que debe haber entre 1 y 20, en este caso 20 separaciones
x = np.linspace(1,20,20)

for j in range (1,4):
    opcion = input("Continuar: ")

    f = open('datos.txt', 'a')
    f.write('\nDATOS DE ALGORITMO '+str(j)+'\n')
    # Defino una lista para luego rellenarla de valores , por el moemnto son numeros random pero luego sera tiempo en segundos
    y = []
    i = 0
    suma_tiempo = 0

    # Este ciclo simula las corridas por cada tipo de mapa
    while i < 20:
        tiempo = round(random.uniform(80, 100), 2) # genero tiempo ficticio
        f.write('MAPA '+str(i+1)+': TIEMPO '+str(tiempo)+'\n')
        suma_tiempo = suma_tiempo + tiempo
        y.append(tiempo) # Guardo el tiempo que genere en la lista y
        i=i+1
    f.write('\n\n')
    tiempo_promedio = suma_tiempo / 20  # Saco el tiempo promedio, es para generar una linea horizontal en el mapa, representara el tiempo promedio

    # Genero la linea azul de la grafica, con los valores de x ya definidos y los tiempos de y, 'b' indica una linea azul
    plt.plot(x,y,'b') 

    # Titulo de la grafica
    plt.title('Grafica de Algoritmo ' + str(j))
    # Nombre del eje x
    plt.xlabel('Mapas')
    # Nombre del eje y
    plt.ylabel('Tiempo (segundos)')
    # Indico que quiero que se vea la cuadricula en el mapa
    plt.grid(True)
    # Indico la cantidad de separaciones que quiero entre 0 y 20
    plt.xticks(np.linspace(0,20,21))
    # Coloco la linea de el tiempo promedio
    plt.axhline(tiempo_promedio,color='k',lw=1)
    # Muestro la grafica
    plt.show()

    f.close()

