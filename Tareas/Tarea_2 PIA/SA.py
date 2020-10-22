import random
import math
from random import randint, uniform,random, sample

def simulated_annealing(Lista):
    # VALORES PRECONFIGURADOS DEL ALGORITMO
    initial_temp = 10
    final_temp = 1
    alpha = 1
    
    # TEMPERATURA ACTUAL IGUAL A 10
    current_temp = initial_temp

    # ESTADO ACTUAL IGUAL AL ESTADO INICIAL
    current_state = Lista.pop(len(Lista)-1)
    # SOLUCION ES IGUAL AL ESTADO INICIAL
    solution = current_state
    cost_current=0 # LE DOY UN COSTO ALTO INICIALMENTE
    soluciones=[solution]
    while current_temp > final_temp:   # MINETRAS LA TEMPERATURA ACTUAL SEA MAYOR A LA TEMPERATURA FINAL...

        # VECINO Y COSTO DE ESTE
        neighbor = Lista.pop(len(Lista)-1)
        cost_neighbor=abs(solution-neighbor)
        
        # DIFERENCIA DE COSTO SOLUCION ACTUAL MENOS COSTO DEL VECINO
        cost_diff = cost_current - cost_neighbor

        print("Solucion actual: ",solution," Costo solucion: ",cost_current," Vecino actual: ",neighbor," Costo vecino: ",cost_neighbor," Diferencia: ",cost_diff)

        # SI LA DIFERENCIA DE LOS COSTOS ES MAYOR A CERO
        if cost_diff > 0:

            solution = neighbor
            cost_current =cost_neighbor 
        # SI LA NUEVA SOLUCION NO ES MEJOR LA ACEPTAMOS PERO CON LAPROBABILIDAD DE e^(-cost/temp)
        else:
            if uniform(0, 1) < math.exp(cost_diff / current_temp):
                solution = neighbor
                cost_current =cost_neighbor
                print ("Probabilidad : ",math.exp(cost_diff / current_temp))
        # DECREMENTO LA TEMPERATURA -1
        current_temp -= alpha
        soluciones.append(solution)

    print("Solucion actual: ",solution," Costo solucion: ",cost_current," Vecino actual: ",neighbor," Costo vecino: ",cost_neighbor," Diferencia: ",cost_diff)
    return soluciones

Lista_original=sample(range(1,11),10)
soluciones = []

for i in [0,1,2,3,4,5,6,7,8,9]:
    print("\n\nITERACION ",i+1);
    Lista=Lista_original[:]
    print(Lista)
    soluciones = simulated_annealing(Lista)
    print (soluciones)