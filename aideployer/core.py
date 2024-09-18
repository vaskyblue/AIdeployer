from typing import Any, Dict
from pydantic import BaseModel

class Input(BaseModel):
    description: str
    default: Any = None

class Path(str):
    pass

class BasePredictor:
    def setup(self):
        """Cargar el modelo en memoria para hacer eficientes múltiples predicciones"""
        pass
    
    def predict(self, **kwargs):
        """Ejecutar una predicción en el modelo"""
        raise NotImplementedError