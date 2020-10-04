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
        # HIJO 1
        y = hijo1[i][j]
        hijo1[i][j] = hijo1[i][j + 1]
        hijo1[i][j + 1] = y
        """
		print("HIJO 1")
		print("%i %i %i" % (hijo1[0][0], hijo1[0][1], hijo1[0][2]))
		print("%i %i %i" % (hijo1[1][0], hijo1[1][1], hijo1[1][2]))
		print("%i %i %i" % (hijo1[2][0], hijo1[2][1], hijo1[2][2]))
		print()
		#return hijo1
		"""
    
    if j - 1 >= 0:
        # HIJO 2
        y = hijo2[i][j]
        hijo2[i][j] = hijo2[i][j - 1]
        hijo2[i][j - 1] = y
        """
		print("HIJO 2")
		print("%i %i %i" % (hijo2[0][0], hijo2[0][1], hijo2[0][2]))
		print("%i %i %i" % (hijo2[1][0], hijo2[1][1], hijo2[1][2]))
		print("%i %i %i" % (hijo2[2][0], hijo2[2][1], hijo2[2][2]))
		print()
		#return hijo2
		"""
    
    if i + 1 < len(hijo3):
        # HIJO 3
        y = hijo3[i][j]
        hijo3[i][j] = hijo3[i + 1][j]
        hijo3[i + 1][j] = y
        """
		print("HIJO 3")
		print("%i %i %i" % (hijo3[0][0], hijo3[0][1], hijo3[0][2]))
		print("%i %i %i" % (hijo3[1][0], hijo3[1][1], hijo3[1][2]))
		print("%i %i %i" % (hijo3[2][0], hijo3[2][1], hijo3[2][2]))
		print()
		#return hijo3
		"""
    
    if i - 1 >= 0:
        # HIJO 4
        y = hijo4[i][j]
        hijo4[i][j] = hijo4[i - 1][j]
        hijo4[i - 1][j] = y
        """
		print("HIJO 4")
		print("%i %i %i" % (hijo4[0][0], hijo4[0][1], hijo4[0][2]))
		print("%i %i %i" % (hijo4[1][0], hijo4[1][1], hijo4[1][2]))
		print("%i %i %i" % (hijo4[2][0], hijo4[2][1], hijo4[2][2]))
		print()
		#return hijo4
		"""

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

def DFS(puzzle , solucion , num , visitado , arbol , pred):
    # Imprimimos el estado actual del puzzle
    print("Actual: ", puzzle)
    # Alamacenamos este primer estado del puzzle en el arbol, seria nuestro nodo raiz
    arbol.append(puzzle)

    # REALIZAMOS LO SIGUIETE CON LA CONDICION DE QUE NO PODEMOS HABER EXPLORADO MAS DE 200 NODOS
    while arbol and (num < 200):
        # AUMENTAMOS EL VALOR DE NUM PORQUE EXPLORAMOS UN NODO PADRE
        num = num + 1
        # OBTENEMOS UN NODO DE LA COLA PARA EXAMINAR SI ES EL ESTADO OBJETIVO O SUS HIJOS EN CASO CONTRARIO
        nodo = arbol.pop(0)
        #SI ES LA SOLUCION RETORNO UN "TRUE"
        if nodo == solucion:
            return True
        
        #EN CASO DE CONTINUAR BUSCAMOS LOS PREDECESORES A ESTE NODO DE LA SIGUIENTE MANERA
        predecesor = pred[str(nodo)]
        # LOS NODOS HIJOS RESULTAN DE LOS MOVIMIENTOS POSIBLES SE ACUERDO A ESTADO DEL NODO PADRE
        hijos = movimientos(nodo , predecesor)
        # cADA NODO HIJO SE VA A LA COLA DE NODOS POR EXAMINAR
        for i in hijos:
            arbol.append(i)
            # SE GUARDA EN LA BIBLIOTECA DE PREDECESORES LOS PRDECESORES DE EL ACTUL NODO PADRE
            pred[str(i)] = str(nodo)
        # SI EL NODO ACTUAL NO ESTA EN VISITADOS 
        if str(nodo) not in visitado:
            # SE AGREGA A LA LISTA DE NODOS VISITADOS
            visitado.add(str(nodo))
            # APLICAMOS RECURSIVIDAD LLAMANDO NUEVAMENTE A LA FUNCION DFS PARA ANALIZAR LOS NODOS QUE SIGAN EN LA COLA
            DFS(nodo , solucion , num , visitado , arbol , pred)
    return visitado

cant = 0
solucion = [[1,2,3],[4,5,6],[7,8,0]]

print("Solucion: ", solucion)



for j in range(0,10):
    for i in range(0,10):
        # CREAMOS UN PUZZLE ALEATORIO
        puzzle = crea_puzzle(8)
        # NUMERO DE NODOS VISITADOS
        num = 0
        # SE INICIALIZA LA VARIABLE VISITADOS
        visitado = set()
        # SE INICIALIZA UNA COLA DONDE SE ALAMCENARAN NODOS HIJOS POR ANALIZAR
        arbol = []
        # INICIALIZAMOS LA VARIABLE PRED QUE ALAMACENARA NODOS PREDECESORES A LOS NODOS ACTUALMENTE ANALIZADOS
        pred = {str(puzzle):"null"}
        res,flag = DFS(puzzle, solucion, num, visitado, arbol, pred)
        if flag:
            cant = cant + 1
        #print(".")
        print("Puzzle: ", puzzle)
    print(j, " Cantidad: ",cant)
    #print("Res: ",res)
    print("---------------------------------")
promedio = cant / 10
print("Promedio: ", promedio)

#print(pred)
#print(visitado)