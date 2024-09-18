from .docker_utils import build_image, push_image
from .api_generator import generate_api
from .config import Config

def deploy(config_path: str):
    config = Config.from_yaml(config_path)
    image_name = build_image(config)
    if config.image:
        push_image(image_name, config.image)
    generate_api(config)
    print(f"Modelo desplegado como {image_name}")