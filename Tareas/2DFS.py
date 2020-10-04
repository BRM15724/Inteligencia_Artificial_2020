#Defino mi diccionario de estados
mapa = {
  'NLE' : ['COA','JAL','TAM'],
  'COA' : ['NLE', 'DUR'],
  'JAL' : ['DUR','MIC','NLE'],
  'TAM' : ['NLE','SLP','YUC'],
  'DUR' : ['SIN','COA','JAL'],
  'MIC' : ['JAL','ZAC'],
  'SLP' : ['TAM','ZAC'],
  'YUC' : ['TAM','CAM'],
  'SIN' : ['CHH','DUR'],
  'ZAC' : ['SLP','MIC','VER','GRO'],
  'CAM' : ['YUC','ROO','CHP'],
  'CHH' : ['SON','BCS','SIN'],
  'VER' : ['ZAC','CHP'],
  'GRO' : ['ZAC','OAX'],
  'ROO' : ['CAM'],
  'CHP' : ['OAX','VER','CAM'],
  'SON' : ['BCN','CHH'],
  'OAX' : ['GRO','CHP'],
  'BCN' : ['SON','BCS'],
  'BCS' : ['BCN','CHH']
}

visitados = set() #En esta lista se almacenan los nodos visitados.

#Defimnimos la funcion que realiza el algoritmo del DFS
def dfs(visitados, mapa, estado):
    #Si no se ha visitado este nodo realizamos lo siguiente
    if estado not in visitados:
        #Imprimimos este nodo no visitado
        print (estado, end = " ")
        #Agregamos este nodo visitado a la lista de nodos visitados
        visitados.add(estado)
        #Para cada uno de los nodos hijos aplicamos recursividad con esta misma funcion para analizarlos
        for vecinos in mapa[estado]:
            dfs(visitados, mapa, vecinos)

#Mostramos el mapa
print("\nGrafo del mapa de México: \n")
for llave, lista in mapa.items():
	print(llave, " -> ", lista)

#Pedimos un nodo de inicio
estado = input("\n\nElija un nodo de partida: ")
print("\n\nRecorrido: \n")

#Ejecutamos la funcion bfs para recorrer desde el nodo que pedimos
dfs(visitados, mapa, estado)