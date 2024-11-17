from algoritme_graf import *
from data.vectorization_texts import *
import uuid

participants = load_participants()
id_str = input("Introducir id de usuario: ")
id_usuari = uuid.UUID(id_str)
G = crear_grafo(participants)

def recommend(id_usuari):
    recomendados = []

    if G.nodes[id_usuari]['friend_registration'] != []:
        G_amigos = conexiones_amigos(G, id_usuari)
        for amigo in G_amigos.nodes():
            recomendados.append(amigo)

    if len(recomendados) < G.nodes[id_usuari]['preferred_team_size']:
        # Get edges connected to the user node and sort by weight
        
        graf_nous_usuaris = conexiones_preferencias(G, id_usuari)
        for usuari in graf_nous_usuaris.nodes():
            edges = list(graf_nous_usuaris.edges(id_usuari, data=True))
            edges.sort(key=lambda x: x[2]['weight'], reverse=True)
                
            for edge in edges:
                if len(recomendados) < G.nodes[id_usuari]['preferred_team_size']:
                    node = edge[1] if edge[0] == id_usuari else edge[0]
                    if node not in recomendados:
                        recomendados.append(node)
                else:
                    break

    if id_usuari in recomendados:
        recomendados.remove(id_usuari)
    return recomendados

#print(recomendados)
