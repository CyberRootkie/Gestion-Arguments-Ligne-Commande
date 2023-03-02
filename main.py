import argparse

# On définit les arguments nécessaires, les valeurs par défaut et l'aide
parser = argparse.ArgumentParser()
parser.add_argument("--name", type=str, help="Name of the person", default="JB")
parser.add_argument("--name2", type=str, help="Name of the person 2", default="JB2")

# On récupère les arguments
args = parser.parse_args()

# On les affiche
print(f"coucou {args.name} et {args.name2}")
