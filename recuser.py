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

print('a')
