# Se declara el tablero como una lista de listas
tablero = [
        ["_","_","_"],
        ["_","_","_"],
        ["_","_","_"],
]

# Función para contar cuantos movimientos quedan disponibles
def movimientos():
    cont = 0
    for i in tablero:
        for j in i:
            if j=="_":
                cont += 1
    return cont
        
# Función para imprimir el tablero
def imprime():
    for i in tablero:
        for j in i:
            print(j," ",end="")
        print()
    print("-----------------------------------------------------------")

# Función para cambiar el caracter _ por el X o la O dependiendo del turno.
def cambiar(x,y,tipo):
    # Se revisa si da una coordenada válida o si es una casilla ocupada
    if (x<1 or x>3) or (y<1 or y>3) or tablero[x-1][y-1]!="_":
        print("*** ERROR - Movimiento no válido ***")
        print("<<ENTER>> para continuar")
        input()
    else:
        tablero[x-1][y-1]=tipo

# Función para revisar si se completó una de las 8 líneas ganadoras
def revisa():
    if tablero[0][0] == tablero[1][0] and tablero[0][0] == tablero[2][0] and tablero[0][0]!="_":
        print(tablero[0][0]," es el ganador")
        print("-----------------------------------------------------------")
    elif tablero[0][1] == tablero[1][1] and tablero[0][1] == tablero[2][1] and tablero[0][1]!="_":
        print(tablero[0][1]," es el ganador")
        print("-----------------------------------------------------------")
    elif tablero[0][2] == tablero[1][2] and tablero[0][2] == tablero[2][2] and tablero[0][2]!="_":
        print(tablero[0][2]," es el ganador")
        print("-----------------------------------------------------------")
    elif tablero[0][0] == tablero[0][1] and tablero[0][0] == tablero[0][2] and tablero[0][0]!="_":
        print(tablero[0][0]," es el ganador")
        print("-----------------------------------------------------------")
    elif tablero[1][0] == tablero[1][1] and tablero[1][0] == tablero[1][2] and tablero[1][0]!="_":
        print(tablero[1][0]," es el ganador")
        print("-----------------------------------------------------------")
    elif tablero[2][0] == tablero[2][1] and tablero[2][0] == tablero[2][2] and tablero[2][0]!="_":
        print(tablero[2][0]," es el ganador")
        print("-----------------------------------------------------------")
    elif tablero[0][0] == tablero[1][1] and tablero[0][0] == tablero[2][2] and tablero[0][0]!="_":
        print(tablero[0][0]," es el ganador")
        print("-----------------------------------------------------------")
    elif tablero[0][2] == tablero[1][1] and tablero[0][2] == tablero[2][0] and tablero[0][2]!="_":
        print(tablero[0][2]," es el ganador")
        print("-----------------------------------------------------------")   
    else:
        return 1

# Ciclo a ejecutarse mientras haya movimientos disponibles y no haya habido ningún ganador
while movimientos()!=0 and revisa()==1:
    print('segimiento')
    revisa()
    imprime()
    # Los turnos pares le corresponderán al jugador de las X y los impares al de las O
    if (movimientos())%2!=0:
        print("Turno para las X")
        coord_x = int(input("Coordenada x:"))
        coord_y = int(input("Coordenada y:"))
        cambiar(coord_x,coord_y,"X")
        imprime()
    else:
        print("Turno para las O")
        coord_x = int(input("Coordenada x:"))
        coord_y = int(input("Coordenada y:"))
        cambiar(coord_x,coord_y,"O")
        imprime()

# Si se acaban las casillas disponibles y no hay ningún ganador se avisa que se terminó el juego
if movimientos()==0 and revisa!=1:
    imprime()
    print("El juego terminó sin ganador")
    
