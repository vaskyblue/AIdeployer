from fastapi import FastAPI
from .model_wrapper import ModelWrapper

def generate_api(config: 'Config'):
    app = FastAPI()
    model = ModelWrapper(config)

    @app.post("/predict")
    async def predict(input_data: dict):
        return model.predict(**input_data)

    with open("serve.py", "w") as f:
        f.write("""
import uvicorn
from fastapi import FastAPI
from aideployer.model_wrapper import ModelWrapper
from aideployer.config import Config

app = FastAPI()
config = Config.from_yaml("aideployer.yaml")
model = ModelWrapper(config)

@app.post("/predict")
async def predict(input_data: dict):
    return model.predict(**input_data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
        """)

    return app