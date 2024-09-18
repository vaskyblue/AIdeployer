from setuptools import setup, find_packages

setup(
    name="aideployer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pydantic",
        "PyYAML",
        "docker",
        "fastapi",
        "uvicorn"
    ],
    entry_points={
        "console_scripts": [
            "aideployer=aideployer.cli:main",
        ],
    },
)