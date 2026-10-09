"""Interfaz común para las estrategias de modelado de villanos."""

from abc import ABC, abstractmethod
from typing import Any


class BaseStrategy(ABC):
    @abstractmethod
    def get_action(self, state: Any) -> Any:
        """Devuelve la acción que el villano debería tomar dado un estado/situación de juego."""
        pass