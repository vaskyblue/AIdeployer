import importlib

class ModelWrapper:
    def __init__(self, config: 'Config'):
        module_name, class_name = config.predict.split(':')
        module = importlib.import_module(module_name)
        predictor_class = getattr(module, class_name)
        self.predictor = predictor_class()
        self.predictor.setup()

    def predict(self, **kwargs):
        return self.predictor.predict(**kwargs)