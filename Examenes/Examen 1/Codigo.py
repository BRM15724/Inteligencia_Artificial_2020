
mapa = {   #ESTE MAPA ME INDICA LOS ESTADOS VECINOS
  19 : [8,24,28],
  8 : [6,10,32,19],
  24 : [19,32,12,22,14,30,28],
  28 : [19,24,30],
  6 : [26,25,10,8],
  10 : [6,25,18,15,32,8],
  32 : [8,10,15,1,24],
  12 : [24,15,16,22],
  22 : [24,12,16,11,14],
  14 : [24,22,11,29,21,30],
  30 : [28,24,14,21,20,5,27],
  26 : [2,6,25],
  25 : [26,6,10,18],
  18 : [25,10,15],
  15 : [18,10,32,1,12,16,9],
  1 : [32,15],
  16 : [9,15,12,22,11,13],
  11 : [16,22,14,29,21,7,17,13],
  29 : [14,21,11],
  21 : [29,14,30,20,13,17,11,],
  20 : [13,21,30,5],
  5 : [20,30,27,],
  27 : [30,5,4],
  2: [3,26],
  3: [2],
  7 : [11,17],
  9 : [15,16],
  13 : [16,11,17,21,20],
  17 : [11,7,21,13],
  4 : [27,23,31],
  23 : [31,4],
  31 : [4,23]
}

estado_republica = {  #ESTA BIBLIOTECA ME INDICA EL ESTADO Y EL COLOR DEL QUE ESTA PINTADO, COLORES: 0 - BLANCO , 1 - ROJO , 2 - AMARILLO , 3 - VERDE, 4 - AZUL , 5- MORADO
1 : [ "Aguascalientes"] ,
2 : [ "Baja Califor"],
3 : [ "Baja California Sur"],
4 :[ "Campeche"],
5 :[ "Chiapas"],
6 :[ "Chihuahua"],
7 :[ "Ciudad de México"],
8 :[ "Coahuila"],
9 :[ "Colima"],
10:[ "Durango"],
11 :[ "Estado de México"],
12 :[ "Guanajuato"],
13 :[ "Guerrero"],
14 :[ "Hidalgo"],
15 :[ "Jalisco"],
16 :[ "Michoacán"],
17 :[ "Morelos"],
18 :[ "Nayarit"],
19 :[ "Nuevo León"],
20 :[ "Oaxaca"],
21 :[ "Puebla"],
22 :[ "Querétaro"],
23 :[ "Quintana Roo"],
24 :[ "San Luis Potosí"],
25 :[ "Sinaloa"],
26 :[ "Sonora"],
27 :[ "Tabasco"],
28 :[ "Tamaulipas"],
29 :[ "Tlaxcala"],
30 :[ "Veracruz"],
31 :[ "Yucatán"],
32 :[ "Zacatecas"]
}

colores_de_estado = {  #ESTA BIBLIOTECA ME INDICA EL ESTADO Y EL COLOR DEL QUE ESTA PINTADO, COLORES: 0 - BLANCO , 1 - ROJO , 2 - AMARILLO , 3 - VERDE, 4 - AZUL , 5- MORADO
1 : 0 ,
2 : 0,
3 : 0,
4 :0,
5 :0,
6 :0,
7 :0,
8 :0,
9 :0,
10:0,
11 :0,
12 :0,
13 :0,
14 :0,
15 :0,
16 :0,
17 :0,
18 :0,
19 :0,
20 :0,
21 :0,
22 :0,
23 :0,
24 :0,
25 :0,
26 :0,
27 :0,
28 :0,
29 :0,
30 :0,
31 :0,
32 :0
}

color = {
  0 : ["Blanco"],
  1 : ["Rojo"],
  2 : ["Amarillo"],
  3 : ["Verde"],
  4 : ["Azul"],
  5 : ["Morado"],

}

visitados = set() #AQUI SE ALMACENAN LOS ESTADOS DE LA REPUBLICA VISITADOS

def Pintar_Estado(estado , mapa , colores_de_estado , cont , color , estado_republica):
  colores_alrededor=set() #AQUI ALMACENO LOS COLORES QUE ESTAN ALREDEDOR DE UN ESTADO DE LA REPUBLICA
  estado=(int)(estado)
  for vecinos in mapa[estado]:
    #PARA CADA VECINO AGREGO SU COLOR A UNA LISTA
    colores_alrededor.add(colores_de_estado[vecinos])

  #YA QUE TENGO TODOS LOS COLORES DE MI ALREDEDOR PREGUNTO SI UN COLOR ESTA EN LA LISTA, SI LO ESTA PREGUNTO POR OTRO
  for i in [1, 2, 3, 4, 5]:
    if i not in colores_alrededor:
      cont=cont+1
      colores_de_estado[estado]=i
      print( estado_republica[estado]," : ",color[i])
      break
  return colores_de_estado





#DEFINIMOS ESTA FUNCION PARA Recorrido_Mapa ORRER EL MAPA DE LA REPUBLICA
def Recorrido_Mapa (visitados, mapa, estado , colores_de_estado,cont,color , estado_republica):
    
    if estado not in visitados: #CONDICION DEESTADO REALIZAMOS LO SIGUIENTE
        #Imprimimos este nodo no visitado
        #print (estado, end = " ")
        
        visitados.add(estado) #AGREGAMOS EL ESTADO ACTUAL VISITADO A LA LISTA DE ESTADOS VISITADOS

        #AQUI MANDO A LLAMAR A LA FUNCION PINTAR, QUE ES LA QUE DECIDE DE QUE COLOR PINTAR UN ESTADO TOMANDO EN CUENTA LOS COLORES DE LSO ESTADOS VECINOS
        colores_de_estado=Pintar_Estado(estado , mapa , colores_de_estado,cont,color , estado_republica)
        #Para cada uno de los nodos hijos aplicamos Recorrido_Mapa ursividad con esta misma funcion para analizarlos
        for vecinos in mapa[estado]:
            Recorrido_Mapa (visitados, mapa, vecinos , colores_de_estado,cont,color , estado_republica)



#MOSTRAMOS EL MAPA
print("\nGrafo del mapa de México: \n")
for llave, lista in mapa.items():
  print(llave, " -> ", lista)

#PIDO UN NODO DE INICIO (PARA POBAR EL Recorrido_Mapa ORRIDO)
estado = input("\n\nElija un nodo de partida: ")
print("\n\nRecorrido_Mapa orrido: \n")
estado=(int)(estado)
cont=1
#colores_de_estado[1]=5
#print(colores_de_estado[1]*2)
#print(mapa[estado])
#Recorrido_Mapa ORREMOS EL MAPA DESDE EL ESTADO DE LA REPUBLICA INDICADO CON ENTERIORIDAD
Recorrido_Mapa (visitados, mapa, estado , colores_de_estado , cont,color , estado_republica)
