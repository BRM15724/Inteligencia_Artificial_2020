import random
import copy

def crea_puzzle(num):
    # CREAMOS UNA LISTA CON LISTAS QUE CONTIENEN
    puzzle = [[1, 2, 4], [5, 0, 3], [6, 8, 7]]
    # REVOLVEMOS LAS LISTAS EN LA LISTA
    random.shuffle(puzzle)
    # REVOLVEMOS LAS LISTAS EN LA LISTA
    random.shuffle(puzzle[random.randint(0, 2)])
    # DEVOLVEMOS EL PUZZLE CREADO
    return puzzle


def movimientos(puzzle, predecesor):
    hijos = []

    # OBTENER POSICION DEL ESPACIO VACIO
    if 0 in puzzle[0]:      # ESTA EN LA PRIMERA LISTA
        i = 0
        j = puzzle[0].index(0)

    elif 0 in puzzle[1]:    # ESTA EN LA SEGUNDA LISTA
        i = 1
        j = puzzle[1].index(0)

    else:                   # ESTA EN LA TERCER LISTA
        i = 2
        j = puzzle[2].index(0)
    
    # PODEMOS IMPRIMIR EL NODO PADRE
    """
    print("PADRE")
    print("_________")
    print("%i %i %i" % (puzzle[0][0], puzzle[0][1], puzzle[0][2]))
    print("%i %i %i" % (puzzle[1][0], puzzle[1][1], puzzle[1][2]))
    print("%i %i %i" % (puzzle[2][0], puzzle[2][1], puzzle[2][2]))
    print("_________")
    """
    # CREAMOS COPIAS DE LAS LISTAS PARA GENERAR SUS HIJOS, A LOS MAS PUEDE TENER 4 HIJOS
    hijo1 = copy.deepcopy(puzzle)
    hijo2 = copy.deepcopy(puzzle)
    hijo3 = copy.deepcopy(puzzle)
    hijo4 = copy.deepcopy(puzzle)

    if j + 1 < len(hijo1[0]):
        y = hijo1[i][j]
        hijo1[i][j] = hijo1[i][j + 1]
        hijo1[i][j + 1] = y
    
    if j - 1 >= 0:
        # HIJO 2
        y = hijo2[i][j]
        hijo2[i][j] = hijo2[i][j - 1]
        hijo2[i][j - 1] = y
    
    if i + 1 < len(hijo3):
        # HIJO 3
        y = hijo3[i][j]
        hijo3[i][j] = hijo3[i + 1][j]
        hijo3[i + 1][j] = y
    
    if i - 1 >= 0:
        # HIJO 4
        y = hijo4[i][j]
        hijo4[i][j] = hijo4[i - 1][j]
        hijo4[i - 1][j] = y

    if hijo1 != puzzle:
        if hijo1 != predecesor:
            hijos.append(hijo1)
    if hijo2 != puzzle:
        if hijo2 != predecesor:
            hijos.append(hijo2)
    if hijo3 != puzzle:
        if hijo3 != predecesor:
            hijos.append(hijo3)
    if hijo4 != puzzle:
        if hijo4 != predecesor:
            hijos.append(hijo4)
    
    return hijos

def BFS(puzzle , solucion):
    nivel = 0
    arbol = {nivel : puzzle}
    hijos = movimientos(puzzle , "null")
    nivel = nivel + 1
    arbol[nivel] = hijos
    cont = 0
    while nivel < 500:
        nivel = nivel + 1
        for i in hijos:
            hijos2 = movimientos(i , "null")
            if solucion in hijos:
                #print(hijos)
                return hijos,True
            if nivel not in arbol:
                arbol[nivel] = hijos2
            else:
                arbol[nivel].append(hijos2)
        hijos[:] = []
        for j in hijos2:
            hijos.append(j)
        hijos2[:] = []
        cont = cont + 1
    #print("ARBOL: ", arbol)
    return arbol,False

cant = 0
solucion = [[1,2,3],[4,5,6],[7,8,0]]

print("Solucion: ", solucion)

for j in range(0,10):
    for i in range(0,10):
        puzzle = crea_puzzle(8)
        res,flag = BFS(puzzle,solucion)
        if flag:
            cant = cant + 1
        #print(".")
        print("Puzzle: ", puzzle)
    print(j, " Cantidad: ",cant)
    #print("Res: ",res)
    print("---------------------------------")
promedio = cant / 10
print("Promedio: ", promedio)