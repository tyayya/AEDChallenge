from algoritme_graf import *

id_usuari = input()
G = crear_grafo(participants)

recomendados = []
def recomendaciones_amigos(G, id_usuari): #Función que devuelve una lista con los amigos del usuario

    G_amigos = conexiones_amigos(G, id_usuari)
    for amigo in G_amigos.nodes():
        recomendados.append(amigo)
    return recomendados

if len(recomendados) < G[id_usuari]['preferred_team_size']:
    # Get edges connected to the user node and sort by weight
    edges = G.edges(id_usuari, data=True)
    sorted_edges = sorted(edges, key=lambda x: x[2]['weight'], reverse=True)
    
    # Select top preferred_team_size nodes
    top_nodes = [edge[1] for edge in sorted_edges[:'preferred_team_size']]
    
    # Add top nodes to recomendados
    recomendados.extend(top_nodes)


