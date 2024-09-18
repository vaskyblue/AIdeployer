import yaml
from pydantic import BaseModel
from typing import Dict, Any, List

class Config(BaseModel):
    build: Dict[str, Any]
    predict: str
    image: str = None
    python_packages: List[str] = []
    system_packages: List[str] = []
    run: List[str] = []

    @classmethod
    def from_yaml(cls, path: str):
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        return cls(**data)