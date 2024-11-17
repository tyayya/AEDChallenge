from simplify import load_participants
from algoritme_graf import crear_grafo, conexiones_amigos, conexiones_preferencias
import recomendaciones
import json

participants = load_participants()
id_usuari = participants[-1].id
G = crear_grafo(participants)

ids_recomendados = recomendaciones.recommend(id_usuari)

perfiles = []
for recomendado in ids_recomendados:
    cars=[]
    for participant in participants:
        if participant.id == recomendado:
            cars = [participant.name,participant.age,participant.introduction]
    perfiles.append(cars)
    
    
with open('perfiles.json', 'w', encoding='utf-8') as f:
    json.dump(perfiles, f, ensure_ascii=False, indent=4)

# Add this code after your existing code in recuser.py
def read_perfiles():
    try:
        with open('perfiles.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Pretty print each profile
            for i, profile in enumerate(data, 1):
                print(f"\nProfile {i}:")
                print(f"Name: {profile[0]}")
                print(f"Age: {profile[1]}")
                print(f"Introduction: {profile[2]}")
                print("-" * 50)
    except FileNotFoundError:
        print("perfiles.json file not found")
    except json.JSONDecodeError:
        print("Error reading JSON file")

# Call the function
read_perfiles()
