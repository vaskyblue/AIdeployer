import argparse
from .deployer import deploy

def main():
    parser = argparse.ArgumentParser(description="AIDeployer CLI")
    parser.add_argument("command", choices=["deploy"], help="Comando a ejecutar")
    parser.add_argument("--config", default="aideployer.yaml", help="Ruta al archivo de configuración")

    args = parser.parse_args()

    if args.command == "deploy":
        deploy(args.config)

if __name__ == "__main__":
    main()