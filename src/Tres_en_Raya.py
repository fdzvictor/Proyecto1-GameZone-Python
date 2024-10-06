import random

class Tablero:
    def __init__(self, filas, columnas, lleno=0):
        self.filas = filas
        self.columnas = columnas
        self.estado = lleno
        self.tablero = self.crear_tablero()
    
    def crear_tablero(self):
        return [["_" for _ in range(self.columnas)] for _ in range(self.filas)]
    
    def mostrar_tablero(self):
        for fila in self.tablero:
            print(fila)
        print()

    def mover_X(self):
        try:
            fila = int(input("Fila (0 a 2): "))
            columna = int(input("Columna (0 a 2): "))
            if 0 <= fila < self.filas and 0 <= columna < self.columnas and self.tablero[fila][columna] == "_":
                self.tablero[fila][columna] = "X"
                self.mostrar_tablero()
            else:  
                print("Coordenadas inválidas o espacio ocupado. Inténtalo de nuevo.")
        except ValueError:
            print("Valor incorrecto. Introduce un número.")

    def mover_O(self):
        try:
            fila = int(input("Fila (0 a 2): "))
            columna = int(input("Columna (0 a 2): "))
            if 0 <= fila < self.filas and 0 <= columna < self.columnas and self.tablero[fila][columna] == "_":
                self.tablero[fila][columna] = "O"
                self.mostrar_tablero()
            else:  
                print("Coordenadas inválidas o espacio ocupado. Inténtalo de nuevo.")
        except ValueError:
            print("Valor incorrecto. Introduce un número.")

    def tresenraya(self):
        # Revisar filas
        for fila in self.tablero:
            if fila == ["X"] * self.columnas:
                print("¡Gana Jugador 1!")
                return True
            elif fila == ["O"] * self.columnas:
                print("¡Gana Jugador 2!")
                return True

        # Revisar columnas
        for col in range(self.columnas):
            valores_columna = [self.tablero[fila][col] for fila in range(self.filas)]
            if valores_columna == ["X"] * self.filas:
                print("¡Gana Jugador 1!")
                return True
            elif valores_columna == ["O"] * self.filas:
                print("¡Gana Jugador 2!")
                return True

        # Revisar diagonal principal
        if all(self.tablero[i][i] == "X" for i in range(self.columnas)):
            print("¡Gana Jugador 1 en diagonal!")
            return True
        elif all(self.tablero[i][i] == "O" for i in range(self.columnas)):
            print("¡Gana Jugador 2 en diagonal!")
            return True

        # Revisar diagonal secundaria
        if all(self.tablero[i][self.columnas - 1 - i] == "X" for i in range(self.filas)):
            print("¡Gana Jugador 1 en diagonal!")
            return True
        elif all(self.tablero[i][self.columnas - 1 - i] == "O" for i in range(self.filas)):
            print("¡Gana Jugador 2 en diagonal!")
            return True

        return False

    def tablero_lleno(self):
        for fila in self.tablero:
            if "_" in fila:
                return False
        return True

    def iniciar_partida(self):
        print("¡Comienza el juego!")
        self.mostrar_tablero()
        turno = random.choice(["X", "O"])

        while not self.tablero_lleno():
            print(f"Turno del jugador {turno}")

            if turno == "X":
                self.mover_X()
            else:
                self.mover_O()

            if self.tresenraya():
                break

            turno = "O" if turno == "X" else "X"

        if self.tablero_lleno() and not self.tresenraya():
            print("Empate. No quedan más movimientos posibles.")


# Crear el juego y empezar
tablero_3x3 = Tablero(3, 3)
tablero_3x3.iniciar_partida()

