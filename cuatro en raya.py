#NOTA: los comentarios son solamente para poder entender y guiarme con mas facilidad
#Son para referencia personal

def tableroVacio(): #esto es una lista con 6 listas de 7 elementos, que conforman el tablero
    return[ 
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0], #esta es la 6ta
    ]

def completarTableroEnOrden(secuencia, tableroVacio):
    ficha = 1 #(turno)
    for columna in secuencia:
        tableroVacio = soltarFichaEnTablero(ficha, columna, tableroVacio)
        if ficha == 1:
           ficha = 2
        else:
            ficha = 1
    return tableroVacio
    
def soltarFichaEnTablero(ficha, columna, tablero): #esta funcion la va a llamar completar tablero en orden
    for fila in range(6, 0, -1): #fila esta siendo declarado, range va de 6 a 0 bajando de a 1
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return tablero #el return tiene que estar incluido en el if para que tire una sola ficha por llamado a la funcion
            #porque de no ser así, se embatata* y revisa 6 veces donde no tiene que hacerlo

def deteccionError(secuencia):
    for x in secuencia:
        if x > 7 or x < 1:
            print("Se ingreso un numero invalido en la secuencia.")
            return 2
    return 1

secuencia = [1, 2, 3, 1, 8]
error = deteccionError(secuencia)
if error == 1:
    dibujarTablero( 
        completarTableroEnOrden(
            secuencia, tableroVacio() #para completar el tablero le envío el orden de los tiros y la lista de listas
        )
    )
