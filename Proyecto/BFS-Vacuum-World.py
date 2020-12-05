import os
import time
import copy

def clear():
    os.system('cls')
def pause():
    time.sleep(.2)

    # world.append(['A', '_', '_', '_', '_', '_', '_', '_'])
    # world.append(['_', '_', '_', '_', '_', '_', '_', '_'])
    # world.append(['_', '_', '_', '_', '_', '_', '_', '_'])
    # world.append(['_', '_', '_', 'B', '_', '_', '_', '_'])
    # world.append(['_', '_', '_', '_', '_', '_', '_', '_'])
    # world.append(['_', '_', '_', '_', '_', '_', '_', '_'])
    # world.append(['_', '_', '_', '_', '_', '_', '_', '_'])
    # world.append(['_', '_', '_', '_', '_', '_', '_', 'B'])


# #Función para explorar los vecinos de una loseta de la matriz, acorde a los ínidices
# def explore_neighbours(r, c, nodes_in_next_layer):
#     #Itero para cada dirección
#     for i in range(4):
#         #Posible indice de la fila
#         rr = r + direction_row[i]
#         #Posible indice de la columna
#         cc = c + direction_column[i]

#         #Si los indices están fuera de los línites del mapa, regreso al for
#         if rr < 0 or cc < 0:
#             continue
#         if rr >= rows or cc >= columns:
#             continue
        
#         #Si la loseta ha sido visitado, regreso al for
#         if visited[rr][cc]:
#             continue
#         #Si la loseta es una pared, regreso al for 
#         if world[rr][cc] == '#':
#             continue

#         #Agrego los índices a sus colas
#         row_queue.append(rr)
#         column_queue.append(cc)
#         #Asigno true a la loseta que ya ha sido visitada
#         visited[rr][cc] =True
        
#         #Sumo uno a la cantidad de nodos en la expansion
#         nodes_in_next_layer += 1 

def solve_bfs(world):
    #Posición de la aspiradora
    vacuum_row, vacuum_column = vacuum_index(world)

    #Numero de filas y columnas
    rows = len(world)
    columns = len(world[0])

    #Cola de las filas y columnas
    row_queue = []
    column_queue = []

    #Matriz de nosos visitados, inicialmeten todos en false
    visited = [[False for i in range(rows)] for j in range(columns)]

    #Vectores de direccion, norte, sur, este y oeste.
    direction_row = [-1, 1, 0, 0]
    direction_column = [0, 0, 1, -1]

    #Variable booleana que indica si se llegó al estado meta, una basura 'B'
    reached_end = False

    #Variables que siguen el número de pasos para llegar a la meta, primera basura. Sirven para reconstruir el camino
    #Cantidad de moviemientod requeridos
    move_count = 0 
    #Cantidad de elementos que hay que sacar de la cola antes de hacer un paso
    nodes_left_in_layer = 1
    #Cantidad de nodos que agregamos en la expansion del BFS 
    nodes_in_next_layer = 0 
    

    #Agrego la posicion de la aspiradora a la cola
    row_queue.append(vacuum_row)
    column_queue.append(vacuum_column)
    
    #Matriz para guardar el camino
    prev = [[[] for i in range(rows)] for j in range(columns)]

    #Asigno la loseta como visidado
    visited[vacuum_row][vacuum_column] = True
    while len(row_queue) > 0: #Mientras haya elementos en la cola
        #Saco los índices de las colas de fila y columna
        r = row_queue.pop(0)
        c = column_queue.pop(0)
        #Si llego a una basura, me detengo
        if world[r][c] == 'B':
            reached_end = True
            break
        
        #Verifico los vecinos y los pongo en la cola
        for i in range(4):
            #Posible indice de la fila
            rr = r + direction_row[i]
            #Posible indice de la columna
            cc = c + direction_column[i]
            #Si los indices están fuera de los línites del mapa, regreso al for
            if rr < 0 or cc < 0:
                continue
            if rr >= rows or cc >= columns:
                continue
            
            #Si la loseta ha sido visitado, regreso al for
            if visited[rr][cc]:
                continue
            #Si la loseta es una pared, regreso al for 
            if world[rr][cc] == '#':
                continue
            
            #Agrego los índices a sus colas
            row_queue.append(rr)
            column_queue.append(cc)

            print_expantion(visited, world, rr,cc)
            #Asigno true a la loseta que ya ha sido visitada
            visited[rr][cc] =True
            #Asigno los indices de la lesetas previas al nodo actual
            prev[rr][cc] = [r, c]
            #Sumo uno a la cantidad de nodos en la expansion
            nodes_in_next_layer += 1
        

        #Este bloque mantiene el numero de pasos que nos toma llegar a la basura
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
    if reached_end:
        return move_count, prev, r, c
    return -1, -1, -1, -1

 

def print_world(world):
    for i in range(len(world)):
        print()
        for j in range(len(world)):
            print(world[i][j], end='')    
    print()

def print_path(world, path):
    clear()
    print_world(world)
    time.sleep(.5)
    clear()
    for i in range(len(path)):
        world[path[i][0]][path[i][1]] = 'A'
        print_world(world)
        time.sleep(.5)
        clear()

def print_expantion(visited, world, r, c):
    clear()
    for i in range(len(world)):
        print()
        for j in range(len(world[0])):
            if(visited[i][j]):
                print('A', end= '')
            else:
                print(world[i][j], end='')
    print()
    pause()

def refresh_world(world, r, c):
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == 'A':
                world[i][j] = '_'
    world[r][c] = 'A'

def vacuum_index(world):
    i = 0
    for row in world:
        if('A' in row):
            vacuum_column = row.index('A')
            vacuum_row = i
            break
        i +=1
    return vacuum_row, vacuum_column


def solve(world):
    count_steps = 0
    count_trash = 0
    paths = []
    #Mientras encuentre basura
    while(count_steps != -1):
        #Resuelvo para una basura
        count_steps, prev, t_r, t_c = solve_bfs(world)
        
        if count_steps != -1:
            #Reconstruyo el camino
            path = []
            for i in range(count_steps):
                if(i == 0):
                    path.append([t_r,t_c])
                else:
                    path.append(prev[path[i-1][0]][path[i-1][1]])
            path.reverse()
            print_path(world, path)
            paths.append(path)
            refresh_world(world, t_r, t_c)
            #print_world(world)
            
            
            #Sumo uno al contador de basura
            count_trash += 1
    clear()
    print('Basura encontrada = ', end='')
    print(count_trash)
    return paths

def copy_world(world, world_copy):
    for i in range(len(world)):
        for j in range(len(world[i])):
            world_copy[i][j] = world[i][j]

def main():
    #Mundo de la aspiradora
    world = []
    world.append(['_', '_', '_', '_', '_', '_', '_', '_', 'B', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'])
    world.append(['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'])
    world.append(['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'])
    world.append(['_', '#', '#', '#', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'B', '_', '#', '#', '#', '_'])
    world.append(['_', '_', 'B', '#', 'B', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '#', 'B', '_', '_'])
    world.append(['_', '_', '_', '#', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '#', '_', '_', '_'])
    world.append(['_', '_', '_', '#', '_', '_', '_', '#', '#', '#', '#', '_', '#', '_', '_', '_', '#', '_', '_', '_'])
    world.append(['_', '_', '_', '#', '_', '_', '_', '#', 'B', '_', '_', '_', '#', '_', '_', '_', '#', '_', '_', '_'])
    world.append(['_', '_', '_', '#', '_', '_', '_', '#', '_', '_', '_', '_', '#', '_', '_', '_', '#', '_', '_', '_'])
    world.append(['_', '_', '_', '#', '_', '_', 'A', '#', '_', '_', '_', '_', '#', '_', '_', '_', '#', '_', '_', '_'])
    world.append(['_', '_', '_', '#', '_', '_', '_', '#', '_', '_', '_', 'B', '#', '_', '_', '_', '#', '_', '_', '_'])
    world.append(['_', '_', '_', '#', '_', '_', '_', '#', '#', '#', '#', '#', '#', '_', '_', '_', '#', '_', '_', '_'])
    world.append(['_', '_', '_', '#', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '#', '_', '_', '_'])
    world.append(['_', '_', '_', '#', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '#', '_', '_', '_'])
    world.append(['_', '_', '_', '#', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'B', '_', '_', '#', '_', '_', '_'])
    world.append(['_', '_', '_', '#', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '#', 'B', '_', '_'])
    world.append(['_', '#', '#', '#', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '#', '#', '#', '_'])
    world.append(['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'])
    world.append(['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'])
    world.append(['B', '_', '_', '_', '_', '_', '_', '_', 'B', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'])

    world_copy = [[ ' ' for i in range(len(world))] for j in range(len(world[0]))]

    copy_world(world, world_copy)   
    paths = solve(world)
    

main()

# world_copy = world.copy()
# count_steps, prev, r, c = solve_bfs(world_copy)
# print(prev)