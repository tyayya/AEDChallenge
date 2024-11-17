from simplify import load_participants
from algoritme_graf import crear_grafo, conexiones_amigos, conexiones_preferencias
from recomendaciones import recommend

participants = load_participants()
id_usuari = participants[-1].id
G = crear_grafo(participants)

ids_recomendados = recommend(id_usuari,G)

perfiles = []
for recomendado in ids_recomendados:
    cars=[]
    for participant in participants:
        if participant.id == recomendado:
            cars = [participant.name,participant.age,participant.introduction]
    perfiles.append(cars)

