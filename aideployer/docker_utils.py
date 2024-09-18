import docker

def build_image(config: 'Config') -> str:
    client = docker.from_env()
    dockerfile = generate_dockerfile(config)
    image, _ = client.images.build(
        path=".",
        dockerfile=dockerfile,
        tag=config.image or "aideployer-model"
    )
    return image.tags[0]

def push_image(image_name: str, registry: str):
    client = docker.from_env()
    client.images.push(registry, tag=image_name)

def generate_dockerfile(config: 'Config') -> str:
    dockerfile = f"""
    FROM python:{config.build.get('python_version', '3.9')}
    
    WORKDIR /app

    RUN apt-get update && apt-get install -y {' '.join(config.system_packages)}

    COPY requirements.txt .
    RUN pip install -r requirements.txt

    COPY . .

    {' && '.join(config.run)}

    CMD ["python", "serve.py"]
    """
    return dockerfile