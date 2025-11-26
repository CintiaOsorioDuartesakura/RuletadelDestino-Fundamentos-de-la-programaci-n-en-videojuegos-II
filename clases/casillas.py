from abc import ABC, abstractmethod

# Clase base abstracta para todas las casillas de la ruleta
class Casillas(ABC):
    """
    Clase base abstracta para casillas en la ruleta. Maneja puntos y define interfaces para polimorfismo.
    """
    def __init__(self, puntos: int):
        self.__puntos_de_casilla = puntos  # Encapsulamiento: atributo privado

    def get_puntos(self) -> int:
        """Getter para obtener los puntos de la casilla."""
        return self.__puntos_de_casilla

    @abstractmethod
    def mostrar_puntos(self) -> None:
        """Método abstracto: Muestra el efecto de la casilla. Debe implementarse en hijas."""
        pass

    @abstractmethod
    def aplicar_efecto(self, puntos_actuales: int) -> int:
        """Método abstracto: Aplica el efecto a los puntos del usuario. Devuelve los puntos actualizados."""
        pass

# Clase hija: Casilla de victoria (suma puntos)
class CasillaWin(Casillas):
    """
    Casilla que suma puntos al usuario.
    """
    def __init__(self, puntos: int):
        super().__init__(puntos)

    def mostrar_puntos(self) -> None:
        print(f"¡Ganaste {self.get_puntos()} puntos! Como una runa de Gebo que une fortunas.")

    def aplicar_efecto(self, puntos_actuales: int) -> int:
        # Lógica: suma los puntos
        return puntos_actuales + self.get_puntos()

# Clase hija: Casilla de pérdida (resta puntos)
class CasillaLose(Casillas):
    """
    Casilla que resta puntos al usuario.
    """
    def __init__(self, puntos: int):
        super().__init__(puntos)

    def mostrar_puntos(self) -> None:
        print(f"Perdiste {self.get_puntos()} puntos... Como un viento de Algiz que prueba tu resistencia.")

    def aplicar_efecto(self, puntos_actuales: int) -> int:
        # Lógica: resta los puntos, pero no baja de 0
        return max(0, puntos_actuales - self.get_puntos())

# Clase hija: Casilla de muerte (resetea puntos)
class CasillaMorir(Casillas):
    """
    Casilla que resetea todos los puntos del usuario a 0.
    """
    def __init__(self, puntos: int = 0):  # Puntos por default 0, ya que es muerte
        super().__init__(puntos)

    def mostrar_puntos(self) -> None:
        print("¡Oh no! Casilla de Muerte. Adiós puntos, Haz morido.")

    def aplicar_efecto(self, puntos_actuales: int) -> int:
        # Lógica: resetea a 0
        return 0