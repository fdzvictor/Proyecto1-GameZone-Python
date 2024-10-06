import random


class Tablero:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero = self.crear_tablero()
        self.barcos = []

    def crear_tablero(self):
        return [["_" for _ in range(self.columnas)] for _ in range(self.filas)]

    def mostrar_tablero(self):
        for fila in self.tablero:
            print(" ".join(fila))
        print()

    def agregar_barco(self, barco):
        for fila, columna in barco.posiciones:
            if not (0 <= fila < self.filas and 0 <= columna < self.columnas):
                print("Error: El barco se sale del tablero.")
                return False
            if self.tablero[fila][columna] != "_":
                print("Error: Esta posición ya está ocupada. Vuélvelo a intentar.")
                return False

        # Si no hay colisión, colocar el barco en las posiciones indicadas
        for fila, columna in barco.posiciones:
            self.tablero[fila][columna] = "B"
        self.barcos.append(barco)
        return True

    def recibir_disparo(self, fila, columna):
        """Registra un disparo en el tablero y verifica si ha impactado en un barco."""
        if self.tablero[fila][columna] == "_":
            print("Agua.")
            self.tablero[fila][columna] = "O"
        elif self.tablero[fila][columna] == "B":
            print("¡Tocado!")
            self.tablero[fila][columna] = "X"
            for barco in self.barcos:
                if (fila, columna) in barco.posiciones:
                    barco.impactos.append((fila, columna))
                    if len(barco.impactos) == len(barco.posiciones):
                        barco.hundido = True
                        print(f"¡{barco.nombre} hundido!")
        else:
            print("Ya disparaste aquí antes.")

    def todos_barcos_hundidos(self):
        """Verifica si todos los barcos han sido hundidos."""
        return all(barco.hundido for barco in self.barcos)


class Barco:
    def __init__(self, nombre, fila, columna, longitud, direccion):
        self.nombre = nombre
        self.longitud = longitud
        self.direccion = direccion
        self.impactos = []
        self.hundido = False
        self.posiciones = self.generar_posiciones(fila, columna)

    def generar_posiciones(self, fila, columna):
        posiciones = []
        for i in range(self.longitud):
            if self.direccion == "H":
                posiciones.append((fila, columna + i))
            elif self.direccion == "V":
                posiciones.append((fila + i, columna))
        return posiciones


def posicionar_barcos(tablero):
    barcos = [
        ("Portaaviones", 5),
        ("Submarino", 3),
        ("Destructor", 3),
        ("Lancha", 2)
    ]

    for nombre, longitud in barcos:
        colocado = False
        while not colocado:
            try:
                print(f"Colocando {nombre} (Longitud: {longitud})")
                tablero.mostrar_tablero()

                fila = int(input(f"Introduce la fila inicial para el {nombre} (0 a {tablero.filas - 1}): "))
                columna = int(input(f"Introduce la columna inicial para el {nombre} (0 a {tablero.columnas - 1}): "))
                direccion = input("Introduce la dirección (H para horizontal, V para vertical): ").upper()
                if direccion not in ["H", "V"]:
                    print("Dirección inválida. Usa 'H' para horizontal o 'V' para vertical.")
                    continue

                # Crear el barco y tratar de colocarlo en el tablero
                barco = Barco(nombre, fila, columna, longitud, direccion)
                if tablero.agregar_barco(barco):
                    print(f"{nombre} colocado correctamente.")
                    colocado = True
                else:
                    print(f"No se pudo colocar el {nombre}. Inténtalo de nuevo.")
            except ValueError:
                print("Valor incorrecto. Introduce números enteros para las coordenadas.")


def jugar_battleship():
    # Crear tableros para el jugador y la máquina
    tablero_jugador = Tablero(10, 10)
    tablero_maquina = Tablero(10, 10)

    print("Colocando tus barcos...")
    posicionar_barcos(tablero_jugador)

    print("Colocando barcos de la máquina...")
    # Colocar barcos de la máquina aleatoriamente
    for nombre, longitud in [("Portaaviones", 5), ("Submarino", 3), ("Destructor", 3), ("Lancha", 2)]:
        colocado = False
        while not colocado:
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            direccion = random.choice(["H", "V"])
            barco_maquina = Barco(nombre, fila, columna, longitud, direccion)
            if tablero_maquina.agregar_barco(barco_maquina):
                print(f"{nombre} de la máquina colocado correctamente.")
                colocado = True

    # Comenzar el juego
    while True:
        # Turno del jugador
        print("--- Tu turno ---")
        tablero_maquina.mostrar_tablero()
        fila = int(input("Introduce la fila para disparar (0-9): "))
        columna = int(input("Introduce la columna para disparar (0-9): "))
        tablero_maquina.recibir_disparo(fila, columna)

        # Verificar si el jugador ha ganado
        if tablero_maquina.todos_barcos_hundidos():
            print("¡Has hundido todos los barcos de la máquina! ¡Ganaste!")
            break

        # Turno de la máquina
        print("--- Turno de la máquina ---")
        fila_maquina = random.randint(0, 9)
        columna_maquina = random.randint(0, 9)
        tablero_jugador.recibir_disparo(fila_maquina, columna_maquina)

        # Verificar si la máquina ha ganado
        if tablero_jugador.todos_barcos_hundidos():
            print("¡Todos tus barcos han sido hundidos! La máquina gana.")
            break
def volver_a_jugar():
    """Pregunta al jugador si desea jugar de nuevo."""
    while True:
        respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if respuesta == 's':
            jugar_battleship()
        elif respuesta == 'n':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Por favor, introduce 's' para sí o 'n' para no.")



