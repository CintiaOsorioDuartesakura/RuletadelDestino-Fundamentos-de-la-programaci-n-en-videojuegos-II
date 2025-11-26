import random
from clases.casillas import Casillas 

class Ruleta:
    """
    Clase que representa la ruleta, conteniendo una lista de casillas y lógica para seleccionarla al azar.
    """
    def __init__(self):
        self.__lista_de_casillas: list[Casillas] = []  # Encapsulamiento: lista privada de casillas

    def agregar_casilla(self, casilla: Casillas) -> None:
        """Agrega una casilla a la ruleta."""
        self.__lista_de_casillas.append(casilla)

    def _ordenar_casillas(self) -> None:
        """Mezcla las casillas para simular el giro azaroso."""
        random.shuffle(self.__lista_de_casillas)

    def detenerse(self) -> Casillas:
        """Detiene la ruleta y selecciona una casilla al azar."""
        print("La ruleta se detiene y no sabemos donde muajajaja...")
        self._ordenar_casillas()  # Mezcla antes de elegir
        return random.choice(self.__lista_de_casillas)