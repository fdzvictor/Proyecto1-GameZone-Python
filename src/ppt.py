import random

class Ppt:
    def __init__(self, ganar1, ganar2, perder1,perder2):
        # Definimos las opciones y sus debilidades
        self.ganar1 = ganar1
        self.perder2 = perder2
        self.ganar2 = ganar2
        self.perder1 = perder1
            
    piedra = Ppt("tijera", "lagarto","papel","Spock")
    papel = Ppt ("piedra", "Spock","tijera","lagarto")
    tijera = Ppt ("papel", "lagarto","piedra","Spock")
    lagarto= Ppt ("Spock", "papel", "piedra","tijera"),
    Spock: = Ppt ("tijera", "piedra","lagarto", "papel"),


    def jugar_ppt(self):
        print("¡Bienvenido al juego de Piedra, Papel, Tijera, Lagarto, Spock!")
        print("Las opciones son: piedra, papel, tijera, lagarto, Spock")

        while True:
            # Obtener la opción del jugador
            eleccion_jugador = input("Elige tu opción (o escribe 'salir' para terminar): ").lower()
            #Aqui tengo que linkearlo al menu

            if eleccion_jugador == 'salir':
                print("Gracias por jugar. ¡Hasta la próxima!")
                break
            
            if eleccion_jugador not in self.opciones:
                print("Opción no válida. Intenta de nuevo.")
                continue

            # Elección de la computadora
            eleccion_computadora = random.choice(list(self.opciones.keys()))
            print(f"La computadora eligió: {eleccion_computadora}")

            # Determinar el resultado
            if eleccion_jugador == eleccion_computadora:
                print("¡Es un empate!")
            elif eleccion_computadora in self.opciones[eleccion_jugador]["gana"]:
                print(f"¡{eleccion_jugador.capitalize()} gana a {eleccion_computadora}!")
            else:
                print(f"¡{eleccion_computadora.capitalize()} gana a {eleccion_jugador}!")


