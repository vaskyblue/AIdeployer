from aideployer import BasePredictor, Input, Path

class Predictor(BasePredictor):
    def setup(self):
        # Cargar el modelo aquí
        pass

    def predict(self, image: Path = Input(description="Imagen a clasificar")):
        # Realizar la predicción aquí
        return "Resultado de la predicción"