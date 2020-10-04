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

visitado = [] #En esta lista se almacenan los nodos visitados.
cola = []    #Inicializamos la cola donde pasaran los por analizar.

#Defimnimos la funcion que realiza el algoritmo del BFS
def bfs(visitado, mapa, estado):
  #Guardo en la lista el nodo inicial
  visitado.append(estado)
  #Guardo en la cola en nodo inicial
  cola.append(estado)

  #Mientras haya nodos en la cola ejecutamos lo siguiente
  while cola:
    #Sacamos el primer nodo en la cola
    n = cola.pop(0) 
    #Imprimimos en pantalla el nodo actual recorrido
    print (n, end = ", ") 

    #Realizamos lo siguiente para los nodos hijos de este nodo actual que acabamos de sacar de la cola
    for vecino in mapa[n]:
      #Si no esta visitado realizamos los siguiente
      if vecino not in visitado:
        #Añadimos el nodo hijo a la lista
        visitado.append(vecino)
        #Guardamos en la cola los nodos hijos del nodo que sacamos de la cola en esta iteracion
        cola.append(vecino)

#Mostramos el mapa
print("\nGrafo del mapa de México: \n")
for llave, lista in mapa.items():
	print(llave, " -> ", lista)

#Pedimos un nodo de inicio
estado = input("\n\nElija un nodo de partida: ")
print("\n\nRecorrido: \n")

#Ejecutamos la funcion bfs para recorrer desde el nodo que pedimos
bfs(visitado, mapa, estado)